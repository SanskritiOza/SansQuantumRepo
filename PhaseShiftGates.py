#!/usr/bin/env python
# coding: utf-8

# In[9]:


from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


circuit= QuantumCircuit(3)
circuit.h([0,1,2])
# circuit.s(1) #S-gate
# circuit.sdg(2) #S-dagger
circuit.t(1) #T-gate
circuit.tdg(2) #T-dagger
circuit.draw(output='mpl')


# In[11]:


simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend=simulator).result()
plot_bloch_multivector(result.get_statevector())

