from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram

def odd_to_even(n, numbers):
    # Calculate the number of qubits required
    k = n.bit_length()
    
    # Create a quantum circuit with k qubits
    qc = QuantumCircuit(k, k)
    
    # Apply Hadamard gates to all qubits
    qc.h(range(k))
    
    # Define the conditional gate to apply a phase shift to odd numbers
    for i in range(1, n, 2):
        mask = format(i, '0' + str(k) + 'b')  # Binary representation of odd numbers
        mask = mask[::-1]  # Qiskit's qubit ordering is reversed
        for j in range(k):
            if mask[j] == '1':
                qc.z(j)  # Apply a phase shift to the qubit if corresponding bit is 1
    
    # Measure qubits
    qc.measure(range(k), range(k))
    
    # Simulate the circuit
    simulator = Aer.get_backend('qasm_simulator')
    job = assemble(transpile(qc, simulator), shots=1)
    result = simulator.run(job).result()
    counts = result.get_counts(qc)
    
    # Post-process the measurement outcome to ensure numbers stay within the range [1, n)
    output = [int(k, 2) for k in counts.keys()]
    output = [x if x < n else x - n for x in output]
    
    return output

# Example usage
n = 31
numbers = [1,2,2,4,5,6,7,11,17,21,22,23]
result = odd_to_even(n, numbers)
print(result)
