# PC1 

Se empezara explicando el uso de cuadernos jupyter, la raiz usado por defecto por esta distribucion de python (anaconda) es /c/USERS/usuario de modo que para cambiar esta ruta o para abrir un cuaderno jupyter en cualquier otra carpeta ( por ejemplo en G:/) con **jupyter notebook** hacemos:
```bash
conda init powershell # en anaconda prompt , iniciando conda para powershell
conda activate base # en powershell
jupyter notebook # en un terminal en la carpeta deseada
```
Luego cambiamos el encoding del README.md de ANSI/Latin-1/Windows-1252 a UTF-8 , Reoping with Encoding (ANSI) a Save with Encoding (UTF-8)

Para ocultar las celdas en jupyter notebook se hizo un tanto complicado , de modo que como .ipynb es solo un archivo JSON se usara jupyterLab pues permite renderizar  , ejecutar kernels y tiene mas funciones. Puesto que ademas se intento instalar algunas extensiones jupyter_contrib_nbextensions 
```bash
pip install jupyter_contrib_nbextensions
jupyter contrib nbextensions install --user
```
Ello instaló los paquetes, pero el comando de registro no funcionaba, ya que notebook.nbextensions ya no existe en la version 7.X.X de jupyter notebook
**Como sea, el truco era hacer click en la barra vertical azul del lado izquierdo de la celda**

El texto de la calificada 1

## Fase 1  La Preparación del Terreno 
Cargamos los datos y estandarizamos, en este caso se normaliza , no escala precisamente, usamos la clasica forma (x- media)/desviacion estandar, para cada columna, los datos de cada columna.
La data X **X= datos.data ,y=datos.target ,con datos=fetch_california_housing()** tiene m =8 columnas , los xi columnas son los predictores ,mientras que el total de elementos de la columna o la columna misma es el descriptor.Como sea , se puede escoger n_sub como el tamaño del subconjunto deseado , en particular tenemos n__sub=5.

La funcion **permutacion(n_sub)** obtiene una permutacion de 5 de un total de 8, usamos conceptos de simulacion.Se trató de ser lo mas explicito posible, codigo como documentacion implicito.

Seguidamente se tiene la funcion normalizacion, es esta quien realiza la fase1.
Respecto a la pregunta **¿Por qué no podemos comparar una variable como "Número de habitaciones" con "Ingreso promedio" sin escalarlas primero?** , con la normalizacion eliminamos las unidades y operamos con datos numericos.

## Fase2 El Torneo de Modelos - Búsqueda Exhaustiva 
Que se pretende, vamos a realizar la regresion para todas posibles combinaciones de las 8(en este caso) columnas de **X**, con el **y** constante. 
Por ejemplo X0,X1,X2,X3,X4,X5,X6,X7   para un subbconjunto de 3 X0,X4,X6  realizaremos la regresion Xs =X0 X4 X6   , theta = (XsT Xs)-1 XsT y.

De modo que primero obtenemos dichos subconjuntos mediante **subconjuntos(lista)** , donde lista =[permutacion(5)] y obtiene los subconjuntos de tamaño 1, 2,3,4,5 con un total de 2**5 - 1 = conjuntos. 
 
Cabe mencionar que se intento obtener dichos subconjuntos via aritmetica, lo cual tomó mucho tiempo,no obteniendose el total de subconjuntos, los intentos de codificacion se mantienen ocultos, un total de 2. Es GPT quien con un nivel mayor de abstraccion consigue el objetivo deseado. Aun no se profundiza en su funcionamiento a plenitud.

Entonces lo siguiente es construir la matriz Xs con las columnas (subconjuntos de 1,2..5 tamaños) , para ello usamos la funcion **X_1** donde agregamos la columna de 1's al inicio y **concatenamos** las columnas del subconjunto, como en el ejemplo de X0X4X6 se obtiene Xs = 1X0X4X6. 
En tanto que la funcion **regresion(Xs,y)** obtiene el theta mediante a ecuacion normal  theta = (XsT Xs)-1 XsT y. La  funcion **fase2()** construye mediante un for todos los Xs para todos las col elementos de subcon= subconjuntos(permutacion()). Dentro del mismo for 
conseguimos los thetas 
```bash
    for col in subcon:
        X_i = X_1(X,col)
        theta = regresion(X_i,y)
```
la informacion se guarda en **theta_Xi_y.append({"X_i":X_i,"col":col,"y":y,"theta":theta})**

## Fase3 El Juicio de los Tres Jueces
R_2 , AIC, BIC es usado en la funcion **metricas()**.Esto es teoria nueva y muy interesante, sin embargo lo abordamos de forma practica e intuitiva , siempre con la ayuda sintentizada de GPT.El cual indica <br>

"No estamos resolviendo: **que modelo ajusta mejor estos datos**" pues esto es trivial , el modelo mas grande siempre gana.

"Estamos resolviendo : **que modelo generalizará mejor a datos nuevos que no se han visto**
Ese es el conflicto : bias vs Varianza , Ajuste vs Complejidad , informacion vs ruido

