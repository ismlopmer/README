'''
Created on 30 dic. 2020

@author: USUARIO
'''

from clase import jugador
import csv
from collections import namedtuple
if __name__ == '__main__':
    fichero = "../data/FIFA20_Important_Stats.csv"
with open(fichero, encoding = 'utf-8') as file:
    reader = csv.reader(file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
 
########################################################################################
     
    def datos():
        jugador = []
        lista = []
        with open("../data/FIFA20_Important_Stats.csv", encoding="utf8") as f:
            reader= csv.reader(f)
            for row in reader:
                jugadores = jugador(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29],row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41],row[42],row[43],row[44],row[45],row[46],row[47],row[48],row[49],row[50],row[51],row[52],row[53],row[54])
                lista.append(jugadores)
        print(lista)
    
    
    #####################################################################################    
    
    def lee_filas_y_columnas():
        i = 0
        
        for columnas in reader:
            i = i + 1
            columnas=len(columnas)
        print('Hay', i, 'filas,', columnas, 'columnas y', columnas*i, "datos")
    
    ######################################################################################
               
    def filtrar_por_nacionalidad_y_pie(nacionalidad, pie):
        jugadores=[]
        for fila in reader:
            if nacionalidad in fila[4]:
                if pie in fila[9]:
                    jugadores.append(fila[2])
        print(jugadores)
    
    #######################################################################################
    
    def nacionalidades_distintas():
        paises=[]
        for fila in reader:   
                paises.append(fila[4])       
        lista_paises = set(paises)
        cantidad_de_paises = len(set(paises))      
        print("En FIFA 20 hay jugadores de", cantidad_de_paises, "paises.\n\nEsos paises son:\n\n",lista_paises)
    
    ######################################################################################    
    
    def media_edad_por_pais(pais):
        media=[]
        p=0
        for fila in reader:
            if pais in fila[4]:
                media.append(fila[3])
        media=[int(x) for x in media] 
        print(media)
        for y in media:
            
            p=p+y
        t=len(media)
        edad_media=p/t
        print("la edad media de los jugadores de", pais,"es", edad_media)
            
    ######################################################################################    
    
    def diccionario_jug_pais(pais):
        res = {}
        for fila in reader:
            res.setdefault(fila[4], fila[2])
        print(res)
    
    ######################################################################################

    nacionalidades_distintas()
        