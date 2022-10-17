# -*- coding: utf-8 -*-
"""labo_2_sinx.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LLiuNrZ1sHkUAoIvS9l3kDhahNXDMTtd
"""

'''
  caso de lab 2 : 
  *parcialmente observable->por que no se tiene la informacion del objetivo
  *agente individual->por que es un solo agente
  *entorno determinista->hace lo que tiene que hacer
  *secuencial->por que una accion afecta a otras
  *dinámico->por que cambia el entorno
  *continuo->por que los valores varian entre abajo arriba derecha izquierda
  *entorno desconocido->por que no se conoce el camino
  Participantes
   Jhon Alan Fernandez Maturano
   Alexander Sacaca Colque 
   Yamil Fernando Torrez Garcia
   Erick Martin Peñafiel Picha
   José Fernando Alfaro Ayzama
   
'''
import random
import time
import os
#numero fila
numero_filas = int(input('Introduzca el número de filas del laberinto: '))
#numero columnas
numero_columnas = int(input('Introduzca el número de columnas del laberinto: '))
#7*8=56
#numero de paredes=30
numero_paredes = int(input('Introduzca el número de paredes del laberinto: '))

#numero de espacios
numero_espacios = numero_filas * numero_columnas - numero_paredes
#56-30=26

def crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios):
# Se crea un mapa lleno de paredes
    mapa_laberinto = []
    numero_paredes_generadas = 0
    for fila in range(0, numero_filas):
        fila_mapa_laberinto = []
        for columna in range(0, numero_columnas):
            fila_mapa_laberinto.append('#')
        mapa_laberinto.append(fila_mapa_laberinto)
#Se ubica aleatoriamente un punto de inicio y a partir de ese punto se llenan espacios
    numero_espacios_generados = 0
    fila_posicion_actual = random.randrange(1,numero_filas-1)
    columna_posicion_actual = random.randrange(1,numero_columnas-1)
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
    numero_espacios_generados += 1
    while numero_espacios_generados < numero_espacios:
        direccion = random.randrange(4)
        if direccion == 0 and fila_posicion_actual > 0:  
            fila_posicion_actual -= 1
        elif direccion == 1 and fila_posicion_actual < numero_filas - 1:
            fila_posicion_actual += 1
        elif direccion == 2 and columna_posicion_actual > 0:
            columna_posicion_actual -= 1
        else:
            if columna_posicion_actual < numero_columnas - 1 :
                columna_posicion_actual += 1
        if fila_posicion_actual > 0 and fila_posicion_actual <numero_filas-1 and columna_posicion_actual >0 and columna_posicion_actual< numero_columnas-1:
          if mapa_laberinto[fila_posicion_actual][columna_posicion_actual] == '#':
              mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
              numero_espacios_generados += 1
    #posicion del jugador
    posicionX = random.randrange(numero_filas)
    posicionY = random.randrange(numero_columnas)
    mapa_laberinto[posicionX][posicionY] = 'G'           

    return mapa_laberinto

