# Multiplication Table Generator 🧮

This is a simple & interactive Python program that generates the multiplication table of any number entered by the user. It uses a simple `while` loop, `input()` to keep the script interactive, it also accepts decimal numbers like '1.5' along with whole numbers.

---

## 🚀 How It Works

1. Asks the user for a number.
2. Prevent crashes from invalid input
3. Accepts both decimals and whole number
4. Keeps running until the user says "No".

---

## 💻 Sample Output

Which Number's table do you want? :  7
7 × 1 = 7
7 × 2 = 14
7 × 3 = 21
......
7 × 10 = 70
Want any other number's table? [YES/NO]: yes

---

## 📚 Concepts Used

- `while True`: For infinite loops to keep the program running until user exits
- `float(input())`: Accepts both integers and decimals as input
- `for i in range(1, 11)`: Loops through numbers 1 to 10 to generate the table
- `if`, `elif`, `else`: Controls flow based on user input like YES/NO
- `.upper()`: Handles lowercase inputs like "yes" or "no" by converting to uppercase
- `f"{num:g}"`: Formats numbers to hide unnecessary `.0` in whole numbers (e.g. `7.0 → 7`)
- `exit()`: Stops the program when the user chooses not to continue

---

## 📌 Requirements

- Python 3.x
- No external libraries required

---

## ✅ To Run the Script

python table_generator.py

## 🧠 Good For

Practicing basic Python syntax

Understanding loops and conditionals

Beginner Python projects

## ✍️ Author

Made by Mohammed Danish Khan

Edited from GitHub website for git pull demo

This line was added from local system.
