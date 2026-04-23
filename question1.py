"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md
import sys
if len(sys.argv) != 3:
    print("Error: Invalid input! Enter numeric values only.")
    sys.exit()
try:
    total_load = float(sys.argv[1])
    num_supports = float(sys.argv[2])
    load_per_support = total_load / num_supports
    print(f"Load per support point: {load_per_support:.2f} N")
except ZeroDivisionError:
    print("Error: Cannot divide by zero! Supports must be greater than zero.")
except ValueError:
    print("Error: Invalid input! Enter numeric values only.")