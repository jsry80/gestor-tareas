# Gestor de Tareas - Proyecto para aprender Git
# Autor: Alexander Rey

tareas = []

def agregar_tarea(nombre):
    tareas.append({"nombre": nombre, "completada": False})
    print(f"✅ Tarea '{nombre}' agregada")

def listar_tareas():
    if not tareas:
        print("No hay tareas pendientes")
        return
    for i, tarea in enumerate(tareas, 1):
        estado = "✔" if tarea["completada"] else "○"
        print(f"{i}. [{estado}] {tarea['nombre']}")

if __name__ == "__main__":
    agregar_tarea("Aprender Git")
    agregar_tarea("Configurar PyCharm")
    listar_tareas()