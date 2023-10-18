#!/usr/bin/env python
# coding: utf-8

# In[42]:


from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, array_to_latex
from math import pi 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[43]:


# Pauli X-gate

# circuit = QuantumCircuit(1)
# circuit.ry(pi/4,0)
# circuit.x(0)
# # circuit.x(0)
# print(circuit)
# #circuit.draw(output='mpl')


# In[44]:


# Pauli Y-gate

# circuit = QuantumCircuit(1)
# circuit.y(0)
# circuit.draw(output='mpl')
# circuit = QuantumCircuit(2)
# circuit.ry(pi/4, [0,1])
# circuit.y(1)
# circuit.draw(output='mpl')


# In[45]:


# Pauli Z-gate

# circuit = QuantumCircuit(1)
# circuit.z(0)
# circuit.draw(output='mpl')
# circuit = QuantumCircuit(2)
# circuit.ry(pi/4, [0,1])
# circuit.z(1)
# circuit.draw(output='mpl')


# In[46]:


simulator= Aer.get_backend('statevector_simulator')
result= execute(circuit,backend=simulator).result()
statevector= result.get_statevector()
array_to_latex(statevector, prefix="\\text{statevector = }") #Display of statevector


# In[47]:


plot_bloch_multivector(statevector)

