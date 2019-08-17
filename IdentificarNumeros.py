#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_digits
import pylab as pl
import sklearn


# In[4]:



# cargamos los datos y desplegamos el objeto
digits = load_digits()
type(digits)


# In[5]:


# observe las propieades del objeto, ¿a que tipo se le parece?
get_ipython().run_line_magic('pinfo', 'sklearn.utils.Bunch')


# In[39]:


pl.gray() # Queremos las imágenes en grises
pl.matshow(digits.images[50]) # Imprimir una imagen dada
numImagenes = len(digits.images) # Numero de imagenes, len es un método que provee el tamaño del arreglo
#print("Se tienen en total:", numImagenes, "imágenes")
# Ver su representación en pixeles
print(digits.images[50])
#print(digits.images[50])
print(digits.keys())


# #Solución

# In[64]:


targetObjetivos=[]
imagesObjetivos=[]
print(range(len(digits.target)))
for i in range(len(digits.target)):
    if digits.target[i] == 0 or digits.target[i] == 3:
        targetObjetivos.append(digits.target[i])
        imagesObjetivos.append(digits.images[i])
print(targetObjetivos)
print(imagesObjetivos)


# In[ ]:


matrizPromedio = [[]]
sumatoria = 0.0
for i in range(len(imagesObjetivos[0])):
    for j in range(len(imagesObjetivos[0])):
        for k in range(len(imagesObjetivos)):
            sumatoria += imagesObjetivos[j][i]
            
    

