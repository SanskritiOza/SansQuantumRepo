#!/usr/bin/env python
# coding: utf-8

# In[57]:


from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector
from math import pi
get_ipython().run_line_magic('matplotlib', 'inline')


# In[58]:


# # Controlled-NOT GATE
# circuit = QuantumCircuit(3)
# circuit.x(0)
# # circuit.cnot(0,1)
# circuit.cx(1,2)
# circuit.cnot(0,1)

# circuit.draw(output='mpl')


# In[59]:


# # Toffoli GATE
# circuit = QuantumCircuit(3)
# circuit.x(0)
# circuit.x(1)
# circuit.rx(pi/3,2)
# circuit.toffoli(0,1,2)
# # circuit.ccx(0,1,2)
# circuit.draw(output='mpl')


# In[60]:


# # Swap and Fredkin Gates
# circuit = QuantumCircuit(3)
# circuit.x(0)
# circuit.h(1)
# circuit.rx(-pi/4,2)
# # circuit.swap(1,2)
# circuit.fredkin(0,1,2)
# # circuit.cswap(0,1,2)
# circuit.draw(output='mpl')


# In[61]:


simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend=simulator).result()
plot_bloch_multivector(result.get_statevector())

