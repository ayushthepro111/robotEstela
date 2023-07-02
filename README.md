### Robot Estela 
_____________________________________________________________________________________________________________________________________________________________________________
```
tiempo de importación
sistema de importación
solicitante de importación
importar navegador web
de búsqueda de importación de googlesearch
desde fecha y hora fecha de importación
desde fechahora fechahora de importación
importar sistema operativo


def principal():
    def delay_print(s):
        para c en s:
            sys.stdout.escribir (c)
            sys.stdout.flush()
            tiempo.dormir(0.1)
    URL = "https://openai.com/chatgpt"
    hoy = fecha.hoy()
    ahora = fechahora.ahora()
    dt = ahora.strftime("%H:%M:%S")
    # Mes, día y año textuales
    d2 = hoy.strftime("%B %d, %Y")
    

    delay_print("Bienvenido al chat GPT V2.0")
    preguntas = [
      investigador.Lista('p1',
                    mensaje="Por favor elija",
                    choice=["Califícanos","Visítanos","Salir", "Buscar-algo", "Cuál-es-la-fecha-hora"],
                ),
    ]
    respuestas = inquirer.prompt(preguntas)
    delay_print (respuestas["p1"])


    if respuestas["p1"] == "Califícanos":
        calificación = entrada ("\nIngrese la cantidad de estrellas en números: \n")
        retraso_imprimir("\n........\n")
        delay_print("\nGRACIAS\n")

    elif responde["p1"] == "Visítanos":
        webbrowser.open(url)
    
    
    elif responde["p1"] == "Salir":
        sys.exit()
    
    elif responde["p1"] == "Buscar-Algo":
        consulta = entrada("\nIngrese algún valor: \n")
        for i in search(query, tld="co.in", num=10, stop=10, pause=2):
            imprimir (yo)
            
    elif responde["p1"] == "Cuál-es-la-fecha-hora":
        imprimir("\nHoy es: \n", d2)
        imprimir("La hora es: ", dt)
    
    demás:
        imprimir("ERROR 404")
        
si __nombre__ == "__principal__":
    principal() 
```
_____________________________________________________________________________________________________________________________________________________________________________
