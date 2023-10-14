#!/usr/bin/env python
# coding: utf-8

# In[9]:


from qiskit import *
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


qr= QuantumRegister(1) #one qubit
cr= ClassicalRegister(1) #one bit
circuit= QuantumCircuit(qr,cr) #quantum circuit initialization
circuit.measure(qr,cr) #measuring qubit and storing it in classical bit


# In[11]:


simulator= Aer.get_backend('qasm_simulator')
result= execute(circuit,backend=simulator,shots=1024).result() #simulating shots
plot_histogram(result.get_counts()) 


# In[12]:


simulator2= Aer.get_backend('statevector_simulator')
result2= execute(circuit,backend=simulator2).result()
statevector= result2.get_statevector()
array_to_latex(statevector) #Display of statevector


# In[13]:


plot_bloch_multivector(statevector) #statevector on Bloch Sphere for 1 qubit

