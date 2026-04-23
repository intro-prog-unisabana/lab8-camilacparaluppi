"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md
import sys
if len(sys.argv) != 4:
    print("Error: Invalid input! Enter numeric values only.")
    sys.exit()
total_load = sys.argv[1]
num_supports = sys.argv[2]
try:
    load_per_support = total_load / num_supports
except ZeroDivisionError:
    print("Cannot divide by zero! Supports must be greater than zero.")
print(f"Load per support point: {load_per_support} N")