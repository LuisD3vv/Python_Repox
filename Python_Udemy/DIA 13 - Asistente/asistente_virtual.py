import pyttsx3 # convertir texto a voz con engine de esta misma biblioteca
import speech_recognition as sr # para reconocimiento y transformacion de voz a texto y viceversa
import pywhatkit # 
import yfinance as yf
import pyjokes
import webbrowser #buscar
import datetime # .now es para horas y .today para fechas.
import wikipedia

# Cuidado con el interprete,segun el que estemos usando estaran o no instaladas als dependencias.

# Escuchar nuestro microfono y devolver el audio como texto

def transformar_audio_en_texto():
    # almacenar el recognizer en variable
    r = sr.Recognizer()
    
    # configurar el microfono
    with sr.Microphone() as origen:
        
        # tiempo de espera
        r.pause_threshold = 0.8
        
        # informar que comenzo la grabacion
        print("Ya puedes hablar.")
        
        # guardar lo que escuche como audio
        audio = r.listen(origen)
        
        try:
            # buscar en google
            pedido = r.recognize_bing(audio,language="es-mx")
            
            # Prueba de que pudo ingresar y tranformar el texto
            print(f"Dijiste: {pedido}")
            # devolver pedido
            return pedido
        # en caso de no lograr la busquda
        except sr.UnknownValueError():
            
            # Prueba de que no comprendio el audio
            print("ups, no hay servicio")
            # devolver error
            return "sigo esperando"
        # en caso de no resolver el pedido
        except sr.RequestError:
            print("ups, no se comprendio")
            # devolver error
            return "sigo esperando"
        # error inesperado
        except:
            print("ups, algo salio mal")
            # devolver error
            return "sigo esperando"

# Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    #engine.setProperty("voice") # moficar con mas opciones de voz
    
    # pronuncie el mensaje
    engine.say(mensaje)
    engine.runAndWait()

# opciones de voces / pendiente

# informar el dia de la semana()
def pedir_dia():
    # crear la variable con datos de hoy
    dia = datetime.date.today()
    
    # crear una variable para el dia de semana
    
    dia_semana = dia.weekday()
    
    # diccionario con os nombres de lops dias
    calendario = {0:'Lunes',
                1:'Martes',
                2:'Miercoles',
                3:'Jueves',
                4:'Viernes',
                5:'Sabado',
                6:'Domingo'}
    hablar(f"El dia de hoy es {calendario[dia_semana]}")

def pedir_hora():
    # crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    # pueda decir la hora
    hablar(hora)

def saludo_inicial():
    # crear variable con datos de dia
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas Noches"
    elif  6 <= hora.hour < 13:
        momento = "Buenas Dias"
    else:
        momento = "Buenas Tardes"
    # saludarnos
    hablar(f"{momento}, soy Ricardo, en que puedo servirte?")

def pedir():
    # activar saludo inicial
    saludo_inicial()
    
    # variable de corte
    comenzar = True
    # loop central
    while comenzar:
        
        # activar el micro y guardar en variable
        
        pedido = transformar_audio_en_texto().lower()
        
        if "abrir youtube" in pedido:
            hablar("Con gusto, estoy abriendo youtube ahora mismo.")
            webbrowser.open('https://www.youtube.com')
            continue
        elif "abrir navegador" in pedido:
            hablar("Con gusto, estoy abriendo el navegador para ti.")
            webbrowser.open("https://www.google.com")
            continue
        elif "que dia es hoy" in pedido:
            pedir_dia()
            continue
        elif "que hora es" in pedido:
            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("Buscando en wikipedia")
            pedido = pedido.replace("busca en wikipedia","")
            wikipedia.set_lang("es") # idioma
            resultado = wikipedia.summary(pedido,sentences=1) # cuantos parrafos leera
            hablar("Segun wikipedia:")
            hablar(resultado)
            continue
        elif "busca en internet" in pedido:
            pedido = pedido.replace("busca en internet",'')
            hablar("En eso estoy")
            pywhatkit.search(pedido)
            hablar("esto es lo que he encontrado")
            continue
        elif 'reproducir' in pedido:
            hablar("buena idea, ya mismo lo pongo")
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones':
            accion = pedido.split('de')[-1].strip()
            cartera = {"apple":'APPL',
                    "amazon":"AMZN",
                    'google':"GOOGL",}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f"La encontre, el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("Perdon, no he encontrado la accion que me solicitaste")
        elif 'adios' in pedido:
            hablar("por el momento me voy,estoy disponible en cualquier momento.")
            break