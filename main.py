import argparse
import logging
from pwn import *

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
        differences = list(unified_diff(events1, events2, lineterm=''))
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

    try:
        differences = diff_events(args.file1, args.file2)

        if differences:
            logging.info("Differences found:")
            for line in differences:
                print(line)

            if args.output:
                with open(args.output, 'w') as outfile:
                    outfile.writelines("\n".join(differences))
                logging.info(f"Differences saved to {args.output}")
        else:
            logging.info("No differences found between the files.")
    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")

if __name__ == '__main__':
    main()