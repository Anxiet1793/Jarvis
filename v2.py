import subprocess
import pywhatkit
import speech_recognition as sr
import pyttsx3
import pruebaBing
import os
import webbrowser
import pruebaBuscador
from buscarArchivo import buscarArchivo
import bingCodigo
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def Asistente():
    activado = True
    hablar("Hola Soy Jarvis,¿En qué puedo ayudarte?")
    while True:
        if not activado:
            if not escuchar_palabra_activacion():
                return ""
        else:
            while True:
                if activarComando() is True:
                    comando = escuchar_comando()
                    if comando == "":
                        hablar("No detecto ningún comando..")
                    elif 'salir' in comando:
                        hablar("Nos vemos amo")
                        return False
                    elif 'conectar con bin' in comando:
                        hablar("Te conecto con bing")
                        pruebaBing.asyncio.run(pruebaBing.main())
                    elif 'código' in comando:
                        hablar("Te conecto con bing para para creación de código")
                        bingCodigo.asyncio.run(bingCodigo.main())

                    elif 'reproduce' in comando:
                        cancion = comando.replace('reproduce', '')
                        hablar("Reproduciendo " + cancion)
                        pywhatkit.playonyt(cancion)
                    elif 'apagar computadora' in comando:
                        os.system('shutdown -s')
                    elif 'busca' in comando:
                        pagina = escuchar_comando()
                        webbrowser.open('https://www.google.com/search?q=' + pagina)
                    ###elif 'abre' in comando:
                    ###pagina = escuchar_comando()
                    ###PruebaBuscador.buscar(pagina)
                    elif 'abre' in comando:
                        hablar("Que necesitas abrir amo")
                        archivo=escuchar_comando()
                        hablar(f"Buscando {archivo}")
                        archivoEncontrado = buscarArchivo(archivo)
                        subprocess.Popen(f'start {archivoEncontrado}', shell=True)

                        if archivoEncontrado is None:
                            hablar("No se encontró el archivo.")
                        else:
                            hablar("abriendo archivo")
                    elif 'envía un mensaje' in comando:
                        hablar("Claro AMO ingrese el numero de télefono")
                        phone = str(input("Ingrese el Numero de telefono: "))
                        mensaje = escuchar_comando()
                        pywhatkit.sendwhatmsg_instantly(phone, mensaje)
                        hablar("¿Desea enviar otro mensaje?")
                        interrogante = escuchar_comando()
                        if "sí" in interrogante:
                            mensaje = escuchar_comando()
                            pywhatkit.sendwhatmsg_instantly(phone, mensaje)
                            hablar("¿Desea enviar otro mensaje?")
                            interrogante = escuchar_comando()
                        else:
                            hablar("Entiendo que ya no quieres enviar otro mensaje")

                    else:
                        hablar("No entendí tu comando.")



def escuchar(a):
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=10)
            texto = r.recognize_google(audio, language=a)
            return texto.lower()
        except sr.UnknownValueError:
            return ""
        except sr.WaitTimeoutError:
            return ""

def activarComando():
    hablar("pip")
    texto = escuchar('en')
    if 'jarvis' in texto:
        return True
    else:
        print("no entendi")
        return False

def escuchar_palabra_activacion():
    hablar("holi") #no se usa por ahora
    texto = escuchar()
    if 'jarvis' in texto:
        return True
    else:
        print("no entendi")
        return False

def escuchar_comando():
    hablar("pi")
    texto = escuchar('es')
    if texto != "":
        print("comando detected..." + texto)
    return texto

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

Asistente()