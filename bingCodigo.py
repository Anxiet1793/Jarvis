import os
import asyncio
from sydney import SydneyClient
import datetime
import speech_recognition as sr
import pyttsx3
import subprocess

# Abre el cmd en segundo plano y escribe el comando

#cookie _U se recoge del buscador edge
#abriendo bing chat previamente logeado apretando F12
#accediendo a cookies en la pestaña de almacenamiento
#Y buscando la que diga _U luego copia el valor y se pega entre las <>
os.environ["BING_U_COOKIE"] = "<12Efcnb7ydicJubOwsw826JJKha7htsV8Cq74SBiGM8ctWHNw87IRwdeAhpzSCVW8cLaiMnmCJ-SotaG6JkpRmn9GlcDoROdm0vDKwsINn8h2jVpnbcpqchVhdF8nzv3MTC5qxN0zbNcMzgIbdEh8nsfGsM_9Lhc3boxGYg_fbBuEDXU7j7RZMrf1bF7CBR3ur4OA9F7GVATwRse7EUsMhpW0Hhfo4MRpt-qtcgx7SBA>"
fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d") # Formato YYYY-MM-DD
#Falta agregar los cambios de caracteristicas al bing segun conveniencia preciso-creativo-equilivadro
# Crear el nombre del archivo basado en la fecha actual

nombreArchivo2 = f"{fecha_actual}codigo.txt"
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
lenguaje=""
async def main() -> None:
    async with SydneyClient(style="PRECISE") as sydney:
        while True:
            respuestas=[]
            hablar("conectado AMO")
            prompt = escuchar_comando()
            if "python" in prompt:
                lenguaje=".py"
            elif "java" in prompt:
                lenguaje=".java"
            elif "html" in prompt:
                lenguaje=".html"
            elif prompt == "resetear":
                await sydney.reset_conversation()
                continue
            elif "salir" in prompt:
                break
            print("Bing: ", end="", flush=True)
            response = await sydney.ask(prompt)
            response_str = str(response)  # Convertir response a cadena

            with open(nombreArchivo2, 'a', encoding='utf-8') as file:
                file.write(response_str + "\n")

            a=cambiar_extension(nombreArchivo2, lenguaje)
            #subprocess.Popen(['start', 'cmd', '/c', f'start {a} '])
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()
def escuchar_comando():
    with sr.Microphone() as source:
        hablar("pi")
        r.adjust_for_ambient_noise(source, duration=1)  # ajusta el ruido de fondo
        audio = r.listen(source)


    try:
        texto = r.recognize_google(audio, language='es')
        print("Buscando...." + texto)
        return texto.lower()  # convertimos todo a minuscula
    except sr.UnknownValueError:
        return ""


def cambiar_extension(nombre_archivo, nueva_extension):
    nombre_base = os.path.splitext(nombre_archivo)[0]
    nuevo_nombre = nombre_base + nueva_extension
    os.rename(nombre_archivo, nuevo_nombre)

if __name__ == "__main__":
    asyncio.run(main())