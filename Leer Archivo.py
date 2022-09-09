import PySimpleGUI as sg
import PySimpleGUI as sg
import pandas as pd
import sidetable as stb

def estadisticas( ):

    # abrir el archivo
    df = pd.read_csv("https://raw.githubusercontent.com/roque63/MATERIAL-PANDAS/main/Archivos/GTO.csv")
    
    # desplegar las columnas del dataframe, sin saltar de renglón por eso end = " "
    for name in df.columns:
        print(name, " ", end = " ")
        
    # saltar de renglon
    print( )
    
    # Desplegar cada renglón del archivo (dataframe)
    for k in range(len(df)):
        print(df.iloc[k, 0],  df.iloc[k, 1],  df.iloc[k, 2],  df.iloc[k, 3], df.iloc[k, 4], df.iloc[k, 5] , df.iloc[k,6]) #font =("chalkboard", 12))
def estadisticas( ):

    # abrir el archivo
    df = pd.read_csv("https://raw.githubusercontent.com/roque63/MATERIAL-PANDAS/main/Archivos/GTO.csv")
    
    # desplegar las columnas del dataframe, sin saltar de renglón por eso end = " "
    for name in df.columns:
        print(name, " ", end = " ")
        
    # saltar de renglon
    print( )
    
    # Desplegar cada renglón del archivo (dataframe)
    for k in range(len(df)):
        print(df.iloc[k, 0],  df.iloc[k, 1],  df.iloc[k, 2],  df.iloc[k, 3], df.iloc[k, 4], df.iloc[k, 5] , df.iloc[k,6]) #font =("chalkboard", 12))


estadisticas( )