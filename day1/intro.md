# Git & GitHub Shortcuts

![png-clipart-computer-icons-pro-git-github-logo-text-logo](./images/png-clipart-computer-icons-pro-git-github-logo-text-logo.png)







![png-clipart-black-cat-github-logo-repository-computer-icons-github-white-cat-like-mammal](./images/png-clipart-black-cat-github-logo-repository-computer-icons-github-white-cat-like-mammal.png)





### (Work Faster with Version Control)

---

### Repository & Setup Shortcuts

- `git init` - Initialize new repository
- `git clone <url>` - Clone a repository
- `git status` - Check status of files
- `git config --global user.name "Name"` - Set global username
- `git config --global user.email "email"` - Set global email

### Basic Workflow Shortcuts

- `git add .` - Add all changes
- `git add <file>` - Add specific file
- `git commit -m "message"` - Commit changes
- `git commit -am "message"` - Add and commit (tracked files)
- `git push` - Push changes to remote
- `git pull` - Pull latest changes

### Branching Shortcuts

- `git branch` - List all branches
- `git branch <name>` - Create a new branch
- `git checkout <name>` - Switch to a branch
- `git checkout -b <name>` - Create and switch to new branch
- `git merge <branch>` - Merge a branch
- `git branch -d <name>` - Delete a branch

### Undo & Restore Shortcuts

- `git restore <file>` - Discard changes in a file
- `git restore .` - Discard all changes
- `git reset <file>` - Unstage a file
- `git reset --hard` - Reset everything (⚠ be careful)
- `git revert <commit>` - Undo a commit (safe)
- `git clean -fd` - Remove untracked files & folders

### Stash Shortcuts

- `git stash` - Stash current changes
- `git stash list` - View stashes
- `git stash apply` - Apply latest stash
- `git stash pop` - Apply and remove latest stash
- `git stash drop` - Delete a stash

### Remote Repository Shortcuts (GitHub)

- `git remote -v` - View remote URLs
- `git remote add origin <url>` - Add remote repository
- `git push -u origin <branch>` - Push and set upstream
- `git fetch` - Fetch latest changes
- `git pull origin <branch>` - Pull from specific branch
- `git push origin --delete <branch>` - Delete remote branch

### Useful Shortcuts

- `git log --oneline` - View commit history (short)
- `git log --graph` - View commit history (graph)
- `git diff` - Show changes
- `git show <commit>` - Show commit details
- `git blame <file>` - See who changed a line
- `git bisect` - Find the commit that introduced a bug

---

### 

# Windows Command Line Shortcuts

![png-transparent-cmd-exe-command-line-interface-computer-icons-user-interface-console-miscellaneous-text-commandline-interface](./images/png-transparent-cmd-exe-command-line-interface-computer-icons-user-interface-console-miscellaneous-text-commandline-interface.png)



### (Navigate, Manage, and Automate Faster)

---

### Navigation & Directory Shortcuts

- `cd <path>` - Change directory (e.g., `cd Documents`)
- `cd ..` - Go up one directory level
- `cd \` - Go to the root of the current drive
- `dir` - List files and folders in current directory
- `tree` - Display folder structure graphically
- `cls` - Clear the command prompt screen
- `exit` - Close the Command Prompt

### File & Folder Management

- `mkdir <name>` - Create a new directory (or `md`)
- `rmdir <name>` - Remove an empty directory (or `rd`)
- `rmdir /s <name>` - Remove directory and all contents (⚠ careful)
- `copy <source> <dest>` - Copy files
- `xcopy <source> <dest> /e` - Copy folders and subfolders
- `move <source> <dest>` - Move or rename files/folders
- `del <file>` - Delete a file
- `ren <old> <new>` - Rename a file or folder

### System Information & Networking

- `ipconfig` - View network IP configuration
- `ipconfig /flushdns` - Clear DNS resolver cache
- `ping <host>` - Test network connection (e.g., `ping google.com`)
- `tracert <host>` - Trace route to a network host
- `netstat -an` - View active network connections
- `systeminfo` - View detailed system configuration
- `tasklist` - List all currently running processes
- `taskkill /im <name>.exe /f` - Force kill a running process

### System Maintenance & Utilities

- `sfc /scannow` - Scan and repair system files (Run as Admin)
- `chkdsk` - Check disk for errors
- `diskpart` - Disk partitioning utility
- `shutdown /s /t 0` - Shut down immediately
- `shutdown /r /t 0` - Restart immediately
- `powercfg /batteryreport` - Generate a battery usage report

### Advanced & Useful Shortcuts

- `|` (Pipe) - Send output of one command to another (e.g., `dir | find "txt"`)
- `>` - Redirect output to a file (e.g., `ipconfig > network.txt`)
- `&&` - Run second command if first succeeds
- `help <command>` - Get help for a specific command
- `color` - Change text and background color of the prompt
- `title <text>` - Change the title of the command prompt window

---

### 

# Python: Basic Introduction

![ec51b026341cc2bdf0d7170a36da010f](./images/ec51b026341cc2bdf0d7170a36da010f.png)





It is easy to learn and use. Python is used by various industries. It has been used to develop web apps, desktop apps, system administrations, and machine learning libraries. In Data Science, it is also very recommended.

## Basic Python

```python
# comment python
```

`img`

```python
"""
This is
multi line Comment
"""
```

`img`

## Data Types

In Python we have different data types. I divided them into smaller groups for better comprehension. They will be covered heavily in the next section.

- **Numbers**
   - **Integers:** Whole numbers ex: `1, 2, 3, 4, 5, -1, 0`. Aka `int` (in py)
   - **Float:** Decimal numbers: `1.1, 3.7` ...
   - **Complex:** Number with Real and imaginary parts. The imaginary part uses `j` instead of `i` like in maths.
- **Strings**
   - A collection of one or more characters under a single `'` or double `"` quote. Ex: `'Yvan'`, `'Ted'`, `'JustCode'`
- **Booleans**
   - A boolean data type is either a `True` or `False`.
- **List**
   - It is an ordered collection which allows to store different data type items.
   - `[0, 1, 2, 3, 4, 5]` - list of integers
   - `['Yvan', 'Ted', 'Just code']` - list of strings (Names)
   - `['Orange', 12, False, 3.14]` - list of different datatypes
- **Dictionary**
   - A Python dictionary object is an ordered collection of data in a key-value pair format.
   - Example:
```python
        {
            "First name": "Morant", 
            "last name": "Ja", 
            "jersey number": 1, 
            "Team": "Portland", 
            "Conference": "East", 
            "skills": ["dunk", "high jump", "dribble"]
        }
```

- **Tuple**
   - It is an ordered collection of different data types like list, but tuples can't be modified once they are created.
   - Example: `('Jo Moanl', 'Lamelo Ball', 'Anthony Edwards', 'Giannis Antetokounmpo', 'Jokic')`
- **Set**
   - A set is a collection of data types similar to list and tuple. While list and tuple are ordered, a set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items. Imagine throwing everything in a bag without caring about how it is placed.
   - `{1, 4, 3, 5, 10, 8, 6, 7}` (the order doesn't matter)

## Operations

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `**` Exponential
- `%` Remainder
- `//` Floor division

**Check data type:**

```python
print(type(10))
```





