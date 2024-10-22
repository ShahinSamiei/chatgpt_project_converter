<!---------------------------------------[Description]-->
## Description
    This project provides a set of Python scripts to work with directory structures and file contents. It allows you to save the structure of a directory tree, the contents of files, and also recreate a project from a text file representation. These tools are useful for documenting projects, backing up file structures, or rebuilding projects from textual representations.

<!---------------------------------------[Install]-->
<br><br>

## Source 
    git clone git@github.com:yourusername/yourproject.git
    cd ./yourproject

<!---------------------------------------[Python]-->
<br><br>

## Python

#### Install
    apt update -y
    apt install python3 -y
    apt install python3-pip -y
    apt install python3-venv -y

#### Virtual environment 
    python3 -m venv .venv
    .venv/bin/python3 -m pip install --upgrade pip
    source .venv/bin/activate
    pip install -r requirements.txt

<!---------------------------------------[Files]-->

<br><br>

## Files

### doc.py
    This script reads all files in a specified folder, retrieves their contents, and saves it into a single text file. It documents each file including its relative path and handles errors encountered during file reading.

### main.py
    This script saves both the directory structure and the contents of the files within a directory, combining both into a single output file.

### project.py
    This script recreates a project’s folder and file structure from a text file representation of the directory and its contents.

### tree.py
    This script focuses on saving the directory structure in a tree format, without file contents.

<!---------------------------------------[Usage]-->
<br><br>

## Usage

### Document a Project:
    python main.py
    # Input the folder path when prompted and save the structure and contents in one file.

### Recreate a Project:
    python project.py
    # Input the path to the saved text file and the directory where the project should be recreated.

### Save Only Directory Structure:
    python tree.py
    # Input the folder path and save the directory structure in a text file.

<!---------------------------------------[Structure]-->
<br><br>

## Structure
    doc.py
    main.py
    project.py
    tree.py
