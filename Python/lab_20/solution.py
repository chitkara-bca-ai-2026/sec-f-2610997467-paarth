import os

def write_notes(filename, content):
    with open(filename, "a") as file:
        file.write(content+"\n")
    print("Notes saved successfully.")

def read_notes(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read()
    return "No notes file exists yet."

filename = "notes.txt"
while True:
    print("\nStudent Notes Management System")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        content = input("Enter your notes: ")
        write_notes(filename, content)
    elif choice == "2":
        print(read_notes(filename))
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
