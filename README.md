![Banner](banner.png)

## Low-Event-Diffing

Low-Event-Diffing is a cybersecurity tool designed to compare application-related events and logs across hosts, identifying anomalous differences.

### Installation

1. Clone the repository: `git clone https://github.com/ShadowStrikeHQ/low-Event-Diffing.git`
2. Change directory: `cd low-Event-Diffing`
3. Install requirements: `pip install -r requirements.txt`

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

**Example:**

```
python main.py -f1 host1-events.txt -f2 host2-events.txt -o diff-output.txt
```

### Security Warnings and Considerations

* Review the diff output carefully for any suspicious or anomalous activity.
* Only compare log or event files you are authorized to inspect.

### License

This software is licensed under the GNU General Public License v3.0.