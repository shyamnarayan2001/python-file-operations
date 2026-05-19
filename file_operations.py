# file_operations.py

# Function to create a file and write content

def create_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f'File created: {file_path}')
    except IOError as e:
        print(f'Error creating file: {e}')

# Function to read content from a file

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print('File content:')
        print(content)
    except IOError as e:
        print(f'Error reading file: {e}')

# Function to append content to a file

def append_to_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
        print(f'Content appended to file: {file_path}')
    except IOError as e:
        print(f'Error appending to file: {e}')

# Function to delete a file

def delete_file(file_path):
    try:
        import os
        os.remove(file_path)
        print(f'File deleted: {file_path}')
    except IOError as e:
        print(f'Error deleting file: {e}')
    except FileNotFoundError:
        print(f'File not found: {file_path}')

# Main function to execute the file operations

def main():
    file_path = 'C:\temp\file_operations.py'
    create_file(file_path, 'Initial content.\n')
    read_file(file_path)
    append_to_file(file_path, 'Appended content.\n')
    read_file(file_path)
    delete_file(file_path)

if __name__ == '__main__':
    main()