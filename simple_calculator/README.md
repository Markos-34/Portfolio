# Simple Python Calculator 🧮

This is a basic command-line calculator built in Python. It allows users to perform simple arithmetic operations by choosing from a menu.

## 🚀 Features

- Addition
- Subtraction
- Multiplication
- Division (with zero division handling)
- Power
- Exit option to end the program

## 🛠️ How It Works

1. The user is presented with a menu of options.
2. The user selects a number from 1 to 6.
3. If an operation (1-5) is selected:
   - The program prompts for two numbers.
   - It performs the chosen calculation and displays the result.
4. If `6` is selected, the program exits.
5. If division by zero is attempted, the program shows a warning instead of crashing.

## 📂 File

- `calculator.py`: The main script file containing the code.

## ▶️ Run It

Make sure you have Python installed. Then run the script in your terminal:

```bash
python calculator.py

🧠 Concepts Used

    while loops

    if/elif/else conditions

    input() handling

    Basic error prevention (e.g., divide by zero)

    Casting strings to integers with int()

✅ Example Output

**********MENU**********

  1)Addition
  2)Substraction
  3)Multiplication
  4)Division
  5)Power
  6)Exit

Please enter the first number: 10
Please enter the second number: 5
Result: 15

