# K-NN (el basico) 
**resumen parafraseado de claude**

Cuales son los k vecinos mas cercanos a un punto de consulta

Memoriza los datos y en el momento de la consulta calcula la distancia


```bash
ENTRADA: puntos, consulta, k
SALIDA:  k vecinos más cercanos

1. para cada punto en puntos:
       calcular distancia(consulta, punto)
       guardar (distancia, punto)

2. ordenar por distancia ascendente

3. retornar los primeros k
```

**Ejemplo**

```bash
Y
8  · (2,8)
7    · (4,7)
6         · (7,6)
5              ★ (6,5)  ← consulta
4  · (1,4)
3    · (5,3)
2         · (9,2)
1              · (6,1)
   1  2  3  4  5  6  7  8  9   X

# PASO 1 distancias

d( (6,5), (2,8) ) = sqrt( (6-2)² + (5-8)² ) = sqrt(16+9)  = sqrt(25)  = 5.000
d( (6,5), (5,3) ) = sqrt( (6-5)² + (5-3)² ) = sqrt(1+4)   = sqrt(5)   = 2.236
d( (6,5), (7,6) ) = sqrt( (6-7)² + (5-6)² ) = sqrt(1+1)   = sqrt(2)   = 1.414
d( (6,5), (1,4) ) = sqrt( (6-1)² + (5-4)² ) = sqrt(25+1)  = sqrt(26)  = 5.099
d( (6,5), (9,2) ) = sqrt( (6-9)² + (5-2)² ) = sqrt(9+9)   = sqrt(18)  = 4.243
d( (6,5), (4,7) ) = sqrt( (6-4)² + (5-7)² ) = sqrt(4+4)   = sqrt(8)   = 2.828
d( (6,5), (6,1) ) = sqrt( (6-6)² + (5-1)² ) = sqrt(0+16)  = sqrt(16)  = 4.000

#Paso 2 , ordenar

#PuntoDistancia
1   (7,6)1.414
2   (5,3)2.236
3   (4,7)2.828
4   (6,1)4.000
5   (9,2)4.243
6   (2,8)5.000
7   (1,4)5.099

# Paso 3 , retomar los k =3 vecinos (en este caso)
1° vecino: (7,6)  distancia: 1.414
2° vecino: (5,3)  distancia: 2.236
3° vecino: (4,7)  distancia: 2.828

Y
8  · (2,8)
7    ·③(4,7)
6         ·①(7,6)
5              ★ (6,5)
4  · (1,4)
3    ·②(5,3)
2         · (9,2)
1              · (6,1)
   1  2  3  4  5  6  7  8  9   X
```

k-NN para clasificación
Si cada punto tiene una etiqueta (clase), el punto de consulta hereda la clase más frecuente entre sus k vecinos — esto se llama votación por mayoría.
````bash
Ejemplo — clasificar el pixel (250, 10, 10) entre colores RGB:
Colores conocidos:
  Rojo    → (255,   0,   0)
  Verde   → (  0, 255,   0)
  Azul    → (  0,   0, 255)
  Negro   → (  0,   0,   0)
  Blanco  → (255, 255, 255)
  ...

Consulta: (250, 10, 10)

d( consulta, Rojo  ) = sqrt( 5²+10²+10² ) = sqrt(225) = 15.0   ← más cercano
d( consulta, Negro ) = sqrt(250²+10²+10²) = sqrt(62600) = 250.2
d( consulta, Azul  ) = sqrt(250²+10²+245²) = 352.8
...

k=1 → clase asignada: Rojo 
```

