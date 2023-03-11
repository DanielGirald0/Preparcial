option = 1
empanadas = []
while option != 0:
    print('***** EMPANADAS EL CANIVAL *****')
    print('1. Ingresar empanada: ')
    print('2. Mostrar empanadas registradas ')
    print('3. buscar empabnada por ID ')
    print('4. Editar empanada ')
    print('5. Eliminar empanada ')
    print(' * Presione 0 para salir ')
    option = int(input('Escoja opcion: '))

    if(option == 1):
        empanada = {}
        empanada = [id] = int(input('Digite id de empanada: '))
        empanada = [nombre] = input('Digite nombre de empanada: ')
        empanada = [precio] = float(input('Digite precio de empanada: '))
        empanada = [popularidad] = int(input('Digite popularidad de empanada: '))
        empanada = [fechavencimiento] = input('Digite fecha de vencimiento de empanada: ')
        empanadas.append(empanada)
        print("empanadas registrada...")

    elif(option == 2):
        for empanada in empanadas:
            print(empanada)

    elif(option == 3):
        EmpanadaBuscada = int(input("Ingrese id de la empanada a buscarr: "))
        for empanada in empanadas:
            if(empanada['id'] == EmpanadaBuscada):
                print(f'Empanada encontrada {empanada}')
            else:
                print('sin empanada')

    elif(option == 4):
        EmpanadaBuscada = int(input("Ingrese id de la empanada para editar: "))
        for empanada in empanadas:
            if(empanada['id'] == EmpanadaBuscada):
                print(f"Precio anterior: {empanada['precio']}")
                empanada['precio']
                precioNuevo = float(input('digite el nuevo precio: '))
                empanada['precio']= precioNuevo 
            else:
                print('sin empanada')
                
    elif(option == 5):
        EmpanadaBuscada = int(input("IEliminar empanada por id "))
        for empanada in empanadas:
            if(empanada['id'] == EmpanadaBuscada):
                empanada.remove(empanadas)
                print('empanada encontrada y eliminada')
            else:
                print('sin empanada')

    elif(option == 0):
        pass
    else :
        print("Opcion invalida")

        