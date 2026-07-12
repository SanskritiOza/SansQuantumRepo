"""
Shor's Algorithm Implementation using Qiskit

Shor's algorithm is a quantum algorithm for integer factorization that runs in 
polynomial time. It finds prime factors of large integers, which has significant 
implications for cryptography.

This implementation demonstrates the key components of Shor's algorithm:
1. Classical order-finding
2. Quantum phase estimation
3. Classical post-processing
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile, execute
from qiskit_aer import AerSimulator
import numpy as np
from math import gcd, log2, ceil
from fractions import Fraction


def classical_gcd(a, b):
    """
    Compute the greatest common divisor of a and b.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: GCD of a and b
    """
    while b:
        a, b = b, a % b
    return a


def find_order_classical(a, n):
    """
    Find the order r such that a^r mod n = 1.
    This is the classical part of Shor's algorithm.
    
    Args:
        a (int): The base
        n (int): The modulus
    
    Returns:
        int: The order r, or None if not found
    """
    if gcd(a, n) != 1:
        return None
    
    x = 1
    for r in range(1, n):
        x = (x * a) % n
        if x == 1:
            return r
    return None


def shors_algorithm_classical(N, max_attempts=10):
    """
    Classical implementation of Shor's algorithm with order-finding.
    This demonstrates the overall structure of Shor's algorithm.
    
    Args:
        N (int): The number to factorize
        max_attempts (int): Maximum number of attempts to find factors
    
    Returns:
        tuple: (factor1, factor2) if factorization is found, else None
    """
    # Check if N is even
    if N % 2 == 0:
        return (2, N // 2)
    
    # Check if N is a perfect power
    for k in range(2, int(log2(N)) + 1):
        a = int(N ** (1 / k))
        if a ** k == N:
            return (a, N // a)
    
    # Attempt to find factors using random bases
    for attempt in range(max_attempts):
        # Pick random a in range [2, N-1]
        a = np.random.randint(2, N)
        
        # Check if gcd(a, N) > 1
        factor = gcd(a, N)
        if factor != 1 and factor != N:
            return (factor, N // factor)
        
        # Find order r such that a^r mod N = 1
        r = find_order_classical(a, N)
        
        if r is None or r % 2 != 0:
            continue
        
        # Compute x = a^(r/2) mod N
        x = pow(a, r // 2, N)
        
        # Check if x != -1 mod N
        if x != N - 1:
            # Compute potential factors
            factor1 = gcd(x + 1, N)
            factor2 = gcd(x - 1, N)
            
            if factor1 != 1 and factor1 != N:
                return (factor1, N // factor1)
            if factor2 != 1 and factor2 != N:
                return (factor2, N // factor2)
    
    return None


def create_qpe_circuit(n_counting_qubits, n_target_qubits):
    """
    Create a simplified Quantum Phase Estimation (QPE) circuit.
    In a real implementation, this would perform phase estimation for order-finding.
    
    Args:
        n_counting_qubits (int): Number of qubits for phase estimation
        n_target_qubits (int): Number of target qubits
    
    Returns:
        QuantumCircuit: The QPE circuit
    """
    qc = QuantumCircuit(n_counting_qubits + n_target_qubits, n_counting_qubits)
    
    # Create superposition in counting qubits
    for i in range(n_counting_qubits):
        qc.h(i)
    
    # Initialize target qubits to |1⟩ state
    for i in range(n_counting_qubits, n_counting_qubits + n_target_qubits):
        qc.x(i)
    
    # Apply controlled unitary operations (simplified version)
    for i in range(n_counting_qubits):
        control_qubit = i
        target_qubit = n_counting_qubits
        
        # Apply controlled operations (example with single target)
        if i < n_counting_qubits - 1:
            qc.cp(2 * np.pi / (2 ** (n_counting_qubits - i)), control_qubit, target_qubit)
    
    # Apply inverse quantum Fourier transform
    apply_inverse_qft(qc, n_counting_qubits)
    
    # Measure counting qubits
    for i in range(n_counting_qubits):
        qc.measure(i, i)
    
    return qc


def apply_inverse_qft(qc, n_qubits):
    """
    Apply the inverse Quantum Fourier Transform.
    
    Args:
        qc (QuantumCircuit): The quantum circuit
        n_qubits (int): Number of qubits to apply QFT on
    """
    for j in range(n_qubits // 2):
        qc.swap(j, n_qubits - j - 1)
    
    for j in range(n_qubits):
        for k in range(j):
            qc.cp(-2 * np.pi / (2 ** (j - k)), k, j)
        qc.h(j)


def extract_order_from_phase(phase, denominator_limit=1000):
    """
    Extract the order from the measured phase using continued fractions.
    
    Args:
        phase (float): The measured phase
        denominator_limit (int): Maximum denominator for continued fraction
    
    Returns:
        int: The estimated order
    """
    frac = Fraction(phase).limit_denominator(denominator_limit)
    return frac.denominator


def demonstrate_shors_algorithm(N):
    """
    Demonstrate Shor's algorithm for factorizing a number.
    
    Args:
        N (int): The number to factorize
    
    Returns:
        dict: Results of the factorization attempt
    """
    print(f"\n{'='*60}")
    print(f"Shor's Algorithm - Factorizing {N}")
    print(f"{'='*60}\n")
    
    results = {
        'number': N,
        'factors': None,
        'method': None,
        'success': False
    }
    
    # Check trivial cases
    if N % 2 == 0:
        factor = 2
        results['factors'] = (factor, N // factor)
        results['method'] = 'Even number detection'
        results['success'] = True
        print(f"✓ N = {N} is even")
        print(f"  Factors: {factor} × {N // factor}")
        return results
    
    # Check for perfect powers
    for k in range(2, int(log2(N)) + 1):
        a = int(N ** (1 / k))
        if a ** k == N:
            results['factors'] = (a, N // a)
            results['method'] = f'Perfect {k}-th power'
            results['success'] = True
            print(f"✓ N = {N} is a perfect {k}-th power")
            print(f"  Factors: {a} × {N // a}")
            return results
    
    # Run classical Shor's algorithm
    print(f"Running classical Shor's algorithm with order-finding...")
    factors = shors_algorithm_classical(N, max_attempts=20)
    
    if factors and factors[0] != 1 and factors[1] != 1:
        results['factors'] = factors
        results['method'] = 'Order-finding with gcd'
        results['success'] = True
        print(f"✓ Factorization successful!")
        print(f"  Factors: {factors[0]} × {factors[1]}")
    else:
        print(f"✗ Factorization failed (would require full quantum implementation)")
        print(f"  For larger numbers, quantum phase estimation is needed")
    
    return results


def main():
    """
    Main demonstration of Shor's algorithm
    """
    print("\n" + "="*60)
    print("SHOR'S ALGORITHM - QUANTUM INTEGER FACTORIZATION")
    print("="*60)
    
    print("\nShor's Algorithm Overview:")
    print("-" * 60)
    print("• Polynomial-time quantum algorithm for integer factorization")
    print("• Classical runtime: O(log N) steps")
    print("• Quantum order-finding: O(log³ N) gates")
    print("• Breaks RSA encryption (currently infeasible with classical computers)")
    print("• Key insight: Factoring reduces to period-finding problem")
    
    # Test cases
    test_numbers = [15, 21, 35, 91]
    
    print("\n" + "="*60)
    print("DEMONSTRATION")
    print("="*60)
    
    all_results = []
    for N in test_numbers:
        result = demonstrate_shors_algorithm(N)
        all_results.append(result)
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"\nSuccessful factorizations: {sum(1 for r in all_results if r['success'])}/{len(all_results)}")
    
    for result in all_results:
        if result['success']:
            factors = result['factors']
            print(f"• {result['number']} = {factors[0]} × {factors[1]} ({result['method']})")
    
    print("\n" + "="*60)
    print("NOTES ON FULL QUANTUM IMPLEMENTATION")
    print("="*60)
    print("""
This implementation demonstrates the classical components and structure
of Shor's algorithm. For the full quantum version, you would need:

1. Quantum Phase Estimation (QPE):
   - Superposition of counting qubits
   - Controlled modular exponentiation
   - Inverse QFT for phase measurement

2. Modular Exponentiation Circuit:
   - Most resource-intensive part
   - O(log³ N) gates for N-bit number
   - Requires quantum adders and multipliers

3. Post-processing:
   - Extract order from measured phase using continued fractions
   - Use classical gcd to find factors

The quantum advantage comes from superposition and interference in QPE,
allowing parallel evaluation of the periodic function.
    """)


if __name__ == "__main__":
    main()
