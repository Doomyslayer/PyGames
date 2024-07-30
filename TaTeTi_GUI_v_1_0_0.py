#Versión del ta-te-tí con interfáz gráfica, Versión 1.0.0

#Importo las librerías a utilizar

import random #para la asignación del primer turno
import guizero#para la GUI


#variables globales para el inicio del juego

contador=0
turno_X=True
X_win=False
O_win=False
#funciones para el juego

def open_window():#ésta función cambia del "menú" al juego
    ventana_auxiliar.hide()
    app.show()

# def captura_de_pantalla(simbolo):
#     global info_de_pantalla,pantalla
#     simbolo=str(simbolo)
#     info_de_pantalla += simbolo
#     pantalla.value=info_de_pantalla
#Diseño de la GUI

#creo una función para colocar una marca en el tablero
def marcar_casilla(button):
  global turno_X, contador;
  if contador%2==0:
      turno_X= True
  else:
     turno_X=False
  if button.value==0:
    if turno_X==True:
       button.text=" X "
       #PushButton(caja_de_numeros,text=" X ", command=lambda:marcar_casilla(button),grid=[0,0])
       contador=contador+1
    else:
       button.text=" O "
       contador=contador+1
  hay_ganador()
from guizero import *

#creo una función para verificar si alguno/a de los/las jugadores/as ha ganado:
def hay_ganador():
  # Verificar filas
  
  if uno.text==cuatro.text ==siete.text:
      print(uno.text+"wins")
  elif dos.text==cinco.text ==ocho.text:
      print(dos.text+"wins")
  elif tres.text == seis.text == nueve.text:
      print(tres.text+"wins")
  
      # Verificar columnas
  if uno.text == dos.text == tres.text:
      print(uno.text+"wins")
  elif cuatro.text == cinco.text == seis.text:
      print(cuatro.text+"wins")
  elif siete.text == ocho.text == nueve.text:
      print(siete.text+"wins")
  
  # Verificar diagonales
  if uno.text == cinco.text == nueve.text:
      print(uno.text+"wins")
  elif tres.text == cinco.text == siete.text:
      print(cuatro.text+"wins")    
  

app = App(title="Ta-Te-Ti - v 1.0.0")#acá va el título de la aplicación
app.hide()#acá la estoy ocultando, porque quiero que tenga una ventana de inicio auxiliar

ventana_auxiliar = Window(app, title="Second window")
ventana_auxiliar.bg="#660505"
textoBienvenida=TextBox(ventana_auxiliar, text="     Bienvenido al Ta-Te-Ti",width="fill")
textoBienvenida.text_size=20
textoBienvenida.text_color="#FFFFFF"
imagenBienvenida = Picture(ventana_auxiliar,image="logov1.png")

open_button = PushButton(ventana_auxiliar, text="Comenzar", command=open_window)
open_button.text_color="#FFFFFF"
open_button.font="Haettenschweiler"
open_button.text_size=30

texto_de_instruccion=Text(ventana_auxiliar,text="Por favor, presione el boton Comenzar para empezar a operar")
texto_de_instruccion.text_color="#FFFFFF"
texto_de_instruccion.text_size=20
    
#Defino y parametrizo una "caja" donde estarán los números, a la izquierda de la app
caja_de_numeros= Box(app,layout="grid",align="center", width="fill",height="fill")

uno=PushButton(caja_de_numeros,text=" ", command=lambda:marcar_casilla(uno),grid=[0,0])
uno.text_color="green"
dos=PushButton(caja_de_numeros,text=" ", command=lambda:marcar_casilla(dos),grid=[0,1])
dos.text_color="green"
tres=PushButton(caja_de_numeros,text=" ", command=lambda:marcar_casilla(tres),grid=[0,2])
tres.text_color="green"
tres.text_color="green"
cuatro=PushButton(caja_de_numeros,text=" ", command=lambda:marcar_casilla(cuatro),grid=[1,0])
cuatro.text_color="green"
cinco=PushButton(caja_de_numeros,text=" ", command=lambda:marcar_casilla(cinco),grid=[1,1])
cinco.text_color="green"
seis=PushButton(caja_de_numeros,text=" ", command=lambda:marcar_casilla(seis),grid=[1,2])
seis.text_color="green"
siete=PushButton(caja_de_numeros,text=" ", command=lambda:marcar_casilla(siete),grid=[2,0])
siete.text_color="green"
ocho=PushButton(caja_de_numeros,text=" ", command=lambda:marcar_casilla(ocho),grid=[2,1])
ocho.text_color="green"
nueve=PushButton(caja_de_numeros,text=" ", command=lambda:marcar_casilla(nueve),grid=[2,2])
nueve.text_color="green"

app.display()
