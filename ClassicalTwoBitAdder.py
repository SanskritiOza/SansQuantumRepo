#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import *


# In[2]:


circuit= QuantumCircuit(4,2)
circuit.x(0) # initialize input A
circuit.x(1) # initialize input B
circuit.barrier()

circuit.cx(0,2)
circuit.cx(1,2)
circuit.ccx(0,1,3)

circuit.barrier()
circuit.measure(2,0) #measure SUM
circuit.measure(3,1) #measure CARRY-OUT
circuit.draw(output='mpl')

