# REGRESION LOGISTICA
Queremos clasificar la clase a la que pertenece una entrada dada, es un tipo de aprendizaje supervisado , aprende de un conjunto ya clasificado.

y e {0,1} se busca que 0 h(x)<1, de forma intutiva se tiene la **regresion lineal x@theta** luego esta se evalua mediante la funcion sigmoide **h** de modo que si el valor es >=umbral → y = 1 0 y =0 respectivamente.

<p align="center">
    <img src="imagenes/1.png" width="75%">
</p>

La frontera de desicion sería el theta obtenido (mediante la ecuacion normal ?) luego , se tendria

<p align="center">
    <img src="imagenes/2.png" width="75%">
</p>

Un ejemplo clarificador 

<p align="center">
    <img src="imagenes/3.png" width="75%">
</p>

No se usa el error cuadratico, pue con h = sigmoide  , J(theta)  = SUMA (h(xi)  - yi)**2 no es convexa. 

Entonces el coste sera -log(h_x(x)) y =1   -log(1-h_x(x))  y=0

coste h_x(),y = -ylog(h_x(x)) - (1 - y)log(1-h_x(x)), luego derivando y usando la gradiente descendente 
<p align="center">
    <img src="imagenes/4.png" width="75%">
</p>

## Regularizacion
Para el tratamiento del sobreajuste, overfifting, esto es que el modelo no generalice con nuevos datos. Una de las causas es el uso de demasiadas caracteristicas(predictores?) 
<p align="center">
    <img src="imagenes/5.png" width="75%">
</p>

1. Reduccion del numero de caracteristicas: seleccionar manualmente de las caracteristicas, algoritmos

2. Regularizacion: reducir la magnitud de los valores de theta 

Se introduce esto de modo que penalizando theta3 o theta4(ejemplo) estos parametros tenderan a valores pequeños. 
<p align="center">
    <img src="imagenes/6.png" width="75%">
</p>

- L1 
<p align="center">
    <img src="imagenes/l1.png" width="75%">
</p>

- L2
<p align="center">
    <img src="imagenes/l2.png" width="75%">
</p>

- Elastic-Net

<p align="center">
    <img src="imagenes/elastic-net.png" width="75%">
</p>

Accuracy , metrica de evaluacion mas basica **Accuracy = (TP + TN)/all samples**

