# KD-Tree

Resumen parafraseado de chatgpt.
Mencionar que claude.ai es mucho menos verboso que chatgpt, mucho mas conciso, casi trivial.Gpt por su parte tiene una presentacion incluso didactica y muy amigable.

un KD-Tree es una estructura de datos para organizar puntos en un espacio de k dimensiones.

Se usa para :
- Busqueda de vecino mas cercano
- Busqueda por rango
- Acelerar consultas espaciales en machine learning

Es un arbol binario, en lugar de dividir por valores discretos (Binary Search Tree) divide el espacio geometrico por hiperplanos

La complejidad es O(log n) como se espera del uso de un arbol binario

Ejemplo 

La construccion de las regiones 

```bash
    (2,8), (5,3), (7,6), (1,4), (9,2), (4,7), (6,1)

    Se ordena en el eje X
     (1,4), (2,8), (4,7), ([5],3), (6,1), (7,6), (9,2)
    Se calcula la mediana (en X [5])  y este punto sera la raiz

    
8  · (2,8)          
7      · (4,7)  |  · (7,6)
6               |           
5               |           
4  · (1,4)      |           
3          (5,3)*           
2               |  · (6,1)  · (9,2)
1               |           
   1  2  3  4  5  6  7  8  9   
                |
         corte en X=5


          (5,3)          ← divide por X
         /     \

    
    Ahora en Y , lado izquierdo (1,4), (4,[7]), (2,8)
    
8  · (2,8)      |
7  -----(4,7)*--+               corte en Y=7
4  · (1,4)      |
                |
   1  2  3  4  5

                lado derecho  (6,1), (9,[2]), (7,6)

6               |  · (7,6)
2               +-----(9,2)*---  corte en Y=2
1               |  · (6,1)
                |
                5  6  7  8  9  


         (5,3)          ← divide por X
         /     \
      (4,7)   (9,2)      ← dividen por Y   


8  · (2,8)      |              
7  -----(4,7)---+-----------      ← Y=7
6               |      ·(7,6)   
5               |        
4  · (1,4)      |              
3               |(5,3)     
2               +------------(9,2)   ← Y=2
1               |    · (6,1)   
                |              
   1  2  3  4   X=5  6  7  8   9    

Luego cada region solo tiene un punto

           (5,3)          ← divide por X
         /     \
      (4,7)   (9,2)       ← dividen por Y
      /   \   /   \
   (1,4)(2,8)(6,1)(7,6)   ← hojas

```

Seguidamente la consulta de (6,5)  k =1
```bash
    Se incia en (5,3) 
        X : 6>5 a la derecha
        ahora en (9,2)
            Y : 5>2  a la derecha
                (7,6)

    Ahora se calcula la distancia euclideana 
    d(6,5) , (7,6) =   1.41   candidato (7,6) d=1.41
    
8  · (2,8)      |              
7  -----(4,7)---+--------------+-------- Y=7
6               |   ✓(7,6)1.41 
5               |      ×(6,5)  
4  · (1,4)      |               
3               |(5,3)      
2               +--------------+(9,2)--- Y=2
1               |    · (6,1)   
                |              
   1  2  3  4   5    6  7  8   9    

   Se sube a (9,2) eje Y
   d (6,5) , (9,2) = 4.24 > 1.41 no mejora
   Distancia  a Y=2  |5 - 2| = 3 > 1.41 podamos (6,1)

          (5,3)
         /     \
      (4,7)   (9,2) 4.24
      /   \   /   \
   (1,4)(2,8) ✗   ✓
             (6,1)(7,6)1.41


8  · (2,8)      |              
7  -----(4,7)---+--------------+--------
6               |   ✓(7,6)1.41 
5               |      ×(6,5)  
4  · (1,4)      |              
3               |(5,3)     
2               +--------------+(9,2)---
1               |   ✗(6,1)        ← podado, 3 > 1.41
                |              
   1  2  3  4   5    6  7  8   9    

   se sube a (5,3) eje X
   d (6,5) , (5,3) = 2.24 > 1.41 no mejora
   Distancia  a X=3  |6 - 5| = 1 < 1.41 explorar lado izq

    
8  · (2,8)      |              
7  -----(4,7)---+--------------+--------
6               |   ✓(7,6)1.41 
5               |      ×(6,5)  
4  · (1,4)      |              
3               |(5,3)2.24 
2               +--------------+(9,2)---
1               |   ✗(6,1)     
                |              
   1  2  3  4   5    6  7  8   9    
                ←~~1~~×
                  esfera cruza X=5

           (5,3) 2.24
         /     \
     →(4,7)   (9,2) 4.24
      /   \   /   \
   (1,4)(2,8) ✗   ✓
             (6,1)(7,6)1.41

    se baja a (4,7) eje Y
   d (6,5) , (4,7) = 2.83 > 1.41 no mejora
   Distancia  a Y=7  |5 - 7| = 2 > 1.41 podar las ramas 

           (5,3) 2.24
         /     \
      (4,7)✗  (9,2) 4.24
      2.83
      /   \   /   \
     ✗     ✗  ✗   ✓
  (1,4)(2,8)(6,1)(7,6)1.41

```
Un ejemplo para k = 2, la logica es la misma pero se mantienen dos puntos candidatos.

