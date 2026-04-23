"""Laboratorio 8 - Módulo de persistencia para lista de tareas."""


def read_todo_file(file_path):
    """Reads tasks from a file. Returns a list of tasks."""
    # TODO: Implementar manejo de FileNotFoundError según README.md
file_path = []
    try:
        with open(file_path, 'r') as file:
    except FileNotFoundError:
        print(f"File {file_path} not found! Returning an empty to-do list.")
return file_path


def write_todo_file(file_path, tasks):
    """Writes tasks to a file, one per line."""
    # TODO: Implementar escritura de tareas según README.md
    raise NotImplementedError
