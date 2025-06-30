"""
Notas:
• Está prohibido el uso de las funciones print() e input() dentro de las clases (capricho del profesor). Se
pueden realizar funciones específicas (no métodos) para imprimir la información por pantalla.
• Está permitido el uso del módulo datetime, para gestionar las fechas.

1) Crear una clase Tarea con atributos como nombre, descripción, fecha de vencimiento y prioridad.
Implementar métodos para marcar como completa, modificar fecha de vencimiento y prioridad. Se
pueden agregar más atributos y/o métodos que crean convenientes.
2) Crear una clase Evento con atributos como nombre, descripción, ubicación, fecha y duración.
Implementar métodos para modificar fecha, duración o ubicación. Se pueden agregar más atributos y/o
métodos que crean convenientes.
3) Crear una clase Agenda que utilice los objetos de la clase Tarea y Evento de los ejercicios anteriores.
Implementar métodos para agregar y eliminar tareas y eventos. Listar las tareas por orden de prioridad y
por orden de fecha de vencimiento. Listar eventos por fecha o por ubicación. Se pueden agregar más
atributos y/o métodos que crean convenientes.
4) Realizar un pequeño programa que permita al usuario cargar tareas y eventos en la agenda, marcar Tareas
como realizadas y Listar Tareas pendientes (por fecha o por prioridad) listar eventos, y listar tareas y/o
eventos de un día. 
"""
from datetime import date, datetime, timedelta

# 1)
class Tarea:
    def __init__(self, nombre: str, descripcion: str, fecha_vencimiento: date, prioridad: int):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.prioridad = prioridad
        self.completa = False

    def marcar_completa(self):
        self.completa = True
    
    def marcar_incompleta(self):
        self.completa = False
    
    def modificar_fecha(self, nueva_fecha: date):
        self.fecha_vencimiento = nueva_fecha
    
    def modificar_prioridad(self, nueva_prioridad: int):
        self.prioridad = nueva_prioridad
    
    def modificar_descripcion(self, nueva_descripcion: str):
        self.descripcion = nueva_descripcion
    
    def modificar_nombre(self, nuevo_nombre: str):
        self.nombre = nuevo_nombre
    
    def obtener_info(self):
        estado = "Completa" if self.completa else "Incompleta"
        return f"Tarea: {self.nombre}\nDescripción: {self.descripcion}\nVencimiento: {self.fecha_vencimiento}\nPrioridad: {self.prioridad}\nEstado: {estado}"
    
    def obtener_prioridad(self):
        return self.prioridad

    def obtener_fecha_vencimiento(self):
        return self.fecha_vencimiento

# 2)
class Evento:
    def __init__(self, nombre: str, descripcion: str, ubicacion: str, fecha: datetime, duracion: timedelta):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.fecha = fecha
        self.duracion = duracion

    def modificar_fecha(self, nueva_fecha: datetime):
        self.fecha = nueva_fecha

    def modificar_duracion(self, nueva_duracion: timedelta):
        self.duracion = nueva_duracion

    def modificar_ubicacion(self, nueva_ubicacion: str):
        self.ubicacion = nueva_ubicacion

    def modificar_nombre(self, nuevo_nombre: str):
        self.nombre = nuevo_nombre

    def modificar_descripcion(self, nueva_descripcion: str):
        self.descripcion = nueva_descripcion

    def obtener_info(self):
        return (f"Evento: {self.nombre}\n", f"Descripción: {self.descripcion}\n", f"Ubicación: {self.ubicacion}\n", f"Fecha: {self.fecha}\n", f"Duración: {self.duracion}")
    
    def obtener_fecha(self):
        return self.fecha

    def obtener_ubicacion_minusculas(self):
        return self.ubicacion.lower()

# 3)

class Agenda:
    def __init__(self):
        self.tareas = []
        self.eventos = []

    def agregar_tarea(self, tarea: Tarea):
        self.tareas.append(tarea)
    
    def eliminar_tarea(self, nombre: str):
        tareas_a_mantener = []
        for tarea in self.tareas:
            if tarea.nombre != nombre:
                tareas_a_mantener.append(tarea)
        self.tareas = tareas_a_mantener
    
    def agregar_evento(self, evento: Evento):
        self.eventos.append(evento)
    
    def eliminar_evento(self, nombre: str):
        eventos_a_mantener = []
        for evento in self.eventos:
            if evento.nombre != nombre:
                eventos_a_mantener.append(evento)
        self.eventos = eventos_a_mantener
    
    def listar_tareas_por_prioridad(self):
        return sorted(self.tareas, key=Tarea.obtener_prioridad)

    def listar_tareas_por_fecha(self):
        return sorted(self.tareas, key=Tarea.obtener_fecha_vencimiento)

    def listar_eventos_por_fecha(self):
        return sorted(self.eventos, key=Evento.obtener_fecha)

    def listar_eventos_por_ubicacion(self):
        return sorted(self.eventos, key=Evento.obtener_ubicacion_minusculas)
    
