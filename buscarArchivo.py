import os
import subprocess
def buscarArchivo(nombreArchivo):
    extensiones = [
        ".txt", ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".csv", ".doc", ".docx",
        ".xls", ".xlsx", ".ppt", ".pptx", ".xml", ".html", ".htm", ".php",
        ".py", ".js", ".java", ".c", ".cpp", ".cs", ".h", ".json",
        ".mp3", ".mp4", ".flv", ".avi", ".mov", ".wmv",
        ".zip", ".tar", ".gz", ".bz2",
        ".ico", ".svg",
    ]
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.startswith(nombreArchivo) and file.endswith(tuple(extensiones)):
                print(os.path.abspath(os.path.join(root, file)))
                return os.path.abspath(os.path.join(root, file))

    return None

def busqueda_binaria(nombre_archivo, extensiones):
    archivos = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(tuple(extensiones)):
                archivos.append(os.path.join(root, file))
    archivos.sort()
    inicio = 0
    fin = len(archivos) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        archivo_medio = archivos[medio]
        if archivo_medio < nombre_archivo:
            inicio = medio + 1
        elif archivo_medio > nombre_archivo:
            fin = medio - 1
        else:
            return archivo_medio
    return None



