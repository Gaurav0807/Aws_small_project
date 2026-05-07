# MyCLI - AWS S3 Command Line Tool

A simple and powerful command-line interface for interacting with AWS S3 buckets using Python and Typer.

## Features

- ✅ List S3 buckets from your AWS account
- ✅ Simple command interface
- ✅ Easy to integrate into other projects
- ✅ Built with Python, Typer, and Boto3

---

## Installation

### Option 1: Install from GitHub (Recommended)

```bash
pip install git+https://github.com/Gaurav0807/Aws_small_project.git#subdirectory=cli_tool
```

### Option 2: Install Locally

```bash
git clone https://github.com/Gaurav0807/Aws_small_project.git
cd Aws_small_project/cli_tool
pip install -e .
```

---

## Prerequisites

You need AWS credentials configured on your machine:

```bash
aws configure
```

Or set environment variables:
```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
```

---

## Usage

### Available Commands

After installation, you can use the following commands:

#### 1. List S3 Buckets
```bash
mycli buckets
```

**Output:**
```
bucket-1
bucket-2
my-data-bucket
```

#### 2. Hello Command
```bash
mycli hello gaurav
```

**Output:**
```
Hello :gaurav
```

#### 3. Test Command
```bash
mycli test something
```

**Output:**
```
Test :something
```

### View Help

```bash
mycli --help
```

---

## Usage in Other Projects

### Method 1: Use as CLI Command

```bash
mycli buckets
```

### Method 2: Import in Python Code

```python
from my_cli.s3 import list_bucket

# Get all S3 buckets
buckets = list_bucket()

for bucket in buckets:
    print(f"Bucket Name: {bucket['Name']}")
```

### Method 3: Use as subprocess in Python

```python
import subprocess

result = subprocess.run(["mycli", "buckets"], capture_output=True, text=True)
print(result.stdout)
```

---

## Project Structure

```
cli_tool/
├── my_cli/
│   ├── __init__.py
│   ├── main.py          # CLI entry point with Typer
│   └── s3.py            # S3 functions using Boto3
├── setup.py             # Package configuration
├── requirements.txt     # Dependencies
└── README.md           # This file
```

---

## Dependencies

- **typer** - CLI framework
- **boto3** - AWS SDK for Python
- **python** >= 3.8

---

## Examples

### Example 1: List Buckets in Your Script

```python
#!/usr/bin/env python3
from my_cli.s3 import list_bucket

def main():
    print("📦 Your S3 Buckets:")
    print("-" * 40)
    
    buckets = list_bucket()
    
    if not buckets:
        print("No buckets found!")
        return
    
    for idx, bucket in enumerate(buckets, 1):
        print(f"{idx}. {bucket['Name']}")

if __name__ == "__main__":
    main()
```

### Example 2: Terminal Usage

```bash
# Install
pip install git+https://github.com/Gaurav0807/Aws_small_project.git#subdirectory=cli_tool

# Use
mycli buckets
mycli hello "World"
mycli test "my-test"
```

---

## Troubleshooting

### Command not found: `mycli`

Make sure you installed the package:
```bash
pip install git+https://github.com/Gaurav0807/Aws_small_project.git#subdirectory=cli_tool
```

### AWS credentials not found

Configure AWS credentials:
```bash
aws configure
```

Or set environment variables:
```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
```

### Permission denied

Try installing with `--user`:
```bash
pip install --user git+https://github.com/Gaurav0807/Aws_small_project.git#subdirectory=cli_tool
```

---

## Contributing

Feel free to fork and submit pull requests!

---

## License

MIT License - See LICENSE file for details

---

## Author

Created by **Gaurav** - [GitHub](https://github.com/Gaurav0807)

---

## Support

For issues and questions, open an issue on [GitHub Issues](https://github.com/Gaurav0807/Aws_small_project/issues)
