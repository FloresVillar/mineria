# Ball Tree

La teoria menciona , que mientras kd-tree divide el espacio con hiperplanos, ball tree hace lo propio con hiperesferas, bolas que contienen los puntos

Cada bola tiene un centroide y un radio

**Pasos**

- Calcular en centroide de todos los puntos
- Calcular el radio = distancia maxima del centroide a cualquier punto
- Encontrar el eje de mayor varianza
- Proyectar los puntos en ese eje y tomar la mediana
- Dividir en dos grupos : izq y der respecto a la mediana
- Recursion ..

**Pseudocodigos**

```bash
funcion construir(puntos):
    si len(puntos)==0: return null
    si len(puntos)==1: return nodo hoja

    nodo.centroide = media(puntos)
    nodo.radio = max(distancia(centroide,p))

    eje = eje de mayor varianza
    ordenados = ordenar puntos en ese eje
    mediana = len(puntos)//2
    nodo.izq = construir(ordenados[:mediana])
    nodo.der = construir(ordenados[mediana:])

    retorna nodo
```

```bash
funcion buscar(nodo,p,candidatos):
    si nodo es null: return candidatos
    d_centroide = distancia(p,nodo.centroide)
    si len(candidatos)==k:
        si d_candidatos - nodo.radio >=candidatos[0][0]: #poda: si la bola mas cercana posible esta mas lejos que el peor candidato
            retornar candidatos                          #la bola mas cercana posible es d_centroide - radio
    si nodo es hoja:
        d = distancia(p,nodo.punto)
        actualizar candidatos con(d,nodo.punto)
        retorna candidatos
    d_izq = distancia(p,nodo.izq.centroide)
    d_der = distancia(p,nodo.der.centroide)
    si d_izq <= d_der:
        candidatos = buscar(nodo.izq,p,candidatos)
        candidatos = buscar(nodo.der,p,candidatos)
    sino:
        candidatos = buscar(nodo.der,p,candidatos)
        candidatos = buscar(nodo.izq,p,candidatos)
```
Pero un ejemplo hecho paso a paso clarifica muchisimo

**Ejemplo** 

- Construccion

```bash
(2,8),(5,3),(7,6),(1,4),(9,2),(4,7),(6,1)  p=(6,5)   k = 1
# construccion 
centroide = (Sumax, Sumay)/n_datos
          = (34, 31) / 7 
        = (4.85,4.43)
radio = mayor distancia del centroide a los puntos 
radio = 4.80
Varianzas en X y en Y 
[np.float64(6.693877551020408), np.float64(5.959183673469389)], escoger X
#Dividiendo  X en torno a su mediana
[[1 4]
 [2 8]
 [4 7]]

[[5 3]
 [6 1]
 [7 6]
 [9 2]] # ver que se ha ordenado de acuerdo a los x'ss

De modo que se tiene 

Y
8  · (2,8)         ╔══════════════════╗
7    · (4,7)       ║                  ║
6         · (7,6)  ║   radio=4.80     ║
5              ×   ║   c=(4.86,4.43)  ║
4  · (1,4)         ║                  ║
3    · (5,3)       ╚══════════════════╝
2         · (9,2)
1              · (6,1)
   1  2  3  4  5  6  7  8  9   X

Ahora repetir el analisis para cada lado , hasta que los "lados/bolas" tengan un solo elemento

# nivel 1 bola izquierda

Nivel 1 — bola izquierda (1,4),(2,8),(4,7)
centroide = (2.33, 6.33)
radio     = 2.69
Varianza X=1.56, Y=2.89 → eje mayor varianza = Y
Ordenados por Y: (1,4),(4,7),(2,8)
Mediana → (4,7). Divide:
izq_izq:  (1,4)          ← hoja
izq_der:  (4,7),(2,8)

# nivel 1 bola derecha

Nivel 1 — bola derecha (5,3),(6,1),(7,6),(9,2)
centroide = (6.75, 3.0)
radio     = 3.01
Varianza X=2.19, Y=3.50 → eje mayor varianza = Y
Ordenados por Y: (6,1),(9,2),(5,3),(7,6)
Mediana → (5,3). Divide:
der_izq:  (6,1),(9,2)
der_der:  (5,3),(7,6)

# nivel 2 
Nivel 2 — 4 bolas finales
izq_izq: (1,4) → hoja directa
izq_der: (4,7),(2,8)
centroide = (3.0, 7.5)
radio     = 1.12
der_izq: (6,1),(9,2)
centroide = (7.5, 1.5)
radio     = 1.58
der_der: (5,3),(7,6)
centroide = (6.0, 4.5)
radio     = 1.80

Nivel 0:          Bola_0  c=(4.86,4.43) r=4.80
                  /      \
Nivel 1:    Bola_izq       Bola_der
            c=(2.33,6.33)  c=(6.75,3.0)
            r=2.69         r=3.01
            /    \          /       \
Nivel 2: (1,4) Bola_izq_der Bola_der_izq Bola_der_der
         hoja  c=(3.0,7.5)  c=(7.5,1.5)  c=(6.0,4.5)
               r=1.12       r=1.58        r=1.80
               /   \        /    \        /    \
Nivel 3:    (4,7) (2,8)  (6,1) (9,2)  (5,3) (7,6)
```

