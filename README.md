
# File Modifier Program 📝

This is a simple Python script that:
- Prompts the user for a filename.
- Reads the contents of the specified file.
- Converts all text to uppercase.
- Writes the modified content to a new file.
- Handles errors like missing files or read/write issues.

## 🚀 How It Works

1. The user is prompted to enter the name of the input file.
2. The script reads the content of the file.
3. It converts the entire content to **uppercase**.
4. A new file named `new_modified` is created.
5. The uppercase content is written to the new file.
6. A success message is printed.

Example:

Enter the name of the file to read: my_file.txt  
Success! Modified content written to 'new_modified.txt'.


## 🛡️ Error Handling

- If the file doesn't exist, the script prints:  
  Error: File not found.
- If the file can't be read, it prints:  
  Error: Could not read the file.
- Other unexpected errors are also caught and printed.

## 🐍 Requirements

- Python 3.6 or higher

No external libraries are required.

## 📂 Example Files

If my-file.txt contains:

Python is powerful.
This is a sample file.

Then new_modified.txt will contain:

Python Is Powerful.
This Is A Simple File.


## 👨‍💻 Author

**Yvonnah Shiala**

