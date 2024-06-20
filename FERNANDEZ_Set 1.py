#!/usr/bin/env python
# coding: utf-8

# In[1]:


def savings(gross_pay, tax_rate, expenses):
    
    return int((int(gross_pay) * (1-float(tax_rate)) // 1) - int(expenses))


savings(1200, 0.5, 100)


# In[2]:


def material_waste(total_material, material_units, num_jobs, job_consumption):
    
    return (str(int(total_material) - (int(num_jobs) * int(job_consumption))) + str(material_units))

material_waste(100, "kg", 20, 2)


# In[3]:


def interest(principal, rate, periods):
   
    return int(principal) + (int(principal) * (float(rate) * int(periods)) // 1) 

interest(200, 0.5, 2)

