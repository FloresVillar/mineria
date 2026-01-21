# MINERIA DE DATOS 

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
































```