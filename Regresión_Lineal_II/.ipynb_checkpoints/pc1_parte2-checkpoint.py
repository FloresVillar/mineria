#!/usr/bin/env python
# coding: utf-8

# In[53]:


# LIBRERIAS 
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS
import numpy as np
import pandas as pd
import math 
import random as rd
inv = np.linalg.inv
import random as rd
import math
log = math.log


# In[54]:


# PERMUTACION , obtenemos el subconjunto de tamño n_sub de un total de 8 columnas(en este caso)
# teoria cortesia del libro de simulacion


def permutacion(l,n_sub):
    f = []
    k = len(l)
    while k>1:
        i = math.floor(k*rd.uniform(0,1))
        #print(f"i : {i}")
        l[k-1] , l[i] = l[i] , l[k-1]
        f.append(l[k-1])
        if (len(l) - k) + 1  == n_sub:
            break
        k = k - 1
    #print(f)
    return f

if __name__=='__main__':
    l = [0,1,2,3,4,5,6,7]
    p = permutacion(l,5)
    print(p)


# In[25]:


# NORMALIZACION de la data (x - media) /desviacion estandar
# Fase 1 subir y normalizar
def normalizacion(X):
    n , m = X.shape
    medias = np.zeros(m)
    varianzas = np.zeros(m)
    for i in range(m):
        medias[i] = X[:,i].mean()
        varianzas[i] = X[:,i].std()
    for i in range(m):
        X[:,i] = (X[:,i] - medias[i])/varianzas[i]
    return X

if __name__=='__main__':
    datos = fetch_california_housing()
    Xe = datos.data
    y = datos.target
    X = normalizacion(Xe)
    print(f"x:\n{X}")


# In[26]:


# agregar la columna de 1's para la operacion algebraica de modo quee 1*W0  + X*W1 = y_
def X_1(Xe,columna):
    n, m = Xe.shape
    X = np.ones((n,len(columna) + 1))
    for i in range(len(columna)):
        X[:,i + 1] = Xe[:,columna[i]]
    return X

if __name__=='__main__':
    datos = fetch_california_housing()
    Xe = datos.data # con 8 predictores osea 8 vectores columnas
    y = datos.target
    X = normalizacion(Xe)
    columna = [0,2,3] # los indices de las columnas
    X = X_1(X,columna)
    print(f"X:\n{X}")


# In[ ]:





# In[20]:


#    0   1   2   3   4  , totalmente propio
def subconjuntos_no(lista):
    n = len(lista)
    combinaciones = []
    for j in range(n):
        combinaciones.append([j])
        for grupos in range(2,n + 1):
            #sub.append(j)# sub(j)
            for k in range(n-1,j,-1):
                sub = []
                sub.append(j)
                # sub(k)
                # grupos:2 j,k     sub(k) 0,4   0,3  0,2   0,1   0,0
                # grupos:3  j:0 k:4 
                if k - j + 1 >= grupos:
                    for i in range(0,grupos-1):
                        if (k - i) != j:
                            sub.append(k - i)
                    combinaciones.append(sub)
                    #  j,k    sub (k - i)
                # grupos:2 sub(k) 0,4   0,3  0,2   0,1   0,0
        # grupos:2  0,4   0,3  0,2   0,1   0,0
    return combinaciones

if __name__=='__main__':
    lista = [ 0 ,  1 ,  2 ,  3  , 4 ]
    combinaciones = subconjuntos_no(lista)
    print(f"combinaciones:\n{combinaciones}")    


# In[ ]:





# In[ ]:


# pero faltan algunas permutaciones
# sugerencia de gpt para el bucle interno
#    0   1   2   3   4 
def subconjuntos_noo(lista):
    n = len(lista)
    combinaciones = []
    for j in range(n):
        combinaciones.append([j])
        for grupos in range(2,n + 1):
            #sub.append(j)# sub(j)
            for k in range(n-1,j,-1):
                sub = []
                sub.append(j)
                # sub(k)
                # grupos:2 j,k     sub(k) 0,4   0,3  0,2   0,1   0,0
                # grupos:3  j:0 k:4 
                if k - j + 1 >= grupos:
                    for salto in range(1, k - j + 1):
                        sub = [j]
                        for i in range(grupos-1):
                            idx = k - i * salto
                            if idx > j:
                                sub.append(idx)
                        if len(sub) == grupos:
                            if sub not in combinaciones:
                                combinaciones.append(sub)
                    #  j,k    sub (k