Para 3 dimensiones (X.Y.Z)
 [ (2,8,1), (5,3,7), (7,6,2), (1,4,9), (9,2,3), (4,7,5), (6,1,8), (3,5,4), (8,9,6), (2,3,7), (6,8,3), (1,6,2), (9,4,8), (5,7,1), (3,9,5) ]
```bash
    ordenar en X y calcular la mediana (5,3,7) X=5
    izq X<5:  (1,4,9),(1,6,2),(2,3,7),(2,8,1),(3,5,4),(3,9,5),(4,7,5)

    der X>5:  (6,1,8),(6,8,3),(7,6,2),(8,9,6),(9,2,3),(9,4,8),(5,7,1)

    Z
│              │
│     izq      │      der
│              │
└──────────────────────── X
               X=5

    Lado izquierdo mediana en Y (1,6,2) Y=6
    izq_izq  Y<6:  (2,3,7),(1,4,9),(3,5,4)
    izq_der  Y>6:  (4,7,5),(2,8,1),(3,9,5)

    Lado derecho mediana en Y (7,6,2)  Y=6
    der_izq  Y<6:  (6,1,8),(9,2,3),(9,4,8)
    der_der  Y>6:  (5,7,1),(6,8,3),(8,9,6)

Z
│    Y=6       │       Y=6    │
│  izq_izq     │   der_izq   │
│──────────────│─────────────│
│  izq_der     │   der_der   │
└──────────────────────────── X
               X=5

Ahora en Z 
    zq_izq (2,3,7),(1,4,9),(3,5,4)
    Mediana → (2,3,7). Plano Z=7
        izq_izq_izq  Z<7:  (3,5,4)
        izq_izq_der  Z>7:  (1,4,9)

    izq_der (4,7,5),(2,8,1),(3,9,5)
    Mediana → (4,7,5). Plano Z=5 
        izq_der_izq  Z<5:  (2,8,1)
        izq_der_der  Z>5:  (3,9,5)

    der_izq (6,1,8),(9,2,3),(9,4,8)
    Mediana → (6,1,8). Plano Z=8
        der_izq_izq  Z<8:  (9,2,3)
        der_izq_der  Z>8:  (9,4,8)
    
    der_der (5,7,1),(6,8,3),(8,9,6) 
    Mediana → (6,8,3). Plano Z=3
        der_der_izq  Z<3:  (5,7,1)
        der_der_der  Z>3:  (8,9,6)

    Y=6          Y=6
          │            │
Z=7 ─────┼────  Z=8 ──┼────
          │            │
Z=5 ─────┼────  Z=3 ──┼────
          │            │
          └────────────────── X
                      X=5

Nivel 0:                          (5,3,7)   ← X=5
                           /               \
Nivel 1:              (1,6,2)                 (7,6,2) ← Y=6 | Y=6
                      /    \                 /       \
Nivel 2:         (2,3,7)  (4,7,5)        (6,1,8)      (6,8,3) ← Z=7 | Z=5 | Z=8 | Z=3
                /   \      /   \        /      \       /    \
Nivel 3:   (3,5,4)(1,4,9)(2,8,1)(3,9,5)(9,2,3)(9,4,8)(5,7,1)(8,9,6)  ← hojas
```
**Algoritmo**

```bash
función construir(puntos, profundidad=0):
    si puntos está vacío: retorna null
    
    eje = profundidad mod k
    ordenar puntos por eje
    mediana = len(puntos) // 2
    
    nodo.punto = puntos[mediana]
    nodo.izq   = construir(puntos[:mediana], profundidad+1)
    nodo.der   = construir(puntos[mediana+1:], profundidad+1)
    
    retorna nodo



función buscar(nodo, consulta, profundidad=0, mejor=null):
    si nodo es null: retorna mejor
    
    // 1. Calcular distancia al nodo actual
    d = distancia(consulta, nodo.punto)
    si mejor es null o d < distancia(consulta, mejor):
        mejor = nodo.punto
    
    // 2. Decidir qué lado explorar primero
    eje = profundidad mod k
    si consulta[eje] <= nodo.punto[eje]:
        lado_cercano = nodo.izq
        lado_lejano  = nodo.der
    sino:
        lado_cercano = nodo.der
        lado_lejano  = nodo.izq
    
    // 3. Explorar lado cercano primero
    mejor = buscar(lado_cercano, consulta, profundidad+1, mejor)
    
    // 4. Verificar si vale la pena explorar el lado lejano
    si |consulta[eje] - nodo.punto[eje]| < distancia(consulta, mejor):
        mejor = buscar(lado_lejano, consulta, profundidad+1, mejor)
    
    retorna mejor
```


**codigo final**

En el cuaderno jupyter, aun falta documentar la teoria , pese a tener comentarios escuetos al derecho de las lineas

