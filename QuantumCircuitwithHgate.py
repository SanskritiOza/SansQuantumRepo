#!/usr/bin/env python
# coding: utf-8

# In[35]:


from qiskit import *
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
get_ipython().run_line_magic('matplotlib', 'inline')


# In[36]:


circuit = QuantumCircuit(2) #Initialize circuit of 2 qubits
circuit.h(0)
circuit.measure_all()


# In[37]:


simulator= Aer.get_backend('qasm_simulator')
result= execute(circuit,backend=simulator).result()
counts= result.get_counts()


# In[38]:


plot_histogram(counts)


# In[33]:


# simulator= Aer.get_backend('statevector_simulator')
# result= execute(circuit,backend=simulator).result()
# statevector= result.get_statevector()
# array_to_latex(statevector) #Display of statevector


# In[34]:


# plot_bloch_multivector(statevector) #statevector on Bloch Sphere for two qubits

