"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file
if len(sys.argv) < 2: 
    try:
        file_path = sys.argv[1]
        if len(sys.argv) < 2: 
            command = sys.argv[2]
            if command == view:  
                tasks = read_todo_file(file_path)
                print("Tasks:")
                for task in tasks:
                    print(task)
            else:
                raise ValueError("Command not found!")
    except IndexError:
        print("Insufficient arguments provided!")