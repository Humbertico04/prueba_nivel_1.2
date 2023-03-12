import os
import platform

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto
        
def leer_numero(min=0, max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        try:
            numero = input("> ")
            if int(numero) >= min and int(numero) <= max:
                return int(numero)
        except ValueError:
            pass

def pedir_entrada_si_o_no(mensaje=None):
    print(mensaje) if mensaje else None
    SI = ("s", "si", "y", "yes", "1")
    """Por defecto, toda respuesta no comprendida será NO"""
    try:
        return input("> ").lower() in SI
    except:
        return False
