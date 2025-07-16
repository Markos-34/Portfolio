# 📝 CLI To-Do List in Python

A beginner-to-intermediate **Command-Line To-Do List** app written in Python. This project lets users add, remove, and list tasks with due dates, sorted chronologically. It's a great example of working with loops, conditionals, dictionaries, and date handling using `datetime`.

---

## 📌 Features

- ✅ Add tasks with a due date (`dd/mm/yy` format)
- 🗑️ Remove tasks by name
- 📅 List all tasks sorted by due date
- 🔁 Simple menu system for user interaction
- 🔐 Input validation to ensure correct date formats

---

## 💻 How It Works

1. When you run the script, a menu appears.
2. You can:
   - Add a task by entering a name and due date
   - Remove a task by name
   - View the full list of tasks sorted by due date
   - Exit the app

---

## 🚀 Getting Started

### Requirements

- Python 3.x

### Running the App

1. Clone the repo or download the script:
    ```bash
    git clone https://github.com/yourusername/cli-todo-list.git
    cd cli-todo-list
    ```

2. Run the program:
    ```bash
    python todo.py
    ```

> Make sure your terminal supports standard input/output interaction.

---

## 📷 Example

```text
**********MENU**********

      1)Add Tasks
      2)Remove Tasks
      3)List Tasks
      4)Exit

Please enter name for a Task: Clean Room
Please enter a date for your Task (dd/mm/yy): 20/07/25

**********MENU**********

      1)Add Tasks
      2)Remove Tasks
      3)List Tasks
      4)Exit

Clean Room: 20/07/25
