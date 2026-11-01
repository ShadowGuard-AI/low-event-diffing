import argparse
import logging
import os
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_argparse():
    """
    Set up the command-line argument parser.

    Returns:
        argparse.ArgumentParser: Configured argument parser.
    """
    parser = argparse.ArgumentParser(
        description="Tool for comparing application-related events and logs across hosts, finding anomalous differences."
    )
    parser.add_argument(
        '-f1', '--file1', required=True, help="Path to the first log/event file."
    )
    parser.add_argument(
        '-f2', '--file2', required=True, help="Path to the second log/event file."
    )
    parser.add_argument(
        '-o', '--output', required=False, help="Path to save the diff results."
    )
    parser.add_argument(
        '-v', '--version', action='version', version='low-Event-Diffing 1.0', help="Show tool version."
    )
    return parser

def diff_events(file1, file2):
    """
    Compare two event/log files and find anomalous differences.

    Args:
        file1 (str): Path to the first file.
        file2 (str): Path to the second file.

    Returns:
        list: List of differences found between the files.
    """
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            events1 = f1.readlines()
            events2 = f2.readlines()

        # Use difflib for a simple comparison
        from difflib import unified_diff
        # unified_diff with its default three lines of context. lineterm is
        # emptied because the content lines already carry their own newlines;
        # the header lines the generator adds would otherwise be the only ones
        # without. Nothing here sorts or normalises the events first, so the
        # same events in a different order diff as changes, and timestamps
        # make near identical logs differ on every line that carries one.
        differences = list(unified_diff(events1, events2, fromfile=file1, tofile=file2, lineterm=''))
        return differences
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred while diffing files: {e}")
        raise

def main():
    """
    Main function to execute the low-Event-Diffing tool.
    """
    parser = setup_argparse()
    args = parser.parse_args()

    logging.info("Starting low-Event-Diffing tool...")

    if args.output:
        resolved_output = os.path.realpath(args.output)
        if resolved_output in (os.path.realpath(args.file1), os.path.realpath(args.file2)):
            logging.error(f"Output path {args.output} resolves to an input file. Refusing to overwrite an input.")
            sys.exit(1)

    try:
        differences = diff_events(args.file1, args.file2)

        # Differences do not change the exit code. A run that finds a hundred
        # differing lines and a run that finds none both exit 0; only a file
        # that cannot be read exits 1, through the handler below. A script
        # gating on this tool has to read its output, not its status.
        if differences:
            # Diff lines from the files already end with newlines, so strip
            # them before joining or every content line gains a blank line.
            normalized = [line.rstrip('\n') for line in differences]
            logging.info("Differences found:")
            for line in normalized:
                print(line)

            if args.output:
                with open(args.output, 'w') as outfile:
                    outfile.write("\n".join(normalized) + "\n")
                logging.info(f"Differences saved to {args.output}")
        else:
            logging.info("No differences found between the files.")
            if args.output:
                with open(args.output, 'w') as outfile:
                    # The no-difference sentence is written into the output file as its
                    # whole content, so a saved result is never an empty file that a
                    # reader could mistake for a run that produced nothing.
                    outfile.write("No differences found between the files.\n")
                logging.info(f"No differences found. That result was saved to {args.output}")
    except SystemExit:
        raise
    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()