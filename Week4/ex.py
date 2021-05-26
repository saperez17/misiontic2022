devs = []

def create_dev():
    dev = {'cc':0,'nombre':'','salario':0}
    dev['nombre'] = input('Escriba el nombre del dev: ')
    dev['cc'] = int(input('Escriba la cedula del dev: '))
    dev['salario'] = int(input('Escriba el salario del dev: '))
    devs.append(dev)

def list_devs():
    print('-------------------------------')
    print('--------Listado de devs--------')
    for dev in devs:
        print(f"Cedula: {dev['cc']}, Nombre: {dev['nombre']}, Salario: {dev['salario']}")

def search_dev_by_id():
    cedula = int(input('Ingrese la cedula \n'))
    dev = None
    for developer in devs:
        if (cedula==developer['cc']):
            dev = developer
    if dev!=None:
        print(f"Desarrollador encontrado. Nombre: {dev['nombre']}, Salario: {dev['salario']}")
    else:
        print("Desarrollador no encontrado")

def search_dev_by_str():
    starting_str = input('Ingrese una cadena de busqueda:')
    matching_devs = []
    for dev in devs:
        if starting_str in dev['nombre']:
            matching_devs.append(dev)
    if len(matching_devs)!=0:
        print('Estos desarrolladores coinciden con la cadena de busqueda ingresada. \n')
        for developer in matching_devs:
            print(f"Desarrollador encontrado. Nombre: {developer['nombre']}, Cedula: {developer['cc']}, Salario: {developer['salario']}")
    else:
        print('No se encontraron coincidencias.')

def set_options(option):
    if option == '1':
        create_dev()
    elif option == '2':
        list_devs()
    elif option == '3':
        search_dev_by_id()
    elif option == '4':
        search_dev_by_str()
    else:
        exit()

def run():
    print("""
    Escoge la accion que deseas realizar:
    1- Agregar un dev
    2- Listar Devs
    3- Buscar desarrollador por cedula
    4- Buscar desarrollador(es) por nombre
    9- Salir
    """)
    option = input('Digita el número de la opción: ')
    set_options(option)
    run()

if __name__ == '__main__':
    run()