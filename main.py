"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file
if len(sys.argv) >= 2:
    try:
        nombrescript = sys.argv[0]
        rutaarchivo = sys.argv[1]
        print("{[sys.argv]}")
    except IndexError:
        print("Insufficient arguments provided!")