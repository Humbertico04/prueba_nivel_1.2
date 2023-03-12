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
        print("[1] Mostrar Polinomios ")
        print("[2] Añadir polinomio   ")
        print("[4] Modificar un cliente")
        print("[5] Borrar un cliente   ")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando polinomios...\n")
            for i in range(contador-1):
                print("p{} = {}".format(i+1, polinomio[f"p{i+1}"].mostrar()))

        elif opcion == '2':
            print(f"Añadiendo el polinomioo p{contador}...\n")
            polinomio[f"p{contador}"] = db.Polinomio()
            polinomio[f"p{contador}"].agregar_termino(helpers.leer_numero(-1000, 1000, "Exponente del término: "), 
                                                      helpers.leer_numero(-1000, 1000, "Coeficiente del término: "))


            
            print(f"p{contador} añadido correctamente.")
            contador += 1

        # elif opcion == '3':
        #     print("Añadiendo un cliente...\n")

        #     dni = None
        #     while True:
        #         dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
        #         if helpers.dni_valido(dni, db.Clientes.lista):
        #             break

        #     nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
        #     apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
        #     db.Clientes.crear(dni, nombre, apellido)
        #     print("Cliente añadido correctamente.")

        # elif opcion == '4':
        #     print("Modificando un cliente...\n")
        #     dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
        #     cliente = db.Clientes.buscar(dni)
        #     if cliente:
        #         nombre = helpers.leer_texto(
        #             2, 30, f"Nombre (de 2 a 30 chars) [{cliente.nombre}]").capitalize()
        #         apellido = helpers.leer_texto(
        #             2, 30, f"Apellido (de 2 a 30 chars) [{cliente.apellido}]").capitalize()
        #         db.Clientes.modificar(cliente.dni, nombre, apellido)
        #         print("Cliente modificado correctamente.")
        #     else:
        #         print("Cliente no encontrado.")

        # elif opcion == '5':
        #     print("Borrando un cliente...\n")
        #     dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
        #     print("Cliente borrado correctamente.") if db.Clientes.borrar(
        #         dni) else print("Cliente no encontrado.")

        elif opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")