#!/usr/bin/env python3
"""
Calendar and Task Scheduler App (CLI Version)
-----------------------------------------------
A command-line application for managing tasks and calendars.

Usage:
    Run the application using:
        python app.py
"""

import sys
import datetime
import json
import os

# Storage file for tasks (for demonstration purposes, using JSON file for persistence)
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Add a new task."""
    title = input("Enter task title: ").strip()
    if title == "":
        print("Task title cannot be empty.")
        return
    description = input("Enter task description: ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    task = {
        "title": title,
        "description": description,
        "due_date": due_date_str,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def view_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx}. {task['title']} - Due: {task['due_date']} - {status}")
        print(f"   Description: {task['description']}")
        print("-" * 40)

def mark_task_completed(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if task_num < 1 or task_num > len(tasks):
            print("Invalid task number.")
            return
        tasks[task_num - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nCalendar and Task Scheduler App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            print("Exiting application.")
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
