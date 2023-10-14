#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import *
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


qr= QuantumRegister(2) #two qubits
cr= ClassicalRegister(2) #two bits
circuit= QuantumCircuit(qr,cr) #quantum circuit initialization
circuit.measure(qr,cr) #measuring qubits and storing it in classical bit


# In[3]:


simulator= Aer.get_backend('statevector_simulator')
result= execute(circuit,backend=simulator).result()
statevector= result.get_statevector()
array_to_latex(statevector) #Display of statevector


# In[4]:


plot_bloch_multivector(statevector) #statevector on Bloch Sphere for two qubits


# In[ ]:




