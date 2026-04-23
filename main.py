"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file
if len(sys.argv) < 2:
    print("Insufficient arguments provided!")
else:
    try:
        rutaarchivo = sys.argv[1]
        print("Command-line arguments:")
        for arg in sys.argv[1:]: 
            print(arg)
        tasks = read_todo_file(rutaarchivo)
        print("Tasks:")
        for task in tasks:
            print(task)
    except IndexError:
        print('Insufficient arguments provided!')