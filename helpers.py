import os
import platform

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def leer_numero(min=0, max=100, mensaje=None, mensaje_error=None):
    print(mensaje) if mensaje else None
    while True:
        try:
            numero = input("> ")
            if int(numero) >= min and int(numero) <= max:
                return int(numero)
            else:
                print(mensaje_error) if mensaje_error else None
                if mensaje_error:
                    break       
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
