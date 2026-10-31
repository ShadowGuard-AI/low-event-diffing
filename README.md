![Banner](banner.png)

## Low-Event-Diffing

Low-Event-Diffing is a cybersecurity tool designed to compare application-related events and logs across hosts, identifying anomalous differences.

### Installation

1. Clone the repository: `git clone https://github.com/ShadowStrikeHQ/low-Event-Diffing.git`
2. Change directory: `cd low-Event-Diffing`
3. No install step is needed beyond the clone: the tool uses only the Python standard library.

### Usage

```
python main.py -f1 FILE1 -f2 FILE2 [-o OUTPUT]

Options:
  -h, --help            show this help message and exit
  -f1 FILE1, --file1 FILE1
                        Path to the first log/event file.
  -f2 FILE2, --file2 FILE2
                        Path to the second log/event file.
  -o OUTPUT, --output OUTPUT
                        Path to save the diff results.
  -v, --version         Show tool version.
```

The tool compares two local log or event files and prints a unified diff of the anomalous differences. It does not connect to a remote host.

The saved diff names both input files in its headers. When `-o` is given, the output file is always written: if the files match, it holds a single line saying no differences were found. An output path that resolves to either input file, including through a symlink, is refused at exit 1, and a run that cannot read an input exits 1.

**Example:**

```
python main.py -f1 host1-events.txt -f2 host2-events.txt -o diff-output.txt
```

### Security Warnings and Considerations

* Review the diff output carefully for any suspicious or anomalous activity.
* Only compare log or event files you are authorized to inspect.

### License

This software is licensed under the GNU General Public License v3.0.