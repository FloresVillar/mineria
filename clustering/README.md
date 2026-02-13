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

funcionan bien si los cluster son esfericos , de tamaño similar, separables por distancia ecuclideana. <br>
Mal cuando hay formas no convexas, hay outliers, los cluster tienen densidades muy distintas

**Variante importante : K-medoids**

En lugar del promedio , el centroide es un punto real del dataset. De modo que es mas robusto a outliers

**Geometria**

K-means particiona el espacio en regiones tipo digrama de voronoi

**complejidad**
O(nkd)  n= puntos   k=cluster   d=dimension

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

## Clustering jerarquico
