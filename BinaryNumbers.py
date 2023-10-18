#!/usr/bin/env python
# coding: utf-8

# In[13]:


from qiskit import *
from qiskit.tools.visualization import plot_state_qsphere
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


circuit = QuantumCircuit(4)
circuit.x([0,2,3])
circuit.draw(output='mpl')


# In[15]:


simulator= Aer.get_backend('statevector_simulator')
statevector= execute(circuit, backend=simulator).result().get_statevector()
plot_state_qsphere(statevector) #Display of statevector

