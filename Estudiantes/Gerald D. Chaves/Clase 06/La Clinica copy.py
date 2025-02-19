import json

def cargar_datos(nombre_archivo="clinica.json"):
    """
    Carga la información de los pacientes desde un archivo JSON.
    Se espera que el archivo contenga una lista de diccionarios.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        return []
    except json.JSONDecodeError:
        print("Error: El archivo JSON tiene un formato incorrecto.")
        return []

def reporte_enfermedades(pacientes):
    """
    Genera un reporte de la cantidad de pacientes por enfermedad.
    """
    conteo = {}
    for paciente in pacientes:
        enfermedad = paciente.get("enfermedad", "No especificada")
        conteo[enfermedad] = conteo.get(enfermedad, 0) + 1
    print("\n--- Reporte de Enfermedades ---")
    for enfermedad, cantidad in conteo.items():
        print(f"- {enfermedad}: {cantidad} paciente(s)")

def reporte_medicamentos(pacientes):
    """
    Genera un reporte de la cantidad de pacientes por medicamento recetado.
    """
    conteo = {}
    for paciente in pacientes:
        medicamento = paciente.get("medicamento", "No especificado")
        conteo[medicamento] = conteo.get(medicamento, 0) + 1
    print("\n--- Reporte de Medicamentos ---")
    for medicamento, cantidad in conteo.items():
        print(f"- {medicamento}: {cantidad} paciente(s)")

def comparar_pacientes(pacientes, id1, id2):
    """
    Compara dos pacientes usando sus identificaciones y muestra:
    - Las enfermedades que tienen en común.
    - Los medicamentos que toman en común.
    
    Se asume que cada paciente tiene una única enfermedad y un único medicamento.
    """
    paciente1 = next((p for p in pacientes if p.get("identificacion") == id1), None)
    paciente2 = next((p for p in pacientes if p.get("identificacion") == id2), None)
    
    if not paciente1 or not paciente2:
        print("Error: Una o ambas identificaciones no fueron encontradas.")
        return
    
    print(f"\n--- Comparación entre paciente {id1} y paciente {id2} ---")
    
    # Comparación de enfermedades
    enfermedad1 = paciente1.get("enfermedad", "No especificada")
    enfermedad2 = paciente2.get("enfermedad", "No especificada")
    if enfermedad1 == enfermedad2:
        print(f"Enfermedad en común: {enfermedad1}")
    else:
        print("No comparten la misma enfermedad.")
    
    # Comparación de medicamentos
    medicamento1 = paciente1.get("medicamento", "No especificado")
    medicamento2 = paciente2.get("medicamento", "No especificado")
    if medicamento1 == medicamento2:
        print(f"Medicamento en común: {medicamento1}")
    else:
        print("No toman el mismo medicamento.")

def menu():
    """
    Función principal que muestra el menú, carga los datos y procesa las operaciones solicitadas por el usuario.
    """
    pacientes = cargar_datos()
    if not pacientes:
        return

    while True:
        print("\n--- Menú de Análisis de Pacientes ---")
        print("1. Generar reporte de enfermedades")
        print("2. Generar reporte de medicamentos")
        print("3. Comparar 2 pacientes")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            reporte_enfermedades(pacientes)
        elif opcion == "2":
            reporte_medicamentos(pacientes)
        elif opcion == "3":
            id1 = input("Ingrese la identificación del primer paciente: ").strip()
            id2 = input("Ingrese la identificación del segundo paciente: ").strip()
            comparar_pacientes(pacientes, id1, id2)
        elif opcion == "4":
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()


