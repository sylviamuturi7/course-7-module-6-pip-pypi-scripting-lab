# Python Automation Lab - Pip, PyPi & Scripting

This is my lab project for learning how to automate tasks with Python. I built a simple tool that fetches data from an API and writes log files automatically.

## What I Built

I created a Python script that:
- Fetches data from a public API using the `requests` library
- Generates log files with timestamps in the filename
- Writes user activity logs to text files
- Can be run from the command line

## How to Run This Project

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd course-7-module-6-pip-pypi-scripting-lab
```

### 2. Install dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Run the script
```bash
python lib/generate_log.py
```

This will create a log file named something like `log_20250302.txt` with today's date.

## What I Learned

- How to use `pip` to install external packages like `requests`
- Writing Python scripts that can run from the command line
- Using File I/O to write data to files
- Tracking project dependencies in `requirements.txt`
- Making reusable functions with the `if __name__ == "__main__"` pattern

## Project Structure

```
├── lib/
│   ├── __init__.py
│   └── generate_log.py    # Main script with log generation logic
├── testing/
│   ├── __init__.py
│   └── test_generate_log.py    # Tests for the script
├── requirements.txt       # All the packages needed to run this
├── Pipfile               # Alternative dependency management
└── README.md             # This file
```

## Dependencies

This project uses:
- **requests** - for making HTTP requests to external APIs
- **pytest** - for running tests (dev dependency)

All dependencies are listed in `requirements.txt` so anyone can recreate my environment.

## Testing

I wrote some tests to make sure everything works:
```bash
pytest testing/
```

## Notes

This was my first time really working with pip and external packages in a structured way. The hardest part was remembering to track all my dependencies in requirements.txt, but I get why it's important now - it makes the project way easier for others to run.