#Emiliano Estrada
#A01769252

import PySimpleGUI as sg
import pandas as pd
import statistics as st
import webbrowser

print=sg.Print

def formulario():
    texto_genero = sg.Text("Genero:", font = ("chalkboard", 20))
    opciones_genero = ("Masculino", "Femenino", )
    genero = sg.Combo(opciones_genero, key = "INPUT_genero")
    
    texto_diagnostico = sg.Text("Resultado del diagnostico :", font = ("chalkboard", 20))
    diagnosticos = ("positivo", "Negativo", "no se sabe", )
    diagnostico = sg.Combo(diagnosticos, key = "INPUT_diagnostico")
    
    texto_sintomas = sg.Text("Tipos de sintomas ", font = ("chalkboard", 20))
    sintoma = ("perdida de olfato" , "cansancio" , "dolor de cabeza" , "perdida del gusto" ,"congestion y gripa ")
    sintomas = sg.Combo (sintoma, key = "INPUT_sintomas")
    
    texto_edo = sg.Text("Estado de origen", font = ("chalkboard", 20))
    edos = ('Aguascalientes','Baja California Sur','Baja California','Campeche','Coahuila de Zaragoza','Colima',
            'Chiapas','Chihuahua','Ciudad de M','Durango','Guanajuato','Guerrero','Hidalgo','Jalisco',
            'Mexico','Michoacan','Morelos','Nayarit','NueveLeon','Oaxaca','Puebla','Queretaro',
            'Quintana Roo','San Luis Potosi','Sinaloa','Sonora','Tabasco','Tamaulipas','Tlaxcala','Veracruz de Ignacio de la Llave',
            'Yucatan','Zacatecas','Otro País... ')
    estado = sg.Combo(edos, key = 'INPUT_estado', font = ('chalkboard', 20), text_color = "#369898")
                        
    texto_edad = sg.Text("Ingresa la edad:", font = ("chalkboard", 20))
    edad = sg.Spin(tuple(range(1,150),), key ="INPUT_edad", font = ("chalkboard", 20) )
    
    texto_ingreso = sg.Text("Ingresa la fecha promedio de tu contagio:",font = ("chalkboard", 20))
    opciones_ingreso = ("principios de ano" , "mediados de ano ", "finales de ano")
    ingreso = sg.Combo (opciones_ingreso, key = "INPUT_ingreso")
    
    texto_vacuna = sg.Text("Tipo de vacuna ", font = ("chalkboard", 20))
    opciones_vacuna = ("Janssen de Johnson & Johnson", "pxifer","AstraZeneca ","OTRO")
    vacuna = sg.Combo (opciones_vacuna, key = "INPUT_vacuna")
    grabar=sg.Button("GRABAR",key="GRABAR")
    #Botón para regresar al menu
    regresar_menu=sg.Button("REGRESAR A MENU",key="REGRESAR_MENU")
     # todo frame tiene layout
    layout = [[texto_genero, genero],
              [texto_edad, edad],
              [texto_edo,estado],
              [texto_sintomas,sintomas],
              [texto_diagnostico,diagnostico],
              [texto_ingreso,ingreso],
              [texto_vacuna,vacuna],
              [grabar,regresar_menu]]
    
    frame_formulario = sg.Frame("Formulario", layout, font = ("chalkboard", 25), key = "FRAME_FORMULARIO", visible = False)
    return frame_formulario

def menu():
    
    #Uso de imagenes como botones
    #Formulario
    b1 = sg.Button( key = "BTN_FORMULARIO", image_filename = "formulario.png") 
    #Reporte formulario
    b2 = sg.Button( key = "BTN_ESTADISTICAS", image_filename = "reporte_formulario.png") 
    #Reporte covidDB
    b3 = sg.Button( key = "BTN_ESTADISTICAS2",image_filename = "reporte_CovidDB.png")
    #Maps
    b4 = sg.Button( key = "BTN_MAPS", image_filename = "maps.png")
    #Link a video
    b5 = sg.Button( key = "BTN_VIDEO", image_filename = "video.png") 
    #Salida
    b6= sg.Button( key = "BTN_SALIDA", image_filename = "exit.png")
    
    #Layout del menú
    layout_menu = [ [b1, b2 ,b3] ,
                    [b4, b5,b6]]
    #Frame del menú
    frame_menu = sg.Frame("Menu", layout_menu, key = "FRAME_MENU", visible = False)
    return frame_menu

