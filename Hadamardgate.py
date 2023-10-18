#!/usr/bin/env python
# coding: utf-8

# In[73]:


from qiskit import *
from qiskit.tools.visualization import plot_histogram, array_to_latex, plot_bloch_multivector
from math import pi
get_ipython().run_line_magic('matplotlib', 'inline')


# In[74]:


circuit= QuantumCircuit(1,1)
# circuit.x(0) #Pauli-X gate
# circuit.h(0) #Hadamard Gate
circuit.h(0) #Hadamard Gate
circuit.draw(output='mpl')


# In[75]:


simulator= Aer.get_backend('statevector_simulator')
result= execute(circuit,backend=simulator).result()
statevector= result.get_statevector()
array_to_latex(statevector, prefix="\\text{statevector = }") #Display of statevector


# In[76]:


plot_bloch_multivector(statevector)


# In[77]:


circuit.measure(0,0)
circuit.draw(output='mpl')


# In[78]:


simulator= Aer.get_backend('qasm_simulator')
result= execute(circuit,backend=simulator,shots=1024).result() #simulating shots
plot_histogram(result.get_counts())

