# Smart Backup Utility

A Python-based backup automation utility for creating reliable backups of files and directories with incremental backup support, verification, logging, and command-line configuration.

## Features

- Incremental backup support
- File-change detection
- Duplicate handling
- Preview mode with confirmation
- Backup verification
- Ignore rules
- Logging and backup reports
- Command-line arguments for source and destination paths
- Versioned implementations from `v3.1` to `v3.6`
- Docker support

## Project Structure

```text
.
├── v3.1/                 # Initial version
├── v3.2/                 # Improved backup functionality
├── v3.3/                 # Further improvements
├── v3.4/                 # Extended functionality
├── v3.5/                 # Improved backup workflow
├── v3.6/                 # Latest version
├── dockerfile
└── .dockerignore
```

## Technologies

- Python
- JSON configuration
- Logging
- Docker

## Safety

Test the utility with sample directories before using it with important data. Verify backup output and destination paths carefully.

## What I Learned

- Building file-backup automation with Python
- Working with files, directories, and metadata
- Implementing incremental backup logic
- Handling errors and logging
- Verifying backup integrity
- Containerizing a Python application with Docker
