from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_histogram
import numpy as np

def odd_to_following_even(num):
    # If the number is odd, increment by 1 to make it even
    if num % 2 != 0:
        num += 1
    return num

# Example usage
odd_numbers = [1,1, 3, 5, 7, 9, 10]  # List of odd numbers
even_numbers = [odd_to_following_even(odd) if odd % 2 != 0 else odd for odd in odd_numbers]  # Convert odd to the following even number, keep even numbers as they are

print("Odd numbers:", odd_numbers)
print("Following even numbers:", even_numbers)

