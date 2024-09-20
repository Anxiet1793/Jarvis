import os
import json

def listar_archivos(ruta):
    lista_archivos = []
    for raiz, dirs, archivos in os.walk(ruta):
        for archivo in archivos:
            lista_archivos.append(os.path.join(raiz, archivo))
    lista_archivos.sort()
    return lista_archivos

def guardar_archivos(archivos, nombre_archivo):
    with open(nombre_archivo, 'w') as f:
        json.dump(archivos, f)

def cargar_archivos(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        return json.load(f)
nombre_archivo = "archivos.json"
# Cargar los archivos
archivos = cargar_archivos(nombre_archivo)
ruta_inicial = "/"  # Puedes cambiar esto a la ruta que desees
# Listar los archivos y guardarlos
#archivos = listar_archivos(ruta_inicial)
#guardar_archivos(archivos, nombre_archivo)

def buscar_palabras(palabras, lista_archivos):
    archivos_encontrados = []
    for archivo in lista_archivos:
        if all(palabra in archivo for palabra in palabras):
            archivos_encontrados.append(archivo)
    return archivos_encontrados

extensiones = [
    ".txt", ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".csv", ".doc", ".docx",
    ".xls", ".xlsx", ".ppt", ".pptx", ".xml", ".html", ".htm", ".php",
    ".py", ".js", ".java", ".c", ".cpp", ".cs", ".h", ".json",
    ".mp3", ".mp4", ".flv", ".avi", ".mov", ".wmv",
    ".zip", ".tar", ".gz", ".bz2",
    ".ico", ".svg",
]
# Buscar las palabras en los archivos
archivos_encontrados = buscar_palabras(palabras, archivos)
for archivo in archivos_encontrados:
    print(archivo)