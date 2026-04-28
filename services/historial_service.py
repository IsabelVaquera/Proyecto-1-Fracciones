"""
Módulo de servicios para la persistencia de datos.

Maneja la lectura y escritura del historial de operaciones en
un archivo de texto plano (JSON) para mantener el estado entre sesiones.
"""

import json
import os

RUTA = "datos/historial.json"

def cargar_historial() -> list:
    """
    Lee el archivo JSON y devuelve su contenido como una lista de Python.
    Si el archivo no existe o está corrupto, devuelve una lista vacía.
    """
    if os.path.exists(RUTA):
        try:
            with open(RUTA, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def guardar_historial(historial: list) -> None:
    """
    Sobrescribe el archivo JSON con la lista actualizada del historial.
    Crea el directorio 'datos' automáticamente si no existe.
    """
    if not os.path.exists("datos"):
        os.makedirs("datos")

    with open(RUTA, "w", encoding="utf-8") as f:
        json.dump(historial, f, indent=4, ensure_ascii=False)

def limpiar_historial() -> None:
    """
    Vacía el archivo del historial sobrescribiéndolo con una lista vacía.
    """
    guardar_historial([])