# In[27]:


#GPT completamente, subconjuntos de todos los tamaños , no importa el orden en total 2**n  -1 grupos
def subconjuntos(lista):
    n = len(lista)
    combinaciones = []
    # tamaños de los grupos
    for grupos in range(1, n + 1):
        # índices iniciales: [0,1,2,...,grupos-1]
        indices = list(range(grupos))
        while True:
            # construir combinación actual
            combinaciones.append([lista[i] for i in indices])
            # buscar posición para avanzar
            for i in range(grupos - 1, -1, -1):
                if indices[i] != i + n - grupos:
                    break
            else:
                # no se puede avanzar más
                break
            # avanzar este índice
            indices[i] += 1
            # reajustar los que están a la derecha
            for j in range(i + 1, grupos):
                indices[j] = indices[j - 1] + 1
    return combinaciones

if __name__ == "__main__":
    lista = [0, 1, 2, 3, 4]
    combinaciones = subconjuntos(lista)
    print("Combinaciones:")
    for c in combinaciones:
        print(c)
    print("\nTotal:", len(combinaciones))
# y obtiene todas las combinaciones, gpt es mucho mejor programador que yo, triste pero cierto<s


# In[18]:


# NO SE USA
def columnas(subconjunto, indices):
    columna = []
    for e in subconjunto:
        columna.append(indices[e])
    return columna

if __name__=='__main__': 
    p = permutacion([0, 1, 2, 3, 4])
    print(f"permutacion:\n{p}")
    subcon = subconjuntos(p)
    print(f"subcon:\n{subcon}")


# In[41]:


# REGRESION multivariada
def regresion(Xe,y):
    #n , m = Xe.shape
    #X = copiar_columnas(Xe,columna)  # debe ser una dependencia y no estar acoplado 
    theta = inv(Xe.T @ Xe) @ (Xe.T @ y)
    #print(f"theta:\n{theta}")
    return theta

if __name__=='__main__':
    datos = fetch_california_housing()
    X, y = datos.data, datos.target
    X = normalizacion(X)
    X = X_1(X,[4,2,1])
    theta = regresion(X,y)
    print(f"theta:\n{theta} \n para {X}")


# In[48]:


# FASE 2, probando las combinaciones posibles

def fase2(Xe, y):
    l = [0,1,2,3,4,5,6,7]
    indices = permutacion(l,5) 
    # los subconjuntos
    X = normalizacion(Xe)
    subcon = subconjuntos(indices)
    theta_Xi_y = []
    for col in subcon:
        X_i = X_1(X,col)
        theta = regresion(X_i,y) 
        theta_Xi_y.append({"X_i":X_i,"col":col,"y":y,"theta":theta})
        print(f"col:\n{col}\nX_i:\n{X_i}\ntheta:\n{theta}\n\n")
    return theta_Xi_y

if __name__=='__main__':
    datos = fetch_california_housing()
    X, y = datos.data,datos.target
    theta_Xi_y = fase2(X,y)
    print(f"regresion:\n{theta_Xi_y}")


# In[49]:


#METRICAS 
def metricas(X,theta,y):
    print(f"MSE, R_2, R_2_ajustado, AIC, BIC\n")
    y_ = X @ theta
    n , m = X.shape
    k = m  # predictores + intercepto
    m = m - 1 
    MSE = np.sum((y - y_)**2)/len(y)
    R_2 = 1 - np.sum((y - y_)**2)/(np.sum((y - y.mean())**2))
    R_2_ajustado = 1 - (1 - R_2)*(n - 1)/(n - m - 1)
    AIC = 2 * k + n * log(MSE)
    BIC = k * log(n) + n * log(MSE)
    #print(f"X::\n{X} \n, y::\n{y}\n, y_::\n{y_}\n")
    #print(f"theta\n{theta}")
    #print(f"errores\n{MSE} , {R_2} , {AIC} , {BIC}")
    return {"MSE":MSE,"R_2":R_2,"R_2_ajustado":R_2_ajustado,"AIC":AIC,"BIC":BIC}

if __name__=='__main__':
    datos = fetch_california_housing()
    X, y = datos.data, datos.target
    X = normalizacion(X)
    X = X_1(X,[4,2,1])
    theta = regresion(X,y)
    mtrics = metricas(X,theta,y)
    print(f"METRICAS:\n{mtrics}")


# In[52]:


# FASE 3 , metricas
def fase3(data_regresion):
    # se tiene X_i   col   y   theta , cada e de data_regresion tiene esos 4 arrays
    info_final = []
    for e in data_regresion:
        X_i,col,y,theta = e["X_i"],e["col"],e["y"],e["theta"]
        mtrics = metricas(X_i,theta,y)
        info_final.append({"X_i":X_i,"col":col,"y":y,"theta":theta,"metricas":mtrics})
    return info_final

if __name__=='__main__':
    datos = fetch_california_housing()
    X, y = datos.data,datos.target
    data_regresion = fase2(X,y)
    info_final = fase3(data_regresion)
    print(f"x:\n{X} \n y:\n{y}")
    for e in info_final:
        print(f"col:\n {e["col"]}, \n {e["metricas"]}")


# In[4]:


## RESUMEN hasta la fase 3
# LIBRERIAS 
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS
import numpy as np
import pandas as pd
import math 
import random as rd
inv = np.linalg.inv
import random as rd
import math
log = math.log
def permutacion(l,n_sub): # l 8 columnas , n_sub 5 predictores
    f = []
    k = len(l)
    while k>1:
        i = math.floor(k*rd.uniform(0,1))
        #print(f"i : {i}")
        l[k-1] , l[i] = l[i] , l[k-1]
        f.append(l[k-1])
        if (len(l) - k) + 1  == n_sub:
            break
        k = k - 1
    #print(f)
    return f

def normalizacion(X):
    n , m = X.shape
    medias = np.zeros(m)
    varianzas = np.zeros(m)
    for i in range(m):
        medias[i] = X[:,i].mean()
        varianzas[i] = X[:,i].std()
    for i in range(m):
        X[:,i] = (X[:,i] - medias[i])/varianzas[i]
    return X



def subconjuntos(lista):
    n = len(lista)
    combinaciones = []
    # tamaños de los grupos
    for grupos in range(1, n + 1):
        # índices iniciales: [0,1,2,...,grupos-1]
        indices = list(range(grupos))
        while True:
            # construir combinación actual
            combinaciones.append([lista[i] for i in indices])
            # buscar posición para avanzar
            for i in range(grupos - 1, -1, -1):
                if indices[i] != i + n - grupos:
                    break
            else:
                # no se puede avanzar más
                break
            # avanzar este índice
            indices[i] += 1
            # reajustar los que están a la derecha
            for j in range(i + 1, grupos):
                indices[j] = indices[j - 1] + 1
    return combinaciones

def X_1(Xe,columna):
    n, m = Xe.shape
    X = np.ones((n,len(columna) + 1))
    for i in range(len(columna)):
        X[:,i + 1] = Xe[:,columna[i]]
    return X

def regresion(Xs,y):
    #n , m = Xe.shape
    #X = copiar_columnas(Xe,columna)  # debe ser una dependencia y no estar acoplado 
    theta = inv(Xs.T @ Xs) @ (Xs.T @ y)
    #print(f"theta:\n{theta}")
    return theta

def fase2(Xe, y):
    l = [0,1,2,3,4,5,6,7]
    indices = permutacion(l,5) 
    # los subconjuntos
    X = normalizacion(Xe)
    subcon = subconjuntos(indices)
    theta_Xi_y = []
    for col in subcon:
        X_i = X_1(X,col)
        theta = regresion(X_i,y) 
        theta_Xi_y.append({"X_i":X_i,"col":col,"y":y,"theta":theta})
        print(f"col:\n{col}\nX_i:\n{X_i}\ntheta:\n{theta}\n\n")
    return theta_Xi_y

def metricas(X,theta,y):
    #print(f"MSE, R_2, R_2_ajustado, AIC, BIC\n")
    y_ = X @ theta
    n , m = X.shape
    k = m  # predictores + intercepto
    m = m - 1 
    MSE = np.sum((y - y_)**2)/len(y)
    R_2 = 1 - np.sum((y - y_)**2)/(np.sum((y - y.mean())**2))
    R_2_ajustado = 1 - (1 - R_2)*(n - 1)/(n - m - 1)
    AIC = 2 * k + n * log(MSE)
    BIC = k * log(n) + n * log(MSE)
    #print(f"X::\n{X} \n, y::\n{y}\n, y_::\n{y_}\n")
    #print(f"theta\n{theta}")
    #print(f"errores\n{MSE} , {R_2} , {AIC} , {BIC}")
    return {"MSE":MSE,"R_2":R_2,"R_2_ajustado":R_2_ajustado,"AIC":AIC,"BIC":BIC}

