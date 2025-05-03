def file_modifier():
    filename = input("Enter the name of the file you want to read: ")

    try:
        # Opening and reading the input file
        with open(filename, "r") as file:
            content = file.read()

        # Modifying the content (capitalizing the content)
        new_content = content.capitalize()

        # Creating a new file name
        new_filename = f"modified_{filename}"

        # Writing the modified content to new file
        with open(new_filename, "w") as new_file:
            new_file.write(new_content)

        print(f"Success! Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Could not read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
file_modifier()
