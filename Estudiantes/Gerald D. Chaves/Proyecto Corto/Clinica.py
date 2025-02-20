import json
from collections import Counter

def cargar_datos(pacientes):
    with open(pacientes, "r", encoding="utf-8") as file:
        return json.load(file)
    
datos_json = cargar_datos('Estudiantes/Gerald D. Chaves/Proyecto Corto/clinica.json')
    

def generar_reporte_enfermedades(datos):
    #Le identidica al sistema que el indice 4 tiene las enfermedades por paciente.
    enfermedades = [fila[4] for fila in datos]
    #Hace el conteo por enfermedad
    conteo = Counter(enfermedades)
    print("\n Enfermedades por paciente:")
    for enfermedad, cantidad in conteo.items():
        print(f"{enfermedad}: {cantidad} pacientes")

def generar_reporte_medicamentos(datos):
   #Le identidica al sistema que el indice 5 tiene los medicamentos por paciente.
    medicamentos = [fila[5] for fila in datos]
    #Hace el conteo por medicamento
    conteo = Counter(medicamentos)
    print("\nMedicamentos por paciente:")
    for medicamento, cantidad in conteo.items():
        print(f"{medicamento}: {cantidad} pacientes")

def comparar_pacientes(datos, id1, id2):
    #compara las enfermedades entre el paciente 1 y el paciente 2
    enfermedades_p1 = set(fila[4] for fila in datos if fila[0] == id1)
    enfermedades_p2 = set(fila[4] for fila in datos if fila[0] == id2)
    comunes_enfermedades = enfermedades_p1.intersection(enfermedades_p2)
    
    #compara los medicamentos entre el paciente 1 y el paciente 2
    medicamentos_p1 = set(fila[5] for fila in datos if fila[0] == id1)
    medicamentos_p2 = set(fila[5] for fila in datos if fila[0] == id2)
    comunes_medicamentos = medicamentos_p1.intersection(medicamentos_p2)
    
    print("\nComparación de Pacientes:")
    if id1 != id2:
        if comunes_enfermedades:
            print('\nEnfermedades en común:')
            #Si no hay comparaciones, muestra ninguna
            print(f"Enfermedades en común: {', '.join(comunes_enfermedades) if comunes_enfermedades else 'Ninguna'}")
        else:
            print('\nNo tienen enfermedades en común.')
    else:
        print(f'No es posible hacer la comparativa entre el mismo paciente, utilice identificaciones diferentes por favor.')
        
    if id1 != id2:
        if comunes_enfermedades:
            print('\nEnfermedades en común:')
            #Si no hay comparaciones, muestra ninguna
            print(f"Medicamentos en común: {', '.join(comunes_medicamentos) if comunes_medicamentos else 'Ninguno'}")
        else:
            print('\nNo tienen enfermedades en común.')
    else:
        print(f'No es posible hacer la comparativa entre el mismo paciente, utilice identificaciones diferentes por favor.')
        


    
while True:
        print("\nOpciones:")
        print("1. Generar reporte de enfermedades")
        print("2. Generar reporte de medicamentos")
        print("3. Comparar dos pacientes")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("\n-------- Reporte de enfermedades --------")
            generar_reporte_enfermedades(datos_json)
        elif opcion == "2":
            print("\n-------- Reporte de medicamentos --------")
            generar_reporte_medicamentos(datos_json)
        elif opcion == "3":
            print("\n-------- Comparativa entre pacientes --------")
            id1 = input("Ingrese el ID del primer paciente: ")
            id2 = input("Ingrese el ID del segundo paciente: ")
            comparar_pacientes(datos_json, id1, id2)
        elif opcion == "4":
            print(f"\nSalida exitosa del programa, vuelva pronto.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