def validar_ingreso():
    texto_password = sg.Text("Teclea la contraseña ", font = ("chalkboard", 25))
    
    password = sg.Input(password_char = "*" , font = ("chalkboard", 25), key = 'INP_PASSWORD', text_color = "black")
    
    b1 = sg.Button("Validar Ingreso", font = ("chalkboard", 25), key = 'BTN_PASSWORD')
    imagen = sg.Image(filename = 'password.png')
    
    layout =  [[texto_password, password ],
           [imagen] ,
           [b1]
           ]
                         
    #crear el frame - ventana para ingresar los datos del password
    frame_password = sg.Frame("Validar Ingreso", layout, font = ("chalkboard", 25), key = "FRAME_PASSWORD", visible = True)
                         
    return frame_password         

sg.theme("Kayak")

psw=validar_ingreso()
opciones=menu()
formula=formulario()

layout=[[formula,opciones],
        [psw]]

window = sg.Window('Emiliano Estrada ', layout,size=(800,500))

while True:
        
        event,values=window.read()
        
        
        if event==sg.WIN_CLOSED:
                break
        
        elif event=="BTN_PASSWORD":
                password=values["INP_PASSWORD"]
                
                if password=="Emiliano":
                        sg.popup("Bienvenido")
                        window["FRAME_PASSWORD"].update(visible=False)
                        window["FRAME_MENU"].update(visible=True)
                        
                else:
                        sg.popup("Incorrecto")
        
        elif event=="BTN_FORMULARIO":
                window["FRAME_FORMULARIO"].update(visible=True)
                window["FRAME_MENU"].update(visible=False)
                
        elif event=="GRABAR":
                with open("Datos.csv","a") as archivo:
                        genero=values["INPUT_genero"]
                        edad=values["INPUT_edad"]
                        estado=values["INPUT_estado"]
                        sintomas=values["INPUT_sintomas"]
                        diagnostico=values["INPUT_diagnostico"]
                        ingreso=values["INPUT_ingreso"]
                        vacuna=values["INPUT_vacuna"]
                        #Creamos el sting para enviar los datos
                        row=genero + "," + str(edad) + "," + estado + "," + sintomas + "," + diagnostico+ "," + ingreso + "," + vacuna + "\n"
                        #Escribimos los datos en la base
                        archivo.write(row)
                        sg.popup("Datos guardados correctamente")
        
        elif event=="REGRESAR_MENU":
                window["FRAME_MENU"].update(visible=True)
                window["FRAME_FORMULARIO"].update(visible=False)
                
        elif event=="BTN_ESTADISTICAS":
                datos=pd.read_csv("Datos.csv")
                print("Casos por genero:")
                print(datos['Genero'].value_counts())
                print("Conteo de Vacunas:")
                print(datos['Vacuna'].value_counts())
                print("Sintomas más frecuentes:")
                print(datos['Vacuna'].value_counts(sort=True))
                print("Diagnosticos positivos vs negativos:")
                print(datos["Diagnostico"].value_counts())
        elif event=="BTN_ESTADISTICAS2":
                datos=pd.read_csv("covidDB.csv")
                print("Muertes acumuladas totales:",datos["Muertes acumuladas"].sum())
                print("Nuevos casos", datos["Nuevos casos"].sum())
        elif event =="BTN_VIDEO":
                webbrowser.open("https://www.youtube.com/watch?v=aTHBoxCo2SE")
        elif event =="BTN_MAPS":
                webbrowser.open("https://www.google.com/maps/search/vacunacion+covid/@19.3896355,-99.3101109,10z/data=!3m1!4b1")
                
        elif event=="BTN_SALIDA":
                break
window.close()
