# 📚 Personal Book Manager
![Static Badge](https://img.shields.io/badge/python-3.13-blue)

A simple Python application to manage your personal book collection.




# Features

- ➕ Add new books
- 📖 View your book collection
- 💾 Save books in a JSON file
- 📂 Load previously saved books
- 🔐 Password-protected Admin Mode




#  File Description
|File | Descriptin|
| --- | --- |
| `main.py` | main file used to run book manager
| `books.py` | اandles displaying, saving, and loading books using JSON
| `.gitignore` | tells git switch files and folders shold not be tracked
| `.env.example` | shows the envoirment variables needed by the project
| `requirements.txt` | lists the external libraries required to run the project
| `images/` | stores project screenshots
| `gifs` | stores project gifs


#  Requirements

- Python
- Python-dotenv

# Installation

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

# Environment Setup

Create a `.env` file in the project folder.

Use `.env.example` as a template and add your admin password:

```env
BOOK_MANAGER_ADMIN_PASSWORD=your_password_here
```

Replace `your_password_here` with your own admin password.

# Run the Program

Run the main file:

```bash
python main.py
```

# How It Work
1. open a terminal in the project folder
2. run the `main.py`
3. enter your name
4. Admin mode :
   1. if you awnser was `no`, move on the next
   2. if you awnser was `yes`, enter the password

5. enter the number of books and write down their names
6. the terminal shows list of books and save them



# Screenshot

![personal_book_manager](images\p1.jpg)

# Demo

![personal_book_manager](gifs\g1.gif)


# Troubleshooting
1. **FileNotFoundError**

- Meaning : the program cannot finde a required file
- Because : the file may be missing or in the wrong directory
- Check : make sure the file exist in the project folder

2. **JSONDecodeError**

- Meaning : the program cannot read the JSON file
- Because : the `books.json` file may be empty or contain invalid JSON
- Check : open `books.json` and check its content


3. **ModuleNotFoundError (python-dotenv)**
  
- Meaning : python cannot find the required madule
- Because : the `python-dotenv` package may not be installed
- Check : make sure you installed the required packages using `requirements.txt`


4. **Password not Found**
- Meaning : the program cannot read the admin password
- Because : the `.env` file may be missing or the variable name may be incorrect
- Check : check the `.env` file and make sure the password variable is correct


---

<p align="center">
  Made with 🐍 Python
</p>


