#!/usr/bin/env python
# coding: utf-8

# In[35]:


from qiskit import *
from qiskit.tools.visualization import plot_histogram, array_to_latex
get_ipython().run_line_magic('matplotlib', 'inline')


# In[36]:


# 2-Qubit Bell State
# circuit = QuantumCircuit(2)
# For different qubits
# circuit.x(1)
# circuit.h(0)
# circuit.cnot(0,1)
# 00 and 11 -For same qubits
# circuit.h(0)
# circuit.cnot(0,1)

# 3-Qubit Bell State
# circuit = QuantumCircuit(3)

# circuit.h(0)
# circuit.cnot(0,1)
# circuit.cnot(1,2)
# # circuit.cnot(0,2)

# 4-Qubit Bell State
# circuit = QuantumCircuit(4)

# circuit.h(0)
# circuit.cnot(0,1)
# circuit.cnot(1,2)
# circuit.cnot(0,3)

# circuit.draw(output='mpl')

# W-state ???????????????????????
 
# circuit = QuantumCircuit(3)
# circuit.x(1)
# circuit.h(0)
# circuit.cnot(0,1)
# circuit.cnot(1,2)


# In[37]:


simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend=simulator).result()
statevector= result.get_statevector()
array_to_latex(statevector, prefix = "\\text{statevector=}\n")


# In[38]:


circuit.measure_all()
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator).result()
plot_histogram(result.get_counts())

