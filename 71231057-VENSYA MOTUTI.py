#!/usr/bin/env python
# coding: utf-8

# In[1]:


def perkalian(a, b):
   
    result = 0
    for _ in range(b):
        result += a
    return result

print(perkalian(6, 5)) 
print(perkalian(7, 10))


# In[2]:


def ganjil(bawah, atas):
   
   
    if bawah > atas:
        bawah, atas = atas, bawah
    result = []
    for i in range(bawah, atas + 1):
        if i % 2 != 0:
            result.append(i)
    return result

print(ganjil(10, 30))  
print(ganjil(97, 82))


# In[3]:


def sgpa(jumlah_mk, nilai_a, nilai_b, nilai_c, nilai_d):
    

    sgpa = 0
    for i in range(jumlah_mk):
        if nilai_a[i] != 0:
            sgpa += nilai_a[i] * 4
        elif nilai_b[i] != 0:
            sgpa += nilai_b[i] * 3
        elif nilai_c[i] != 0:
            sgpa += nilai_c[i] * 2
        else:
            sgpa += nilai_d[i] * 1
    sgpa /= jumlah_mk
    return sgpa

jumlah_mk = 5  
nilai_a = [4, 3, 2, 3, 4]  
nilai_b = [3, 2, 3, 4, 3]  
nilai_c = [2, 3, 4, 3, 2]  
nilai_d = [3, 2, 3, 4, 3]  

print(sgpa(jumlah_mk, nilai_a, nilai_b, nilai_c, nilai_d))  


# In[ ]:




