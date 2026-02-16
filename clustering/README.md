 # Clustering 
## **Basado en centroides**

Se tienen **X={x1, x2, x3, ..,xn} xi e R^d** vamos a dividirlo en k cluster <br>

Cada cluster **Ck** tendra un centroide **uk**<br>
**uk = SUMA xi / |Ck|** el promedio de los puntos del cluster

**Minimizamos**   
**J = SUMA SUMA ||xi - uk||^2**

Within sum of squares (WCSS).
Se busca que los puntos esten lo mas cercano a su centro, esto equivale a minimizar la varianza dentro de cada cluster, de modo que se producen cluster "compactos".

**algoritmo**
- Se eligen k centroides iniciales (aleatoriamente)
- Asignamos cada punto al centro mas cercano
- Recalculamos los centroides como el promedio del cluster
- Repitiendo los los 2 pasos anteriores

**Porque el centroide es el promedio?**

Cortesia de gpt , claro con un buen prompt XD
```bash
PROBLEMA
--------

Sea un cluster C_k con n puntos:

    x1, x2, ..., xn      (cada xi ∈ R^d)

Queremos encontrar μ que minimice:

    J(μ) = Σ ||xi - μ||^2
           i=1..n


DESARROLLO COMPLETO
-------------------

1) Expandimos la norma cuadrada:

   ||xi - μ||^2 = (xi - μ)^T (xi - μ)

   = xi^T xi
     - xi^T μ
     - μ^T xi
     + μ^T μ

   Como xi^T μ es escalar:

     xi^T μ = μ^T xi

   Entonces:

     (xi - μ)^T (xi - μ)
     = xi^T xi
       - 2 xi^T μ
       + μ^T μ


2) Sustituimos en J(μ):

   J(μ)
   = Σ [ xi^T xi - 2 xi^T μ + μ^T μ ]
   = Σ xi^T xi
     - 2 Σ xi^T μ
     + Σ μ^T μ


3) Simplificamos sumatorias:

   Σ xi^T xi        → no depende de μ
   Σ xi^T μ         = μ^T Σ xi
   Σ μ^T μ          = n μ^T μ   (porque hay n términos iguales)

   Entonces:

   J(μ)
   = Σ xi^T xi
     - 2 μ^T Σ xi
     + n μ^T μ


4) Derivamos respecto a μ

   Recordemos reglas:

     d/dμ (μ^T a) = a
     d/dμ (μ^T μ) = 2μ

   Derivando término por término:

     d/dμ [Σ xi^T xi]      = 0
     d/dμ [-2 μ^T Σ xi]    = -2 Σ xi
     d/dμ [n μ^T μ]        = 2n μ

   Entonces:

     ∇J(μ) = -2 Σ xi + 2n μ


5) Condición de mínimo

   ∇J(μ) = 0

   -2 Σ xi + 2n μ = 0

   Dividimos entre 2:

   - Σ xi + n μ = 0

   n μ = Σ xi

   μ = (1/n) Σ xi


CONCLUSIÓN
----------

El μ que minimiza:

    Σ ||xi - μ||^2

es:

    μ = promedio de los puntos


INTERPRETACIÓN
--------------

El promedio es el único punto donde:

    Σ (xi - μ) = 0

Las desviaciones se cancelan.
Es el centro de masa.
Minimiza la energía cuadrática total.
Es un mínimo global (la Hessiana = 2nI > 0).

```


**Propiedades**

Funciona bien si los cluster son esfericos , de tamaño similar, separables por distancia ecuclideana. <br>
Mal cuando hay formas no convexas, hay outliers, los cluster tienen densidades muy distintas

**Variante importante : K-medoids**

En lugar del promedio , el centroide es un punto real del dataset. De modo que es mas robusto a outliers

**Geometria**

K-means particiona el espacio en regiones tipo digrama de voronoi

**complejidad**
O(nkd) ,  n= puntos   k=cluster   d=dimension

**EJEMPLO**

```bash
A(1,1),B(1.5,2),C(3,4),D(5,7),E(3.5,5),F(4.5,5)
K= 2 cluster
# 1 inicializacion
μ1(0)​=A(1,1)
μ2(0)​=D(5,7)
# 2 asignacion
A(1,1)
    d^2(A,μ1​)=0             MENOR
    d^2(A,μ2​)=(1−5)^2+(1−7)^2=16+36=52
B(1.5,2)
    d^2(B,μ1​)=(1.5−1)^2+(2−1)^2=0.25+1=1.25  MENOR
    d^2(B,μ2​)=(1.5−5)^2+(2−7)^2=12.25+25=37.25
C(3,4)
    d^2(C,μ1​)=4+9=13
    d^2(C,μ2​)=4+9=13
D(5,7)
    d2^(D,μ1​)=52
    d2^(D,μ2​)=0             MENOR
E(3.5,5)
    d2^(E,μ1​)=6.25+16=22.25
    d2^(E,μ2​)=2.25+4=6.25   MENOR
F(4.5,5)
    d^2(F,μ1​)=12.25+16=28.25
    d^2(F,μ2​)=0.25+4=4.25   MENOR
la asignacion 
    cluster 1 : A(1,1),B(1.5,2),C(3,4)
    cluster 2 : D(5,7),E(3.5,5),F(4.5,5)

como tenemos nuevos puntos en cada cluster ,se calcula el centroide de cada uno , usando (valga la redundancia) estos puntos
# actualizacion de los centroides
μ1​=(1+1.5+3​/3,1+2+4/3​)
μ1​=(1.83,2.33)

μ2​=(5+3.5+4.5/3​,7+5+5/3​)
μ2​=(4.33,5.67)

# Reasignacion
A (1,1)
    d^2(A,u1) = (1−1.83)^2+(1−2.33)^2 = 2.4578
    d^2(A,u2) = (1−4.33)^2+(1−5.67)^2 = 32.89
    permanece en el cluster 1 , no cambia
B (1.5,2)
    d^2(B,u1) = (1.5−1.83)^2+(2−2.33)^2 = 0.21
    d^2(B,u2) = (1.5−4.33)^2+(2−5.67)^2 = 21.47
permanece en el cluster 1 , no cambia
C (3,4)
    d2(C,μ1​)= (3−1.83)^2+(4−2.33)^2 = 4.1578  
    d2(C,μ2​) = (3−4.33)^2+(4−5.67)^2 =  4.5578 
los demas puntos tampoco cambian
C1(1)​=C1(0)​
C2(1)​=C2(0)​
# Funcion objetivo final

    J=∑∥xi​−μk​∥^2
Converge ; minimiza J respecto a asignaciones, minimiza J respecto a centroides

ni las asignaciones ni los centroides cambian

J(t + 1) <= J(t)

Garantiza el minimo local, no el global.


```
Aunque sklearn lo tiene implementado mediante **from sklearn import KMeans** 

```bash
modelo = KMeans(n_clusters=4,n_init='auto')
modelo.fit(X)  # realiza el calculo de los centroides, se entiende que llama a alguna funcion similar a kmeans() implementado
y_clasificacion = modelo.predict(X)  # 0,1,2,0,.. el indice del cluster al cual pertenecen las filas(puntos ) en orden 
centros = modelo.cluster_centers_  
```
Pero para un proceso de aprendizaje adecuado se implementara (en la medida de los posible y con el SOPORTE de gpt) la teoria en funciones claramente identificables.

Comenzamos con la definicion de la distancia
```bash
def distancia (a,b): # son vectores [2,3..],[3,4..]
    d = 0   
    for j in range(len(a)):
        d =+(a[i]-b[i])**2
    return d 
```
Que es la distancia euclidea, luego abarcamos la parte mas extensa e interesante de k-means. 

```bash
def kmeans(x,K,N=1000)
    n  = len(x)  # cantidad de filas (datos)
    d = len(x[0])   # las columnas, dimension , x1,x2,x3...
    for k in range(K):
        centros.append(x[k].copy())      
        #asignar k centroides arbitrariamente , el detalle para usar copy() es que asi se pierde la referencia (nombre distinto para el mismo ojeto )y se trabaja con un recurso nuevo.
    asignaciones[0]*n   # es el objeto analogo a y_pred = modelo.predict(X) , contiene los indices de los cluster a los cuales pertenece la fila i (dato [x11,x12,...]) 
```
Definido los "atributos" , ahora se realiza la iteracion N veces , con una condicion de salida **conteo != True** es decir,los centroides no han cambiado (niguno de ellos) . Termina la iteracion.La teoria asegura que con los centroides estabilizados se minimiza J la distancia de los puntos a sus respectivos centroides.

```bash
    for it in range(N)      # todas las iteraciones
        cambio = False      # bandera de salida
```
Luego para cada dato se analiza respecto a cada cluster 
```bash
    for i in range(n): # cada dato
        cluster_cercano = None
        mejor_distancia = None
            for k in range(K): # cada centroide de los cada k-cluster
                dis = distancia(x[i],centros[k])
                si dis < _distancia: # debe pertenecer al cluster k
                cluster_cercano = k
                mejor_distancia = dis  # la menor distancia 
            # una vez analizados el punto respecto a todos los k-clusters, asignar dicho punto al cluster mas cercano
            if asignaciones[i]!=cluster_cercano:
                cambio = True
            asignaciones[i] = cluster_cercano

```
Una vez realizado el analisis para todos los datos, se tiene asignado dichos puntos a sus "mejores" cluster, a los cluster cuyo cuyos centroides son los mas cercanos a cada punto en cuestion

Ahora creamos los nuevos centros (cada centro tiene una dimension d (x1,x2, .. ,xd)) y una cuenta para cada cada  cluster , de modo que cuentas[k] representa la cantidad de puntos que pertencen a dicho k cluster

Entonces si la fila 2 esta asignado al cluster 0 X3 = [x0=2,x1=4] <br>
nuevos_centros[ind_cluster=0][0] + X3[0]=2 <br>
nuevos_centros[ind_cluster=0][1] +  X3[1]=4 <br>
conteos[ind_cluster=0] ++ 

Y si la fila (dato) 10 X11[0]=1 X11[1]=5 tambien esta asignado al cluster 0 <br>
nuevos_centros[ind_cluster=0][0] + X11[0]=2 <br>
nuevos_centros[ind_cluster=0][1] +  X11[1]=4 <br>
conteos[ind_cluster=0] ++

Entonces , estamos sumando las columnas j de las filas que pertenecen al cluster k

Para luego promediar esos j de cada cluster k , esto dentro de nuevos_cluster donde cada fila [k][] es la referencia a cada cluster , y los elementos  j [k][j] son las coordenadas del centroide de la dimension j-esima , esto es nuevo_u1 , nuevo_u2, nuevo_u3 de cada cluster , desde luego se divide entre conteos[k] para que sea el promedio(centroide).

```bash
    nuevos_centros = []
    conteos = []
    for _ in range(K):
        nuevos_centros.append([0]*d) # d columnas, dimension
        conteos.append(0)
    for i in range(n):
        ind_asignaciones = asignaciones[i]
        conteos[ind_asignaciones] +=1
        for j in range(d):
            nuevos_centros[ind_asignaciones][j]+=x[i][j] # las columnas posicion-j de cada fila como se explico antes
    # para cada cluster con la suma de las nuevas coordenadas del cluster en cada dimension
    for k in range(K):
        if conteos[k]>0:
            for k in range(d):
                nuevo_cluster[k][j]/conteos[k]
    # reasignamos los nuevos centros 
    centros = []
    for k in range(K):
        centros.append(np.array(nuevos_centros[k]))
    if not cambio: # convergio
        break    
```
En este punto se tienen las asignaciones de todos los puntos a su respectivo cluster, aunque N es grande , la condicion if not cambio: asegura que se dio la convergencia, de acuerdo a la teoria generosamente facilitado por gpt

Lo siguiente es mi codigo, para asignar los puntos al cluster . De modo que se tendra un diccionario con id  k del cluster, el centroide centros[k] y los puntos

```bash
    n = len(x)
    for k in range(K):
        puntos = [] 
        for i in range(n):
            if asginaciones[i] == k:
                puntos.append(x[i])
        puntos = np.array(puntos) # temas de sintaxis, pese a quee python presume de ser simple, estas pequeñeces sintacticas pueden provocar dolores de cabeza
        if len(puntos)>0: # solo verificacion 
            mi_cluster.append({INFO})
```
finalmente retornamos centros, asignaciones, cluster

Ahora bien , el tema de los graficos son muy interesantes, mas que solo delegar la generacion de codigos  a gpt, lo que se intento fue codearlo por uno mismo pero siempre (en lugar de libros, foros ) con gpt como respaldo teorico.

La funcion graficar_cluster(M, cluster) grafica para datos con 2 dimensiones como maxio, gpt sugiere que para dimensiones mayores se use pca

obtenemos x,y = DATA[:,0] , DATA[:,1] que son las coordenadas matrices para los x,y
dibujamos la grafica de dispersion via plt.scatter
pero estos son equivalentes a puntos[:,0],puntos[:,1] dentro del for

Luego , pese a que los cluster no son "circulos" propiamente, por motivos didactivos lo dibujo de ese forma
```bash
    for c in clusters:
        puntos = c["puntos"]
        centro = c["centro"]
        plt.scatter(puntos[:,0],puntos[:;1])
        plt.scatter(centro[0],centro[1],marker='X')
        ..
```
Para los puntos dentro del cluster **c**, se calcula las distancias de ese punto al CENTROIDE, nos quedamos con la mayor distancia que sera el radio, luego graficamos un circulo con CENTRO y radio
```bash
    radio = 0.0
    for p in puntos:
        dx = p[0] - centro[0]
        dy = p[1] - centro[1]
        d = (dx**2 + dy**2)**0.5
        if d > radio:
            radio = d
    circulo = plt.Circle(TUPLA,radio,fill=False)   # fill False para solo colorear el borde, TUPLA = (centro[0],centro[1])
    plt.gca()    # plt.gca() obtenemos los ejes actuales GET CURRENT AXES
    plt.gca().add_patch(circulo) # con add_patch() añadimos a los ejes

```
Eso para cada punto que pertence a cada cluster.
finalmente **plt.gca().set_aspect('equal')** para evitar deformaiones.

Luego de PROBAR  el codigo y compararlo con la clase de sklearn 

```bash
    modelo = KMeans(n_clusters=4,n_init='auto')
    modelo.fit(X)
    y = modelo.predict(X)
    centros = modelo.cluster_centers_
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    plt.scatter(centros[:, 0], centros[:, 1], c='red', s=200, alpha=0.75, marker='X', label='Centroides')
 
```
Sin embargo como indica la teoria sklearn usa kmeans++ un algoritmo que elige los centroides inciales de forma mas coherente con los datos. 

De modo que el primer centro se escoge aleatoriamente y los demas se escogen entre los puntos mas lejanos a  los k-centros anteriores

```bash
implementar despues
```
## Clustering jerarquico

```bash
========================================================
CLUSTERING JERÁRQUICO (SINGLE LINKAGE)
========================================================

PUNTOS
A = (1,1)
B = (2,2)
C = (3,1)
D = (6,5)
E = (7,7)
F = (8,6) 

--------------------------------------------------------
CLUSTERS INICIALES
--------------------------------------------------------

{A}   {B}   {C}   {D}   {E}   {F}
 
--------------------------------------------------------
PASO 1 — MATRIZ COMPLETA DE DISTANCIAS
--------------------------------------------------------

        A      B      C      D      E      F
A       -     1.41   2.00   6.40   8.48   8.60
B             -      1.41   5.00   7.07   7.21
C                    -      5.00   7.21   7.07
D                           -      2.23   2.23
E                                  -      1.41
F                                         -

MÍNIMA GLOBAL = 1.41  (A-B)

--------------------------------------------------------
PASO 2 — FUSIONAR A Y B
--------------------------------------------------------

{A,B}   {C}   {D}   {E}   {F}

Single linkage:
d({A,B},X) = min(d(A,X), d(B,X))

--------------------------------------------------------
PASO 3 — NUEVAS DISTANCIAS
--------------------------------------------------------

{A,B} – C = min(2.00 , 1.41) = 1.41
{A,B} – D = min(6.40 , 5.00) = 5.00
{A,B} – E = min(8.48 , 7.07) = 7.07
{A,B} – F = min(8.60 , 7.21) = 7.21

Matriz reducida:

            {A,B}     C      D      E      F
{A,B}         -      1.41   5.00   7.07   7.21
C                     -      5.00   7.21   7.07
D                            -      2.23   2.23
E                                   -      1.41
F                                          -

MÍNIMA GLOBAL = 1.41  ({A,B} - C)

--------------------------------------------------------
PASO 4 — FUSIONAR {A,B} Y C
--------------------------------------------------------

{A,B,C}   {D}   {E}   {F}

Single linkage:
d({A,B,C},X) = min(d(A,X), d(B,X), d(C,X))

--------------------------------------------------------
PASO 5 — NUEVAS DISTANCIAS
--------------------------------------------------------

{A,B,C} – D = min(6.40 , 5.00 , 5.00) = 5.00
{A,B,C} – E = min(8.48 , 7.07 , 7.21) = 7.07
{A,B,C} – F = min(8.60 , 7.21 , 7.07) = 7.07

Matriz:

            {A,B,C}     D      E      F
{A,B,C}        -       5.00   7.07   7.07
D                       -      2.23   2.23
E                              -      1.41
F                                     -

MÍNIMA GLOBAL = 1.41  (E-F)

--------------------------------------------------------
PASO 6 — FUSIONAR E Y F
--------------------------------------------------------

{A,B,C}   {D}   {E,F}

Single linkage:
d({E,F},X) = min(d(E,X), d(F,X))

--------------------------------------------------------
PASO 7 — NUEVAS DISTANCIAS
--------------------------------------------------------

D – {E,F} = min(2.23 , 2.23) = 2.23

{A,B,C} – {E,F}
= min(7.07 , 7.07) = 7.07

Matriz:

              {A,B,C}     D      {E,F}
{A,B,C}          -       5.00     7.07
D                         -       2.23
{E,F}                               -

MÍNIMA GLOBAL = 2.23  (D - {E,F})

--------------------------------------------------------
PASO 8 — FUSIONAR D CON {E,F}
--------------------------------------------------------

{A,B,C}   {D,E,F}

--------------------------------------------------------
PASO 9 — ÚLTIMA DISTANCIA
--------------------------------------------------------

d({A,B,C} , {D,E,F})
= min(5.00 , 7.07 , 7.07)
= 5.00

--------------------------------------------------------
PASO 10 — FUSIÓN FINAL
--------------------------------------------------------

{A,B,C,D,E,F}

ALGORITMO TERMINA
========================================================

```
El ejemplo anterior es muy detallado, se fusionan los clusters de menor distancia, y en la siguiente iteracion buscamos la distancia mas corta, si la distancia menor no se da entre un punto del cluster anterior fusionado y otro punto analizaddo, se fusionara (creando otro cluster) de modo que se tendran 2 clusters con mas de un elemento en cada cluster. Okay, se repite hasta obtener un unico Dendograma.

Se usa la distancia euclideana, para ello la funcion dist(p,q)
```bash
def dist(p,q):
    d = 0
    for i in range(len(p)):
        d+=(p[i]-q[i])**2
```
Ademas para cada para-cluster de calcula la minima distancia entre ellas , llamando a la funcion anterior cada vez que sea requiera

```bash
def d_cluster(cl1,cl2):
    minima = float('inf')
    for p in cl1:
        for q in cl2:
            d = dist(p,q)
            if d < minima:
                minima = d
    return minima 
```

Con las funciones que calculan las distancias y la que determina la menor entre un par de cluster, nos embarcamos en la logica principal

Comenzamos haciendo que cada dato(punto) sea un cluster
```bash
for i in range(n):
    _clusters[i] = [datos[i]]  # un array en si mismo

```
Luego usamos **cluster_id = n** pues para implementar el concepto de dendograma(osea el dendograma mismo ) los indices corresponden a los puntos ,primero para los datos y luego incrementandose y asignandose al mismo tiempo a cada cluster,estto resultado de la fusion de los puntos de menor distancia

n-indices (0,1→n-1) para los n puntos(datos) luego n indice del 1er(0) cluster formado, n+1 del sdo(1) cluster formado  y asi en adelante

```bash
cluster_id = len(datos)
```

Como se indica antes, el algoritmo es "recursivo" mientras no se tenga un unico cluster **len(_cluster)>1** . Esto resulta pues cada vez que se hace la fusion se eliminan los cluster(puntos) anteriores **_cluster.pop(indice del cluster)**

```bash
while len(_clusters)>1:
    mejor_distancia 
    mejor_i
    mejor_j
    ids = list(_clusters.keys()) # _clusters es un {} para obtener sus indices usamos keys() , estos indices no consecutivos 0,1,2..  sino 4,5,6.. por el tipo de eliminacion antes señalada
```

Ahora dentro de este bucle se realiza en analisis cluster vs cluster , comparando el cluster i vs los i+1, i+2....clusters
```bash
Matriz reducida:

            {A,B}     C      D      E      F
{A,B}         -      1.41   5.00   7.07   7.21
C                     -      5.00   7.21   7.07
D                            -      2.23   2.23
E                                   -      1.41
F
```
```bash
    for i in range(len(ids)):
        for j in range(i+1,len(ids)):
            d = d_cluster(cl1,cl2) # distancia entre cluster , recordad que d_cluster llama a distancia para cada punto que pertenezca al cluster, obteniendo el minimo

            # luego se obtienen los indices de los cluster con la menor distancia
            if d < mejor_distancia:
                mejor_distancia = d
                mejor_i = ids[i]
                mejor_j = ids[j]

```
Ahora bien , concatenamos los cluster con la menor distancia

```bash
        nuevo_cluster  = _clusters[mejor_i] + _clusters[mejor_j]
        if mejor_i > mejor_j:
            _clusters.pop(mejor_i)
            _clusters.pop(mejor_j)
            ...
    # y asignamos al indices cluster_id de _clusters el nuevo_cluster
    _cluster[cluster_id] = nuevo_cluster
    cluster_id =+1
```

Ahora bien , una vez obtenido el dendograma logico pasamos a graficarlo

De acuerdo con la teoria no se va a graficar los puntos originales, sino su posicion de acuerdo a los indices de los puntos , en el nivel de las hojas, y los puntos medios de los cluster que forman la union , todo esto en el eje de las abscisas. Y para el eje de las ordenadas la distancia d calculado anteriormente.

```bash
x = {}                    #indices
for i in range(n):
    x[i] = i
altura = {}               # ordenadas
for cluster in clusters:  # para todos los clusters
    d = cluster["d"]
    i = cluster["i"]
    j = cluster["j"]
    id_ = cluter["id"]
    x1 = x[i]
    x2 = x[j]
    y1 = altura[i] is i in altura else 0
    y2 = altura[j] is j in altura else 0
    plt.plot([x1,x1],[y1,d])   # el punto (x1,x1) se une verticalmente con el punto (y1,d)
    plt.plot([x2,x2],[y2,d]) # lo mismo
    plt.plot([x1,x2],[d,d]) # la recta horizontal a la altura d en la cual se realizo la fusion 
    #para la coordenada del cluster fusion se promedia (x1 + x2) /2
    x[id_] = (x1 + x2)/2
    altura[id_] = d
```
Se grafican A,B como hojas. luego en la siguiente iteracion, si el x[i] es el cluster fusionado el punto se grafica en (x1+x2)/2 y la altura es d, luego se realiza el analisis para el otro punto que forma el (se entiende) nuevo cluster.