# 4)
def agregar_tarea_interactivo(agenda: Agenda):
    nombre = input("Nombre de la tarea: ")
    descripcion = input("Descripción: ")
    fecha_str = input("Fecha de vencimiento (YYYY-MM-DD): ")
    fecha_vencimiento = date.fromisoformat(fecha_str)
    prioridad = int(input("Prioridad (1 = Alta, 0 = Baja): "))
    tarea = Tarea(nombre, descripcion, fecha_vencimiento, prioridad)
    agenda.agregar_tarea(tarea)
    print("Tarea agregada correctamente.")

def agregar_evento_interactivo(agenda: Agenda):
    nombre = input("Nombre del evento: ")
    descripcion = input("Descripción: ")
    ubicacion = input("Ubicación: ")
    fecha_str = input("Fecha y hora del evento (YYYY-MM-DD HH:MM): ")
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
    duracion_min = int(input("Duración en minutos: "))
    duracion = timedelta(minutes=duracion_min)
    evento = Evento(nombre, descripcion, ubicacion, fecha, duracion)
    agenda.agregar_evento(evento)
    print("Evento agregado correctamente.")

def marcar_tarea_realizada_interactivo(agenda: Agenda):
    nombre = input("Nombre de la tarea a marcar como realizada: ")
    for tarea in agenda.tareas:
        if tarea.nombre == nombre:
            tarea.marcar_completa()
            print("Tarea marcada como completa.")
            return
    print("Tarea no encontrada.")

def listar_tareas_pendientes_por_fecha(agenda: Agenda):
    tareas = agenda.listar_tareas_por_fecha()
    for tarea in tareas:
        if not tarea.completa:
            print(tarea.obtener_info())
            print("-" * 30)

def listar_tareas_pendientes_por_prioridad(agenda: Agenda):
    tareas = agenda.listar_tareas_por_prioridad()
    for tarea in tareas:
        if not tarea.completa:
            print(tarea.obtener_info())
            print("-" * 30)

def listar_eventos_por_fecha(agenda: Agenda):
    eventos = agenda.listar_eventos_por_fecha()
    if not eventos:
        print("No hay eventos para mostrar.")
        return
    print("\n--- Eventos (por Fecha) ---")
    for evento in eventos:
        print(evento.obtener_info())
        print("-" * 30)

def listar_todo_por_fecha(agenda: Agenda):
    fecha_str = input("Ingresá la fecha a consultar (YYYY-MM-DD): ")
    try:
        fecha_consulta = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        print("Formato incorrecto. Usá YYYY-MM-DD.")
        return

    print(f"\n--- Tareas para el {fecha_consulta} ---")
    tareas_encontradas = False
    for tarea in agenda.tareas:
        if tarea.fecha_vencimiento == fecha_consulta:
            print(tarea.obtener_info())
            print("-" * 30)
            tareas_encontradas = True
    if not tareas_encontradas:
        print("No hay tareas para esta fecha.")

    print(f"\n--- Eventos para el {fecha_consulta} ---")
    eventos_encontrados = False
    for evento in agenda.eventos:
        if evento.fecha.date() == fecha_consulta:
            # Y AQUÍ también usarás evento.obtener_info()
            print(evento.obtener_info())
            print("-" * 30)
            eventos_encontrados = True
    if not eventos_encontrados:
        print("No hay eventos para esta fecha.")

def menu_agenda():
    agenda = Agenda()

    while True:
        print("\n--- MENÚ DE AGENDA ---")
        print("1. Agregar Tarea")
        print("2. Agregar Evento")
        print("3. Marcar Tarea como Realizada")
        print("4. Listar Tareas Pendientes por Fecha")
        print("5. Listar Tareas Pendientes por Prioridad")
        print("6. Listar Eventos por Fecha")
        print("7. Listar Tareas y Eventos de un Día")
        print("8. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            agregar_tarea_interactivo(agenda)
        elif opcion == "2":
            agregar_evento_interactivo(agenda)
        elif opcion == "3":
            marcar_tarea_realizada_interactivo(agenda)
        elif opcion == "4":
            listar_tareas_pendientes_por_fecha(agenda)
        elif opcion == "5":
            listar_tareas_pendientes_por_prioridad(agenda)
        elif opcion == "6":
            listar_eventos_por_fecha(agenda)
        elif opcion == "7":
            listar_todo_por_fecha(agenda)
        elif opcion == "8":
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción inválida. Elegí un número del 1 al 8.")

if __name__ == "__main__":
    menu_agenda()