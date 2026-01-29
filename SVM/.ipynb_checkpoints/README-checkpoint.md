# SVM 
Resumen de gpt, lo genial es que sintetiza la teoria
Que se esta haciendo ? <br>
1. Buscamos el hiperplano **w*X + b = 0** que maximiza el margen **1/||w||** , lo cual es minimizar **||w||** , pero matematicamente no se maximiza el margen directamente, sino que haremos algo equivalente

2. La distancia de un punto **x** al hiperplano **d(x,H) = |wx + b|/||w||** la margen entre las rectas es **marge =2 /||w||** .

3. Para datos etiquetados **(xi,yi)** con **yi** pertenece **{-1,1}** Problema Primal : <br>
min **||w||^2 / 2** sujeto a   **yi(wx*i + b) >=1** , promagramacion cuadratica convexa

4. Relajacion SOFT MARGIN, con una variable de holgura **yi(w xi + b)>= 1 -Ei**  Ei >=0 Funcion objetivo **min |w|^2 / 2  + C SUMA Ei** 

5. Primal , langrangiano
**L(w , b, lam) = |w|^2 / 2 - SUMA li(yi(wixi + b)-1)** con **li>=0**
   
```bash
```