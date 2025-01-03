## Low-Event-Diffing

Low-Event-Diffing is a cybersecurity tool designed to compare application-related events and logs across hosts, identifying anomalous differences.

### Installation

1. Clone the repository: `git clone https://github.com/ShadowStrikeHQ/low-Event-Diffing.git`
2. Change directory: `cd low-Event-Diffing`
3. Install requirements: `pip install -r requirements.txt`

### Usage

```
python main.py [options]

Options:
  -h, --help            show this help message and exit
  --host HOST           Host to analyze (default: localhost)
  --port PORT           Port to analyze (default: 22)
  --username USERNAME   Username to use for SSH connection (default: root)
  --password PASSWORD   Password to use for SSH connection
  --keyfile KEYFILE     Path to SSH private key file
  --log-file LOG_FILE   Path to log file
  --verbose             Enable verbose output
```

**Example:**

```
python main.py --host 192.168.1.100 --port 22 --username user --password password --log-file /tmp/logs.txt
```

### Security Warnings and Considerations

* Ensure that the host you are analyzing is trusted and authorized for remote access.
* Use strong passwords or SSH keys to secure the remote connection.
* Review the log file carefully for any suspicious or anomalous activity.

### License

This software is licensed under the GNU General Public License v3.0.