def fase3(data_regresion):
    # se tiene X_i   col   y   theta , cada e de data_regresion tiene esos 4 arrays
    info_final = []
    for e in data_regresion:
        X_i,col,y,theta = e["X_i"],e["col"],e["y"],e["theta"]
        mtrics = metricas(X_i,theta,y)
        info_final.append({"X_i":X_i,"col":col,"y":y,"theta":theta,"metricas":mtrics})
    return info_final

def comparar_metricas(info_final):
    """
    info_final.append({"X_i":X_i,"col":col,"y":y,"theta":theta,"metricas":mtrics})
    """
    mejor_R2aj = None
    mejor_AIC = None
    mejor_BIC = None
    for e in info_final:
        col = e["col"]
        met = e["metricas"]
        if mejor_R2aj is None or met["R_2_ajustado"]>mejor_R2aj["valor"]:
            mejor_R2aj={"col":col,"valor":met["R_2_ajustado"]}
        if mejor_AIC is None or met["AIC"]<mejor_AIC["valor"]:
            mejor_AIC={"col":col,"valor":met["AIC"]}
        if mejor_BIC is None or met["BIC"]<mejor_BIC["valor"]:
            mejor_BIC = {"col":col,"valor":met["BIC"]}
    return {"mejor_R2aj":mejor_R2aj ,"mejor_AIC":mejor_AIC,"mejor_BIC":mejor_BIC}

def fase4(info_final):
    columnas = []
    R2 = []
    AIC = []
    BIC = []
    for e in info_final:
        columnas.append(e["col"])
        R2.append(e["metricas"]["R_2_ajustado"])
        AIC.append(e["metricas"]["AIC"])
        BIC.append(e["metricas"]["BIC"])
    tabla = pd.DataFrame({"columnas":columnas,"R2_ajustado":R2,"AIC":AIC,"BIC":BIC})
    tabla_final = tabla.sort_values(by="BIC",ascending=True)
    return tabla_final

if __name__=='__main__':
    datos = fetch_california_housing()
    X, y = datos.data,datos.target
    data_regresion = fase2(X,y)
    info_final = fase3(data_regresion)
    print(f"x:\n{X} \n y:\n{y}")
    for e in info_final:
        print(f"col:\n {e["col"]}, \n {e["metricas"]}")
    result = comparar_metricas(info_final) 
    print(f"\n mejor_R2aj:\n{result["mejor_R2aj"]} \n mejor_AIC:\n{result["mejor_AIC"]}\n mejor_BIC\n {result["mejor_BIC"]} ")
    print(f"tabla:\n{fase4(info_final)}")  


# In[16]:


## CON SKLEARN 
#!pip install mlxtend
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from mlxtend.feature_selection import ExhaustiveFeatureSelector 
import numpy as np
import pandas as pd
datos = fetch_california_housing()
X = datos.data
y = datos.target
escalador = StandardScaler()  # calculará las u y sigma, transformara (== normalizacion)
# entrada X E R^(n * m)  salida lo mismo
X_std = escalador.fit_transform(X)
regresor = LinearRegression() # es solo el modelo de regresion lineal
efs = ExhaustiveFeatureSelector(regresor, min_features=1,max_features=5,cv=0,scoring='neg_mean_squared_error')
# selecciona las columnas en forma de tuplas, pero tambien calcula MSE, aunque no guarda los theta's , == subconjuntos
efs.fit(X_std,y) # tenemos dichas columnas
# ahora recorremos los elementos de subset_ mediante subsets_.values()
resultados =  [] # ==fase3
for subset in efs.subsets_.values():
    cols = subset['feature_idx']  # es una tupla ej: (0,2,5)
    X_sub = X_std[:,cols] # == X_1() ,slicing admite tuplas, entra R^(n*8) sale R^(n*cols)
    regresor.fit(X_sub,y)  # entrenamos cada subconjunto == regresion(Xs,y)
    y_pred = regresor.predict(X_sub) # lo veo redundante
    n = len(y)     # == metricas
    k = X_sub.shape[1] + 1
    MSE = np.mean((y - y_pred)**2)
    AIC = 2*k + n*log(MSE)
    BIC = k*np.log(n) + n*log(MSE)
    resultados.append({"columnas":cols,"AIC":AIC,"BIC":BIC})
tabla = pd.DataFrame(resultados) #==fase4
tabla = tabla.sort_values("BIC")
print(tabla)


# In[64]:

 


