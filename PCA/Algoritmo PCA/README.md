## LDA
Merodo de reduccion de dimension supervisado, maximiza la separacion entre clases de datos.

Maximiza la varianza entre-clases, minimiza la varianza dentro de la clase

<p align="center">
<img src="imagenes/lda.png" width="80%">
</p>

Ejemplo

```bash
==========================
       EJEMPLO MANUAL LDA
==========================

Datos originales:
X1  X2  Clase
2   3    0
3   3    0
2   4    0
5   2    1
6   2    1
6   3    1

1️⃣ Medias por clase y global:
Clase 0: μ0 = ((2+3+2)/3 , (3+3+4)/3) = (2.33, 3.33)
Clase 1: μ1 = ((5+6+6)/3 , (2+2+3)/3) = (5.67, 2.33)
Media global: μ = ( (2+3+2+5+6+6)/6 , (3+3+4+2+2+3)/6 ) = (4, 2.83)

2️⃣ Matriz de dispersión intra-clase SW:
X0 - μ0 = 
[-0.33, -0.33]
[ 0.67, -0.33]
[-0.33,  0.67]

SW0 = (X0-μ0)^T*(X0-μ0) = |0.67  -0.33|
                             |-0.33  0.67|

X1 - μ1 = 
[-0.67, -0.33]
[ 0.33, -0.33]
[ 0.33,  0.67]

SW1 = (X1-μ1)^T*(X1-μ1) = |0.67  -0.33|
                             |-0.33 0.67|

SW = SW0 + SW1 = |1.34  -0.66|
                  |-0.66 1.34|

3️⃣ Matriz de dispersión entre-clase SB:
μ0 - μ = (-1.67, 0.5)
μ1 - μ = ( 1.67,-0.5)

SB0 = n0*(μ0-μ)*(μ0-μ)^T = 3*|2.79  -0.835|
                               |-0.835 0.25|
     = |8.37 -2.505|
       |-2.505 0.75|

SB1 = n1*(μ1-μ)*(μ1-μ)^T = 3*|2.79  -0.835|
                               |-0.835 0.25|
     = |8.37 -2.505|
       |-2.505 0.75|

SB = SB0 + SB1 = |16.74 -5.01|
                  |-5.01 1.5 |

4️⃣ Resolver eigenvalores: SW^-1 * SB * w = λ*w
SW^-1 ≈ (1/det(SW)) * | 1.34  0.66 |
                       | 0.66  1.34 |
det(SW) = 1.34*1.34 - (-0.66)*(-0.66) = 1.36
SW^-1 ≈ |0.985 0.485|
         |0.485 0.985|

SW^-1 * SB ≈ |13.53 -2.5 |
              | 2.5  -0.01|

Eigenvector principal (λ máximo) ≈ w = [0.97, 0.24]

5️⃣ Proyección de los datos: Z = X * w

Clase 0:
(2,3) → 2*0.97 + 3*0.24 ≈ 2.69
(3,3) → 3*0.97 + 3*0.24 ≈ 3.63
(2,4) → 2*0.97 + 4*0.24 ≈ 2.93

Clase 1:
(5,2) → 5*0.97 + 2*0.24 ≈ 5.03
(6,2) → 6*0.97 + 2*0.24 ≈ 6.00
(6,3) → 6*0.97 + 3*0.24 ≈ 6.24

✅ Las clases ahora están separadas en 1 dimensión. 
```

<p align="center">
    <img src="imagenes/ejemplo_1.png" width="80%">
</p>

<p align="center">
    <img src="imagenes/ejemplo_2.png" width="80%">
</p>


## t -sne

Reduccion de dimensionalidad no lineal

Intenta preserver vecindad probabilistica

Si dos puntos estan cerca en alta dimension , en baja dimenson tambien los estaran

Tenemos x1​,x2​,...,xm​∈Rd y vamos a representarlos como y1​,y2​,...,ym​∈R2

PASOS

<p align="center">
    <img src="imagenes/t_sne.png" width="80%">
</p>

