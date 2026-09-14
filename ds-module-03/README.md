# Introduction to Python: Object-Oriented Programming Skills

> This project aims to teach you the basics of object-oriented programming in Python.
> The tasks are designed in a sequential manner. From creating a simple class to implementing logging and integrating with external services.

| Exercise | What it is about | Description |
|---|---------|-------------|
| 00 | Simple classes | Create a class Must_read that reads and displays the contents of the data.csv file.<br> Objective: first introduction to classes. |
| 01 | Class methods | Move the file reading logic to the file_reader() method of the Research class.<br> Objective: understand the difference between a class and a method. |
| 02 | Constructor | Add the constructor _init_() that accepts the file path. Implement the file structure validation.<br>Objective: Learn to use constructors and handle errors. |
| 03 | Nested Classes | Add a nested class Calculations with counts() and fractions() methods.<br> Objective: Structure code using nested classes. |
| 04 | Inheritance | Create Analytics class inherited from Calculations. Add predict_random() and predict_last() methods.<br> Objective: Master inheritance and extending functionality. |
| 05 | Decomposition | Divide the code into three files: <ul><li>config.py: parameters and report template</li><li>analytics.py: main logic</li><li>make_report.py: entry point that generates a text report</li></ul>Objective: learn about modular project organization and configuration. |
| 06 | Logging | Add logging of all methods to the analytics.log file. Implement sending a notification to Telegram.<br>Objective: master logging and integration with external APIs. |

## Running

```bash
# For ex02–06
python3 first_constructor.py data.csv

# For ex05–06
python3 make_report.py data.csv