def mover(laberinto,numero_columnas,numero_filas, posiciones,comida):
  #posiciones.append([fila_Y , fila_X])
  #  Y=X    X=Y
  #print("pos y",fila_X,"- pos x",fila_Y);

  movimiento=0
  juego=True
  while movimiento<=comida:
    #time.sleep(1.2)
    for fila_mapa_laberinto in laberinto:
      print(fila_mapa_laberinto)
    print(posiciones)
    
    for i in range(0,numero_filas):
      for j in range(0,numero_columnas):
        if laberinto[i][j]== 'G':
          fila_X=j;
          fila_Y=i;
    if laberinto[fila_Y-1][fila_X] != ' ' and laberinto[fila_Y+1][fila_X] != ' ' and laberinto[fila_Y][fila_X-1] != ' ' and laberinto[fila_Y][fila_X+1] != ' ' :  
      posiciones=[]
      laberinto=reiniciar_tabla(laberinto,numero_columnas,numero_filas)
     

    comida_premion , posiciones=comida_rica(fila_X, fila_Y, laberinto ,posiciones)

    if comida_premion:
      direccion = random.randrange(3)
      #print(direccion,"dir")
      #arriba
      
      if direccion == 0 and laberinto[fila_Y-1][fila_X] == ' ':
        if buscar_posicion(posiciones,fila_X,fila_Y-1):
          laberinto[fila_Y][fila_X]='X'
          laberinto[fila_Y-1][fila_X]='G'
          print(fila_Y-1, "-",fila_X)

          posiciones.append([fila_Y-1,fila_X])
        
          #abajo
      elif direccion == 1 and laberinto[fila_Y+1][fila_X] == ' ':
        if buscar_posicion(posiciones,fila_X,fila_Y+1):
          laberinto[fila_Y][fila_X]='X'
          laberinto[fila_Y+1][fila_X]='G'
         
          print(fila_Y+1,'-',fila_X)

          posiciones.append([fila_Y+1,fila_X])
        #izquierda
      elif direccion == 2 and laberinto[fila_Y][fila_X-1] == ' ':
        if buscar_posicion(posiciones,fila_X-1,fila_Y):
          laberinto[fila_Y][fila_X]='X'
          laberinto[fila_Y][fila_X-1]='G'
         
          print(fila_Y,'-',fila_X-1)
        
          posiciones.append([fila_Y,fila_X-1])
      #Derecha
      else:
        if laberinto[fila_Y][fila_X+1]== ' ':
          if buscar_posicion(posiciones,fila_X+1,fila_Y):
            laberinto[fila_Y][fila_X]='X'
            laberinto[fila_Y][fila_X+1]='G'
           
            print(fila_Y,'-',fila_X+1)
          
            #posciones anadimos
            posiciones.append([fila_Y,fila_X+1])
    else:
      movimiento+=1
      if movimiento >= comida:
        print("termino")
        juego=False
        movimiento+=1

      print(movimiento)
      laberinto=reiniciar_tabla(laberinto,numero_columnas,numero_filas)
      posiciones=[]
    os.system('cls')
  return juego
#columna
#
#

###### fila

def buscar_posicion(posiciones,fila_X,fila_Y):
  for movimiento in posiciones:
    if movimiento[0] == fila_Y and movimiento[1] == fila_X: 
      return False
  return True

def comida_rica(fila_X, fila_Y, laberinto,posiciones):
  if laberinto[fila_Y-1][fila_X] == 'O':
    laberinto[fila_Y-1][fila_X]='G'
    laberinto[fila_Y][fila_X]='X'
    return False,[]
  elif  laberinto[fila_Y+1][fila_X] == 'O':
    laberinto[fila_Y+1][fila_X]='G'
    laberinto[fila_Y][fila_X]='X'

    return False,[]
  elif  laberinto[fila_Y][fila_X-1] == 'O':
    laberinto[fila_Y][fila_X-1]='G'
    laberinto[fila_Y][fila_X]='X'

    return False,[]
  else:
    if  laberinto[fila_Y][fila_X+1] == 'O':
      laberinto[fila_Y][fila_X+1]='G'
      laberinto[fila_Y][fila_X]='X'
      return False,[]
  return True,posiciones

def reiniciar_tabla(laberinto,numero_columnas,numero_filas):
  for fila in range(numero_filas):
    for columna in range(numero_columnas):
      if laberinto[fila][columna] == 'X':
        laberinto[fila][columna]= ' '

  return laberinto

def puntos(laberinto, numero_filas, numero_columnas, comida):
  for aux in range(comida):  
    posicionX = random.randrange(numero_filas-2)
    posicionY = random.randrange(numero_columnas-2)  
    laberinto[posicionX][posicionY] = 'O'   
  return laberinto

laberinto = crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios)


comida=2

laberinto = puntos(laberinto, numero_filas, numero_columnas, comida)

for fila_mapa_laberinto in laberinto:
    print(fila_mapa_laberinto)


print("   ")
posiciones=[]
#aqui retornaba el laberinto
# laberinto1= mover(laberinto ,numero_columnas , numero_filas)

# for fila_mapa_laberinto in laberinto1:
#   print(fila_mapa_laberinto)

#while play:
play=True;
play=mover(laberinto ,numero_columnas , numero_filas, posiciones , comida)
