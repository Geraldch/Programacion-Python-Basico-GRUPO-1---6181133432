import json
from collections import defaultdict


pacientes = 'Estudiantes/Gerald D. Chaves/Proyecto Corto/clinica.json' 


def cargar_datos(pacientes):
    """
    Carga la información de los pacientes desde un archivo JSON.
    Se espera que el archivo contenga una lista de diccionarios.
    """
    try:
        with open(pacientes, "r", encoding="utf-8") as archivo:
            datos_pacientes = json.load(archivo)
                        # Si es un diccionario, obtenemos sus valores
            if isinstance(datos_pacientes, dict):
                lista_pacientes = list(datos_pacientes.values())
            else:
                lista_pacientes = datos_pacientes
            #En esta linea haremos que los datos se muestren ordenadamente para un mejor control visual
            print(json.dumps(datos_pacientes, indent=4, ensure_ascii=False))  # Solo para visualizar
            return datos_pacientes  # Devuelve los datos cargados
        #return datos_pacientes
    except FileNotFoundError:
        print(f"Error: El archivo {pacientes} no fue encontrado.")
        return []
    except json.JSONDecodeError:
        print("Error: El archivo JSON tiene un formato incorrecto.")
        return []
    


def generar_reporte_medicamentos(lista_pacientes):
    """
    Genera un reporte de los medicamentos recetados y cuenta cuántos pacientes son recetados por cada medicamento.
    """
    from collections import defaultdict
    reporte = defaultdict(int)
    
    for paciente in lista_pacientes:
        # Verificamos que paciente sea un diccionario
        if isinstance(paciente, dict):
            medicamentos = paciente.get("Medicamento", [])
            for medicamento in medicamentos:
                reporte[medicamento] += 1
        else:
            print(f"Advertencia: Se encontró un elemento no esperado: {paciente}")
    
    print("Reporte de Medicamentos Recetados:")
    for medicamento, cantidad in reporte.items():
        print(f"{medicamento}: {cantidad} pacientes")



    
datos_pacientes = []  # Variable global para almacenar los pacientes
    
while True:
    print('\n--- Menú de Análisis de Pacientes ---')
    print('1. Cargar data de los pacientes.')
    print('2. Reporte de Enfermedades.')
    print('3. Ver estudiante específico.')
    print('4. Salir')
    
    menu  = input('Ingrese una opción por favor: ')

    if menu == '1':
        print("\nEsta es la data de los pacientes registrados: ")
        datos_pacientes = cargar_datos(pacientes)  # Guarda los datos en la variable global
    elif menu == '2':
        print("\nReporte de Enfermedades por paciente registrados: ")
        if datos_pacientes:  # Verifica que la lista no esté vacía
            generar_reporte_medicamentos(datos_pacientes)
        else:
            print("Primero debe cargar los datos de los pacientes (Opción 1).")
    elif menu == '3':
        print(f"\nVer estudiante específico.")
    elif menu == '4':
        print(f"\nSalida exitosa del programa.")
        break    
    else:
        print(f"\nOpción no válida, intente de nuevo.")    

