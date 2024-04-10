# Project "File Falcon"

"File Falcon" is a swift and efficient Python script that swoops into your Downloads directory, picks up loose files, and neatly nests them into respective folders based on their file extensions. It uses a JSON configuration file to determine which file types belong to which directories. If a directory for a file type doesn't exist, the script creates it. Files with unknown types are placed in an 'Others' nest. When the File Falcon finishes its task, it sends a desktop notification.

## Requirements

File Falcon requires Python 3 and the dependencies listed in the `requirements.txt` file.

You can install the required Python packages using pip:

```bash
pip3 install -r requirements.txt
```

## Usage

1. Edit the JSON configuration file named `config.json` in the same directory as the script or create your own. The configuration file maps directory names to lists of file extensions. Here's an example:

```json
{
  "Images": ["jpg", "jpeg", "png"],
  "Documents": ["doc", "docx", "pdf"],
  "Others": []
}
```

1. Unleash the Falcon:

```bash
python3 main.py
```

The File Falcon will organize the files in your Downloads directory according to the configuration file and send a desktop notification when it's done.

## Note

File Falcon is designed for macOS. The desktop notification feature uses the `pync` library, which is a Python wrapper for macOS's native notification system. If you're using a different operating system, you may need to modify the script to use a different library for sending desktop notifications.
