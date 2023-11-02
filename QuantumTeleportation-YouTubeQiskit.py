#!/usr/bin/env python
# coding: utf-8

# In[10]:


from qiskit import *
from qiskit.tools.visualization import plot_histogram
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


circuit = QuantumCircuit(3,3)
circuit.draw(output='mpl')


# In[4]:


circuit.x(0)
circuit.barrier()
circuit.draw(output='mpl')


# In[5]:


circuit.h(1)
circuit.cx(1,2)


# In[6]:


circuit.draw(output='mpl')


# In[7]:


circuit.cx(0,1)
circuit.h(0)
circuit.draw(output='mpl')


# In[8]:


circuit.barrier()
circuit.measure([0,1],[0,1])
circuit.draw(output='mpl')


# In[9]:


circuit.barrier()
circuit.cx(1,2)
circuit.cz(0,2)
circuit.draw(output='mpl')


# In[12]:


circuit.measure(2,2)
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend= simulator,shots=1024).result()
counts = result.get_counts()
plot_histogram(counts)


# In[13]:


print(counts)


# In[ ]:




