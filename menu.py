import helpers
import database as db


def iniciar():
    contador = 1
    polinomio = {}
    while True:
        helpers.limpiar_pantalla()
        
        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Mostrar polinomios  ")
        print(f"[2] Añadir polinomio (p{contador})")
        print("[3] Modificar término   ")
        print("[4] Añadir término      ")
        print("[5] Borrar término      ")
        print("[6] Sumar polinomios    ")
        print("[7] Restar polinomios   ")
        print("[8] Multiplicar polinomios")
        print("[9] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando polinomios...\n")
            for i in range(contador-1):
                print("p{} = {}".format(i+1, polinomio[f"p{i+1}"].mostrar()))

        elif opcion == '2':
            print(f"Añadiendo el polinomio p{contador}...\n")
            polinomio[f"p{contador}"] = db.Polinomio()
            polinomio[f"p{contador}"].agregar_termino(helpers.leer_numero(0, 1000, "Exponente del término: "), 
                                                      helpers.leer_numero(-1000, 1000, "Coeficiente del término: "))
            helpers.limpiar_pantalla()
            while True:
                if helpers.pedir_entrada_si_o_no(mensaje="Desea añadir otro término al polinomio p{}?".format(contador)) == False:
                    break
                else:
                    exp = helpers.leer_numero(0, 1000, "Exponente del término: ")
                    if polinomio[f"p{contador}"].existe_termino(exp) == True:
                        helpers.limpiar_pantalla()
                        print("Ya existe un término con el exponente ingresado.\n")
                    else:
                        polinomio[f"p{contador}"].agregar_termino(exp, helpers.leer_numero(-1000, 1000, "Coeficiente del término: "))
                        helpers.limpiar_pantalla()
            
            print(f"p{contador} añadido correctamente.")
            contador += 1

        elif opcion == '3':
            print("Modificando término...\n")
            polinomios = helpers.leer_numero(1, contador-1, "Que polinomio desea modifcar? (Introduzca solo el número del polinomio 1, 2, 3, etc.):", 
                                             mensaje_error="No existe un polinomio con el número ingresado.\n")
            if polinomios == None:
                input("Presiona ENTER para continuar...")
                continue
            helpers.limpiar_pantalla()
            termino = helpers.leer_numero(0, 1000, "Exponente del término a modicar: ")
            if polinomio[f"p{polinomios}"].existe_termino(termino) == True:
                polinomio[f"p{polinomios}"].modificar_termino(termino, helpers.leer_numero(-1000, 1000, "Nuevo coeficiente del término: "))
                helpers.limpiar_pantalla()
                print(f"p{polinomios} modificado correctamente.")
            else:
                print("No existe un término con el exponente ingresado.")

        elif opcion == '4':
            print("Añadiendo termino...\n")
            polinomios = helpers.leer_numero(1, contador-1, "Que polinomio desea modifcar? (Introduzca solo el número del polinomio 1, 2, 3, etc.):", 
                                             mensaje_error="No existe un polinomio con el número ingresado.\n")
            if polinomios == None:
                input("Presiona ENTER para continuar...")
                continue
            helpers.limpiar_pantalla()
            while True:
                if helpers.pedir_entrada_si_o_no(mensaje="Desea añadir otro término al polinomio p{}?".format(polinomios)) == False:
                    break
                else:
                    exp = helpers.leer_numero(0, 1000, "Exponente del término: ")
                    if polinomio[f"p{polinomios}"].existe_termino(exp) == True:
                        helpers.limpiar_pantalla()
                        print("Ya existe un término con el exponente ingresado.\n")
                    else:
                        polinomio[f"p{polinomios}"].agregar_termino(exp, helpers.leer_numero(-1000, 1000, "Coeficiente del término: "))
                        helpers.limpiar_pantalla()
            print(f"p{polinomios} modificado correctamente.")

        elif opcion == '5':
            print("Borrando un término...\n")
            polinomios = helpers.leer_numero(1, contador-1, "Que polinomio desea modifcar? (Introduzca solo el número del polinomio 1, 2, 3, etc.):",
                                                mensaje_error="No existe un polinomio con el número ingresado.\n")
            if polinomios == None:
                input("Presiona ENTER para continuar...")
                continue
            helpers.limpiar_pantalla()
            termino = helpers.leer_numero(0, 1000, "Exponente del término a eliminar: ")
            if polinomio[f"p{polinomios}"].existe_termino(termino) == True:
                polinomio[f"p{polinomios}"].eliminar_termino(termino)
                helpers.limpiar_pantalla()
                print(f"Término eliminado correctamente.")
            else:
                print("No existe un término con el exponente ingresado.")

        elif opcion == '6':
            print("Sumando polinomios...\n")
            polinomio1 = helpers.leer_numero(1, contador-1, "Que polinomio desea sumar? (Introduzca solo el número del polinomio 1, 2, 3, etc.):",
                                                mensaje_error="No existe un polinomio con el número ingresado.\n")
            if polinomio1 == None:
                input("Presiona ENTER para continuar...")
                continue
            helpers.limpiar_pantalla()
            polinomios2 = helpers.leer_numero(1, contador-1, "Que polinomio desea sumar? (Introduzca solo el número del polinomio 1, 2, 3, etc.):",
                                                mensaje_error="No existe un polinomio con el número ingresado.\n")
            if polinomios2 == None:
                input("Presiona ENTER para continuar...")
                continue
            helpers.limpiar_pantalla()
            print(f"p{polinomio1} + p{polinomios2} = {polinomio[f'p{polinomio1}'].sumar(polinomio[f'p{polinomios2}']).mostrar()}")

        elif opcion == '7':
            print("Restando polinomios...\n")
            polinomio1 = helpers.leer_numero(1, contador-1, "Que polinomio desea restar? (Introduzca solo el número del polinomio 1, 2, 3, etc.):",
                                                mensaje_error="No existe un polinomio con el número ingresado.\n")
            if polinomio1 == None:
                input("Presiona ENTER para continuar...")
                continue
            helpers.limpiar_pantalla()
            polinomios2 = helpers.leer_numero(1, contador-1, "Que polinomio desea restar? (Introduzca solo el número del polinomio 1, 2, 3, etc.):",
                                                mensaje_error="No existe un polinomio con el número ingresado.\n")
            if polinomios2 == None:
                input("Presiona ENTER para continuar...")
                continue
            helpers.limpiar_pantalla()
            print(f"p{polinomio1} - p{polinomios2} = {polinomio[f'p{polinomio1}'].restar(polinomio[f'p{polinomios2}']).mostrar()}")

        elif opcion == '8':
            print("Multiplicando polinomios...\n")
            polinomio1 = helpers.leer_numero(1, contador-1, "Que polinomio desea multiplicar? (Introduzca solo el número del polinomio 1, 2, 3, etc.):",
                                                mensaje_error="No existe un polinomio con el número ingresado.\n")
            if polinomio1 == None:
                input("Presiona ENTER para continuar...")
                continue
            helpers.limpiar_pantalla()
            polinomios2 = helpers.leer_numero(1, contador-1, "Que polinomio desea multiplicar? (Introduzca solo el número del polinomio 1, 2, 3, etc.):",
                                                mensaje_error="No existe un polinomio con el número ingresado.\n")
            if polinomios2 == None:
                input("Presiona ENTER para continuar...")
                continue
            helpers.limpiar_pantalla()
            print(f"p{polinomio1} * p{polinomios2} = {polinomio[f'p{polinomio1}'].multiplicar(polinomio[f'p{polinomios2}']).mostrar()}")

        elif opcion == '9':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")