```bash
     -------------------
          |                 
        (ABC)             
          |                
         1.41              
      ---------         
      |       |         
    (AB)      C          
      |                             
     1.41                          
   ------                          
   |    |                           
   A    B                           
```


Hecho esto se compara con la implementacion de sklearn. 

```bash
    import scipy.cluster.hierarchy as sch

    X,_ = make_blobs(n_samples = 300,centers = 4, cluster_std = 0.60, random_state = 0)
    plt.figure(figsize(10,5))
    dendogram = sch.dendogram(sch.linkage(x,method='ward'))
    
    modelo = AgglomerativeClustering(n_clusters = 4, metric = 'euclidean' , linkage ='ward')
    y  = modelo.fit_predict(X)
    plt.scatter(X[:,0],X[:,1], c = y, s= 50, cmap = 'rainbow')

    
```
## Basado en densidades
Algoritmo Paso a Paso 

Para cada punto no visitado: Marcar como visitado. 

Calcular su vecindad ε. 

Si no tiene suficientes vecinos → marcar como ruido. 

Si es núcleo → crear nuevo cluster. 

Expandir cluster: 

    Agregar todos sus vecinos.

    Si alguno también es núcleo, agregar sus vecinos también.

    Continuar hasta que no crezca más.
    
Eso genera clusters como regiones conectadas por densidad.

```bash
============================================================
DBSCAN – EJEMPLO COMPLETO EN ASCII

DATASET

A = (1,1)
B = (1.2,1.1)
C = (0.8,1)
D = (5,5)
E = (5.2,5.1)
F = (9,1)

PARAMETROS

eps = 0.5
minPts = 3

============================================================
PASO 0 – INICIALIZACION

Visitados = {}
Clusters = []
Ruido = []

============================================================
PASO 1 – PUNTO A

Distancias desde A

A-B = 0.22
A-C = 0.20
A-D = 5.66
A-E = 5.94
A-F = 8.00

Vecindad(A) con eps=0.5

N(A) = {A,B,C}

|N(A)| = 3 >= minPts

=> A es NUCLEO

Crear Cluster 1

Cluster 1 = {A}

EXPANSION DESDE A

Revisar B

Distancias desde B

B-A = 0.22
B-C = 0.45

N(B) = {A,B,C}
|N(B)| = 3 >= 3

=> B es NUCLEO

Cluster 1 = {A,B}

Revisar C

Distancias desde C

C-A = 0.20
C-B = 0.45

N(C) = {A,B,C}
|N(C)| = 3 >= 3

=> C es NUCLEO

Cluster 1 = {A,B,C}

No aparecen nuevos puntos
Expansion termina

Clusters = [ {A,B,C} ]

Visitados = {A,B,C}

============================================================
PASO 2 – PUNTO D

Distancias desde D

D-E = 0.22
D-A = 5.66
D-B = 5.45
D-C = 5.83
D-F = 5.00

N(D) = {D,E}
|N(D)| = 2 < 3

=> D NO es nucleo

D = RUIDO

Ruido = {D}

Visitados = {A,B,C,D}

============================================================
PASO 3 – PUNTO E

N(E) = {D,E}
|N(E)| = 2 < 3

=> E NO es nucleo

E = RUIDO

Ruido = {D,E}

Visitados = {A,B,C,D,E}

============================================================
PASO 4 – PUNTO F

N(F) = {F}
|N(F)| = 1 < 3

=> F NO es nucleo

F = RUIDO

Ruido = {D,E,F}

Visitados = {A,B,C,D,E,F}

============================================================
RESULTADO FINAL

CLUSTER 1:
{A,B,C}

RUIDO:
{D,E,F}
```
