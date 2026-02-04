# Arboles de Desicion 

Ayuda a tomar desiciones de forma visual, nos permite sopesar los resultados y consecuencias, trazamos ademas un camino hacia el resultado deseado

Arbol de desicion representa la funcion de hipotesis mediante un grafo dirigido :
    - Cada nodo es una variable de entrada
    - Cada rama es un valor posible de esa variable correspondiente
    - Las hojas corresponden con las variables de clase 
    - clasificamos recorriendo desde la raiz  , eligiendo la rama que satisface la condicion para el valor del atributo, la clase elegida seria la asignada a la hoja a la que llega

<p align="center">
    <img src="imagenes/1.png" width="75%">
</p>

Se construyen particionando el espacio de entrada de manera recursiva. En cada paso se elige la variable que produce la particion optima. La particion se representa en un arbol

Hasta aqui es muy abstracto
```bash
# se tiene

i | X1 | X2 | Y
--+----+----+---
1 |  2 |  2 | A
2 |  3 |  1 | A
3 |  4 |  2 | B
4 |  5 |  3 | B
5 |  6 |  1 | B

Paso 1:
    R = {{xi,yi}} i:1→5
    #pero esto se simplifica* indicando la i-esima observacion, de modo que en lugar de R={((2,2),A),((3,1),A),((4,2),B),((5,3),B),((6,1),B)} tenemos 
    R ≡ IR ​= {1,2,3,4,5}  #usamos el indice de la observacion i-esima
    # lo mismo para 
    R1 = {1,2}  == R1​={(x1​,y1​),(x2​,y2​)}
    R2 = {3,4,5} == R2​={(x3​,y3​),(x4​,y4​),(x5​,y5​)}
paso 2 :
    # definimos las proporciones pk​=1/∣R∣ ∑​(yi​=k)
    pA = 2/5   Pb = 3/5
paso 3: 
    # calculando la impureza
    I(R) = 1 - SUMA pk^2
         = 1 - 1/5^2 - 3/5^2 
         = 0.48
paso 4 : 
    # generando candidatos split
    Cj​={ (x(i)j​ + x(i+1)j)/2 ​​}
    # se ordenan los valores de las variables y se calculan los puntos medios de los consecutivos distintos
    C1={2.5,3.5,4.5,5.5}  # para 2, 3, 4, 5, 6
    C2​={1.5,2.5}          # para 1, 1, 2, 2, 3
paso 5
    # definimos las particiones para cada split
i | X1 | | Y
--+----+-+---
1 |  2 | | A
2 |  3 | | A
3 |  4 | | B
4 |  5 | | B
5 |  6 | | B
    # para cada split la proporcion y la impureza
        c=2.5
    R1​(1,2.5)={i:xi1​≤2.5}={1}     R1​:pA​=1,pB​=0  I(R1) = 1 -1^2 -0^2 = 0
    R2​(1,2.5)=i:xi1>2.5}={2,3,4,5} R1​:pA​=1/4,pB​=3/4
    I(R2) = 1 - (1/4)^2 - (3/4)^2 = 1 -10/16 = 6/16
    # combinando la impureza Isplit​(j,c)=∣R1∣/∣R​∣​ *I(R1​) + ∣R2∣/∣R​∣*​I(R2​)
    Isplit(1,2.5) = 1/5 * 0 + 4/5*6/16 = 24/80
        c = 3.5
    R1​(1,3.5)={1,2}           R1​:pA​=2/2,pB​=0
    R2(1,3.5)={3,4,5}         R1​:pA​=0,pB​=3/3
        c = 4.5
    R1​(1,4.5)={1,2,3}       R1​:pA​=2/3,pB​=1/3
    R2(1,4.5)={4,5}         R1​:pA​=0,pB​=2/2
        c =5.5
    R1​(1,5.5)={1,2,3,4}     R1​:pA​=2/4,pB​=2/4
    R2​(1,5.5)={5}           R1​:pA​=0,pB​=1/1
    # observar que es el indice de la observacion y no la variable X1,(A,B)

i | | X2 | Y
--+----+----+---
1 | |  2 | A
2 | |  1 | A
3 | |  2 | B
4 | |  3 | B
5 | |  1 | B
        c = 1.5
    R1​(2,1.5)={2,5}   R1​:pA​=1,pB​=1
    R2​(2,1.5)={1,3,4} R2​:pA​=1,pB​=2

        c = 2.5
    R1​(2,2.5)={1,2,3,5} R2​:pA​=2,pB​=2
    R2(2,2.5)={4}       R2​:pA​=0,pB​=1
paso 6 
    # proporcion en cada particion
    pk∣Rm​​=∣Rm​∣1​i∈Rm​∑​1(yi​=k) # se hizo dentro de paso 5
paso 7
    # impureza de cada region
    I(Rm​)=1−k∑​pk∣Rm​2​  # dentro de paso 5
paso 8
    # combinar impurezas
    ∣R∣∣R1​∣​I(R1​) +|R|∣R2​∣​I(R2​)
    split​(X1​,3.5)   # dentro de paso 5
paso 9
    #optimizacion local greedy
    (j∗,c∗)=argj,cmin​Isplit​(j,c)

paso 10
    # criterio de parada

```

