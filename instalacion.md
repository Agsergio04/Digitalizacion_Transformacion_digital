

## Archivo: instalacion.md

```markdown
# Installation Guide

This guide explains how to install and run the Calendar and Task Scheduler App on different operating systems.

## Prerequisites
- **Python 3.6+** must be installed on your system.
- Basic knowledge of using a terminal or command prompt.

---

## Installation on Windows

1. **Download and Install Python:**
   - Go to [Python.org](https://www.python.org/downloads/windows/) and download the latest Python installer.
   - Run the installer and ensure that you select the option "Add Python to PATH".

2. **Clone or Download the Repository:**
   - Open Command Prompt.
   - Clone the repository:
     ```bash
     git clone https://github.com/Agsergio04/Digitalizacion_Transformacion_digital.git
     cd calendar-task-scheduler
     ```
     *Or* download the ZIP file and extract it.

3. **Install Dependencies:**
   - Run the following command in the Command Prompt:
     ```bash
     pip install -r requerimientos.txt
     ```

4. **Run the Application:**
   - In the Command Prompt, execute:
     ```bash
     python app.py
     ```
   - Follow the on-screen instructions in the CLI.

---

## Installation on macOS

1. **Install Python:**
   - macOS typically includes Python; however, you might want to install the latest version using [Homebrew](https://brew.sh/):
     ```bash
     brew install python
     ```

2. **Clone or Download the Repository:**
   - Open Terminal.
   - Clone the repository:
     ```bash
     git clone https://github.com/Agsergio04/Digitalizacion_Transformacion_digital.git
     cd calendar-task-scheduler
     ```
     *Or* download and unzip the repository.

3. **Install Dependencies:**
   - Run the following command in Terminal:
     ```bash
     pip3 install -r requerimientos.txt
     ```

4. **Run the Application:**
   - In Terminal, execute:
     ```bash
     python3 app.py
     ```
   - Follow the on-screen prompts.

---

## Installation on Linux

1. **Install Python:**
   - Most Linux distributions come with Python pre-installed. To install the latest version, use your package manager.
     For example, on Ubuntu:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

2. **Clone or Download the Repository:**
   - Open your terminal.
   - Clone the repository:
     ```bash
     git clone https://github.com/Agsergio04/Digitalizacion_Transformacion_digital.git
     cd calendar-task-scheduler
     ```
     *Or* download the ZIP file and extract it.

3. **Install Dependencies:**
   - Run the following command:
     ```bash
     pip3 install -r requerimientos.txt
     ```

4. **Run the Application:**
   - In the terminal, execute:
     ```bash
     python3 app.py
     ```
   - Follow the application prompts to use the CLI.

---

This guide covers the basics of installing and running the application on the three main platforms. The project is designed to be cross-platform, and future releases may include additional installation scripts or packages.
