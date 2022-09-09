#Emiliano Estrada
#A01769252

import PySimpleGUI as sg


def formulario():
    texto_genero = sg.Text("Genero:"), font = ("chalkboard", 20))
    opciones_genero = ("Masculino", "Femenino", )
    genero = sg.Combo(opciones_genro, key = "INPUT_GENERO")
    
    texto_diagnostico = sg.Text("resultado del diagnostico :", font = ("chalkboard", 20))
    resultado = ("positivo", "Negativo", "no se sabe", )
    resultado = sg.Combo(diagnostico, key = "INPUT_resultados")
    
    texto_sintomas = sg.Text("tipos de sintomas ":, font = ("chalkboard", 20))
    sintomas = ("perdida de olfato" , "cansancio" , "dolor de cabeza" , "perdida del gusto" ,"congestion y gripa ")
    sintomas = sg.Combo (sintomas, key = "INPUT_sintomas")
    
    texto_edo = sg.Text("Estado de origen", font = ("chalkboard", 20))
    edos = ('Aguascalientes','Baja California Sur','Baja California','Campeche','Coahuila de Zaragoza','Colima',
'Chiapas','Chihuahua','Ciudad de M','Durango','Guanajuato','Guerrero','Hidalgo','Jalisco',
'Mexico','Michoacan','Morelos','Nayarit','NueveLeon','Oaxaca','Puebla','Queretaro',
'Quintana Roo','San Luis Potosi','Sinaloa','Sonora','Tabasco','Tamaulipas','Tlaxcala','Veracruz de Ignacio de la Llave',
'Yucatan','Zacatecas','Otro País... ')
    estados = sg.Combo(edos, key = 'INP_ESTADO', font = ('chalkboard', 20), text_color = "#369898")
                        
    texto_edad = sg.Text("Ingresa la edad:", font = ("chalkboard", 20))
    edad = sg.Spin(tuple(range(1,150),), key ="INP_EDAD", font = ("chalkboard", 20) )
    
    texto_ingreso = sg.text("ingresa la fecha promedio de tu contagio:",font = ("chalkboard", 20))
    opciones_ingreso = ("principios de ano" , "mediados de ano ", "finales de ano")
    ingreso = sg.Combo (ingreso, key = "INPUT_INGRESO ")
    
    texto_vacuna = sg.text("tipo de vacuna "), font = ("chalkboard", 20))
    opciones_vacuna = "Janssen de Johnson & Johnson", "pxifer","AstraZeneca ","OTRO")
    vacuna = sg.Combo (ingreso, key = "INPUT_VACUNA ")
                        
    
    # todo frame tiene layout
    layout = [ [ texto_platillo, platillo ] , [texto_arma, arma] ]
    
    frame_formulario = sg.Frame("Formulario", layout, font = ("chalkboard", 25), key = "FRAME_FORMULARIO", visible = True)
    return frame_formulario
    
    b1 = sg.Button( key = "BTN_FORMULARIO", border_width = 5, image_filename = "FormularioAct8_2.png" ) # image_filename = " "
    b2 = sg.Button( key = "BTN_BUSQUEDA", border_width = 5, image_filename = "BusquedaAct8_2.png" ) # image_filename = " "
    b3 = sg.Button( key = "BTN_ESTADISTICAS", border_width = 5, image_filename = "EstadisticasAct8_2.png" ) # image_filename = " "
    b4 = sg.Button( key = "BTN_BASE_DATOS", border_width = 5, image_filename = "Base_de_datosAct8_2.png" ) # image_filename = " "
    
    # todo frame tiene un layout
    layout = [ [b1, b2 ] , [b3, b4] ]
    
    frame_menu = sg.Frame("Menu", layout, font = ("chalkboard", 25), key = "FRAME_MENU", visible = True)
    
    return frame_menu


    Frecuencia_sidetable




def validar_ingreso():
    texto_password = sg.Text("Teclea la contraseña ",   font = ("chalkboard", 25))
    
    password = sg.Input(password_char = "*" ,          font = ("chalkboard", 25), key = 'INP_PASSWORD', text_color = "lightblue")
    
    b1 = sg.Button("Validar Ingreso",                 font = ("chalkboard", 25), key = 'BTN_PASSWORD',
                   pad = ((135, 100), (20, 20)) ,     button_color = "lightblue", border_width = 5 ) # image_filename = " ",
    imagen = sg.Image(filename = 'alumnos.png',      background_color = "lightblue", tooltip = 'migrantes' , size = (500, 200))
    
    layout =  [[texto_password, password ],
           [imagen] ,
           [b1]
           ]
                         
    #crear el frame - ventana para ingresar los datos del password
    frame_password = sg.Frame("Validar Ingreso", layout, font = ("chalkboard", 25), key = "FRAME_PASSWORD", visible = True)
                         
    return frame_password
                         
#sg.theme('DarkAmber')   # Add a touch of color
# llamar a la función validar ingreso para tener el frame que contiene todos los elementos para ingresar la contraseña
psw = validar_ingreso()
 
# All the stuff inside your window.
layout = [[psw]],            
            
# Create the Window
window = sg.Window('Emiliano Estrada ', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED : # if user closes window or clicks cancel
        break
    elif event == 'eel_PASSWORD':
         password = values[ "INP_PASSWORD" ]
         print("Cancel")
         if password == "eel":
             sg.popup('Bienvenido!, CCUMPLES CON LOS REQUISITOS PARA INGRESAR !', font = ('Helvetica', 30)) #, location=(0,0))
         else:
             sg.popup('Contraseña Incorrecta!', 'Adios!', font = ('Helvetica', 30))
    
    elif event == 'Cancel':
        print('Cancel')
        sg.popup('Hello From PySimpleGUI', 'This is the shortest GUI program ever!')
        
    elif event == 'Ok':
        print('You entered ', values[0], values[1])
    else:
        print("No hubo evento")

#********** "BTN GRABAR" ***********
    elif event == "BTN_GRABAR":
        #Abrir el archivo en forma de append - anade un registro al final del archivo
        with open("Mi_base.csv","a") as archivo
        # Sacar todos los valores ingresados en el INPUT_...
        Platllo = values["INPUT_PLATLLOS"]
        arma = values["INPUT_ARMAS"]
        Platllo = values["INPUT_PLATLLOS"]
        arma = values["INPUT_ARMAS"]
        
        raw = platillo + "," + arma + "," + estado + "," str (edad) + "\ln"
        
        #grabar el rengion
        archivo.write(raw)
        
    #***************"BTN_ESTADISTICAS"***************
    elif event == "BTN_ESTADISTICAS":
        Estadisticas()
        
    
    #*************** "BTN_ESTADISTICAS_FORMULARIO" ***********
        elif event == "BTN_ESTADISTICAS_FORMULARIO":
            estadisticas_formulario ()
            estadisticas_formulario()
            
        else:
            print(" no hubo evento")


        
        
    
window.close()