El R_2_ajustado es incluso insuficiente, pues es una formula (aunque no simple) no deriva de un principio probabilistico, no esta conectado a inferencia ni verosimilitud, siempre aumenta al agregar variables , no mide complejidad real.

**Entonces hacemos el salto conceptual → Verosimilitud**<br>
AIC  y BIC no nacen del MSE(error cuadratico medio) sino de :**L(theta | y )** , este responde la pregunta **Que modelo hace mas probable que los datos observados hayan ocurrido?**<br> 
Bajo supuestos gaussianos (es la teoria del cual proviene, en casos practicos solo se usa la formula y se analiza) -2 log(L) DP n log(MSE) , por ello las formulas de AIC y BIC incluyen **n log(MSE)** . 

### AIC:Teoria de la informacion(Akaike)
<br>
AIC = 2k -2log(L)<br>
AIC = 2k + n log(MSE)<br>

Que esta optimizando IAC realmente? <br>
Minimiza la divergencia (de Kullback-Leibler) entre : el modelo verdadero(desconocido) y el modelo estimado
 **quiero un modelo que pierda menos informacion al aproximar** de modo que tolera complejidad(?) , prefiere modelos grandes, excelente para prediccion.

### BIC : Inferencia Bayesiana (Schwarz)
BIC = klog(n) -2log(L)
BIC = klog(n) +n log(MSE)

BIC castiga mucho mas la complejidad (k log n) mientras que aic penaliza 2k (no el n). Aproximamos -2log(P(modelo | datos)) esto es **cual es el modelo mas probable dado los datos** de modo que si una variable no aporta BIC la elimina, aunque mejore un poco el ajuste.

En cuanto a la Parsimonia, el principio de OCCAM **no multiplicar entidades sin necesidad** , BIC implementa OCCAM no se usa el modelo mas complejo porquee aumentar la complejidad (mas columnas) aumenta solo un poco la verosimilitud(nos acercamos solo un poquito mas al modelo real)
Pero detallemos en este concepto, parsimonio no es: **usar menos modelos porque si** o **usar el modelo mas simple**, el problema es que cada predictor nuevo introduce varianza adicional , incertidumbre y ruido<br>
    ERROR = bias**2 + varianza + ruido<br>
```bash
modelos grandes bajo  bias ↓ pero alta varianza ↑
modelos pequeños alto bias ↑ pero bajo varianza ↓
```
Entonces la parsimonia busca minimo error esperado no el observado , BIC calcula cuando una variable merece existir, no necesariamente pretende disminuir la cantidad de predictores .
Parsimonia esta codificada en BIC , penalizacion BIC = k log n
 **Cada nuevo parametro debe justificaar su existencia aumentando la verosimilitud en al menos** log n  si no lo hace es solo ruido.

 Si dos modelos explican casi igual los datos, se prefiere el mas simple

 los resultados muestran en mas ocasiones que se prefieren el subconjunto de tamaño 5 y otras veces las de tamaño 3.

 
 ## Fase  4 :
 Finalmente la funcion comparar metricas , teniendo la **info_final** con los Xi , col, y, theta, metricas; se comparan las metricas R2ajustado , AIC y BIC para quedarnos con el mayor R2ajustado y menores AIC , BIC .Entendiendo las implicancias teoricas de cada metrica.

Para concluir , la funcion fase4() crea un data frame mediante pandas para observar la indo de auerdo al menor BIC, quien nos brinda la info de que columnas brindan mayor verosimilitud dado una complejidad.

## SKLEARN
Todo lo anterior se hara via las funciones de las librerias(libreria?) Sklearn.
```bash
datos = fetch_california_housing()
X = datos.data
y = datos.target
escalador = StandardScaler()  # calculará las u y sigma, transformara (== normalizacion)
# entrada X E R^(n * m)  salida lo mismo
X_std = escalador.fit_transform(X)
regresor = LinearRegression() # es solo el modelo de regresion lineal
EFS = ExhaustiveFeatureSelector(lr, min_features=1,max_features=5,scoring)
# selecciona las columnas en forma de tuplas, pero tambien calcula MSE, aunque no guarda los theta's , == subconjuntos
EFS.fit(X_std,y) # tenemos dichas columnas
# ahora recorremos los elementos de subset_ mediante subsets_.values()
resultados =  [] # ==fase3
for subset in efs.subsets_.values():
    cols = subset['feature_idx']  # es una tupla ej: (0,2,5)
    X_sub = X_std[:,cols] # == X_1() ,slicing admite tuplas, entra R^(n*8) sale R^(n*cols)
    lr.fit(X_sub,y)  # entrenamos cada subconjunto == regresion(Xs,y)
    y_pred = lr.predict(X_sub) # lo veo redundante
    n = len(y)     # == metricas
    k = X_sub.shape[1] + 1
    MSE = np.mean((y - y_pred)**2)
    AIC = 2*k + n*log(MSE)
    BIC = k*np.log(n) + n*log(MSE)
    resultados.append({"columnas":cols,"AIC":AIC,"BIC":BIC})
tabla = pd.DataFrame(resultados) #==fase4
tabla = tabla.sort_values("BIC")
print(tabla)
```


 


































```