- Busqueda

```bash
p  = (6,5)  k =1  # punto y vecino de consulta

#Paso 1: 

Bola_0
d_centroide = dist((6,5), (4.86,4.43))  = 1.28

dmin = 1.28 - radio(4.8) = -3.52 < 0 
# se explora

¿que hijo primero? el mas cercano
d_centroide Bola_izq = dist((6,5),(2.33,6.33)) = 3.90
d_centroide Bola_der = dist((6,5),(6.75,3.0))  = 2.14

2.14 < 3.90 explorar 

#PASO 2  

Bola_der 
Paso 2: Bola_der c=(6.75,3.0) r=3.01
d_centroide = 2.14
minima_posible = 2.14 - 3.01 = -0.87
Negativo → dentro de la bola → exploramos.
¿Qué hijo primero?
d_centroide Bola_der_der = dist((6,5),(6.0,4.5)) = 0.50
d_centroide Bola_der_izq = dist((6,5),(7.5,1.5)) = 3.81
0.50 < 3.81 → exploramos Bola_der_der primero

#Paso 3:

Bola_der_der c=(6.0,4.5) r=1.80
d_centroide = 0.50
minima_posible = 0.50 - 1.80 = -1.30
Dentro → exploramos ambas hojas:
Hoja (7,6):
d = dist((6,5),(7,6)) = sqrt(1+1) = 1.41
Candidato: (7,6) = 1.41
Hoja (5,3):
d = dist((6,5),(5,3)) = sqrt(1+4) = 2.24
2.24 > 1.41 → no mejora

#paso 4

Paso 4: Bola_der_izq c=(7.5,1.5) r=1.58
d_centroide = 3.81
minima_posible = 3.81 - 1.58 = 2.23
peor candidato = 1.41

2.23 >= 1.41 → PODAMOS toda la bola


#Paso 5:

Bola_izq c=(2.33,6.33) r=2.69
d_centroide = 3.90
minima_posible = 3.90 - 2.69 = 1.21
peor candidato = 1.41

1.21 >= 1.41 ? False → exploramos
¿Qué hijo primero?
d hoja (1,4)         = dist((6,5),(1,4))   = 5.10
d Bola_izq_der c=(3,7.5) = dist((6,5),(3,7.5)) = 3.91
3.91 < 5.10 → exploramos Bola_izq_der primero

#Paso 6:

Bola_izq_der c=(3.0,7.5) r=1.12
d_centroide = 3.91
minima_posible = 3.91 - 1.12 = 2.79
peor candidato = 1.41

2.79 >= 1.41 → PODAMOS (4,7) y (2,8)

#Paso 7:

Hoja (1,4)
d = dist((6,5),(1,4)) = sqrt(25+1) = 5.10
5.10 > 1.41 → no mejora

#resultado 
Nivel 0:        Bola_0 ✓ visitada
                /      \
Nivel 1:   Bola_izq✓   Bola_der✓
            /    \       /       \
Nivel 2: (1,4)✓ Bola_izq_der✗  Bola_der_izq✗  Bola_der_der✓
                  PODADA          PODADA
                  /   \           /    \          /    \
Nivel 3:       (4,7) (2,8)     (6,1) (9,2)    ✓(7,6) ✗(5,3)
               podados          podados        1.41


Visitados: Bola_0, Bola_der, Bola_der_der, (7,6), (5,3), Bola_der_izq, Bola_izq, Bola_izq_der, (1,4)
Podados:   (6,1), (9,2), (4,7), (2,8)  → 4 puntos nunca evaluados
```
*falta documentar el codigo*