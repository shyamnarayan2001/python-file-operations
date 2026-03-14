# File Operations in Python with Exception Handling

import os

try:
    # Create a new file and write to it
    with open('example.txt', 'w') as f:
        f.write('Hello, World! This is a file operation example.\n')

    # Read from the file
    with open('example.txt', 'r') as f:
        content = f.read()
        print('Content of the file:')
        print(content)

    # List files in the current directory
    print('Files in the current directory:')
    print(os.listdir('.'))

    # Delete the file
    os.remove('example.txt')
    print('example.txt has been deleted.')

except FileNotFoundError:
    print('Error: The file was not found.')
except PermissionError:
    print('Error: Permission denied.')
except Exception as e:
    print(f'An unexpected error occurred: {e}')