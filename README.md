# Time Calculator

A Python project to calculate the resulting time after adding a duration to a start time, with an optional day of the week.

## Overview

This project implements the `add_time` function, which takes a start time in 12-hour format (e.g., "3:30 PM"), a duration (e.g., "2:12"), and an optional day of the week (e.g., "Monday"). It calculates the resulting time, handles AM/PM transitions, tracks day rollovers, and formats the output with proper spacing and punctuation.

## Features

- Supports 12-hour clock format with AM/PM.
- Adds duration (hours and minutes) to a start time.
- Handles optional case-insensitive day of the week.
- Indicates day rollovers with "(next day)" or "(n days later)".
- Formats output precisely (e.g., "6:10 PM", "12:03 AM, Thursday (2 days later)").
- No external Python libraries required.
- Handles edge cases like zero duration, midnight transitions, and large durations.

## Installation

1. Ensure Python 3.x is installed.
2. Download or clone this repository:
   ```bash
   git clone https://github.com/thesoulseizure/time-calculator.git
   ```
3. Navigate to the project directory:
   ```bash
   cd time-calculator
   ```

## Usage

1. Save `time_calculator.py` in your project directory.
2. Import and use the `add_time` function in a Python script or interpreter.

Example usage:

```python
# Basic time addition
print(add_time("3:30 PM", "2:12"))
# Output: 5:42 PM

# With day of the week
print(add_time("11:30 AM", "2:32", "Monday"))
# Output: 2:02 PM, Monday

# Next day
print(add_time("10:10 PM", "3:30"))
# Output: 1:40 AM (next day)

# Multiple days with day of the week
print(add_time("11:43 PM", "24:20", "tueSday"))
# Output: 12:03 AM, Thursday (2 days later)

# Large duration
print(add_time("6:30 PM", "205:12"))
# Output: 7:42 AM (9 days later)
```

## File Structure

- `time_calculator.py`: Main Python script containing the `add_time` function.
- `README.md`: This documentation file.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
