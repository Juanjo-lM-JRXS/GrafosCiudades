import mysql.connector;

db = mysql.connector.connect(user="root", password="",
                            host="localhost", database="ciudadescolombia",
                            auth_plugin="mysql_navite_password")

cursor = db.cursor()

class Graph:
    def __init__(self):
        self.graph = {}

    # Crear (Agregar nodo y arista)
    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    # Leer (Mostrar las conexiones de un nodo)
    def get_connections(self, node):
        return self.graph.get(node, [])

    # Actualizar (Agregar un vecino adicional a un nodo)
    def update_edge(self, node, old_neighbor, new_neighbor):
        if node in self.graph and old_neighbor in self.graph[node]:
            self.graph[node].remove(old_neighbor)
            self.graph[node].append(new_neighbor)

    # Eliminar (Eliminar un nodo y sus conexiones)
    def delete_node(self, node):
        if node in self.graph:
            del self.graph[node]
        for connections in self.graph.values():
            if node in connections:
                connections.remove(node)

    # Mostrar el grafo completo
    def display_graph(self):
        return self.graph

def ConsultaCiudadPorID(id):
    cursor.callproc("ConsultaCiudadPorID",(id,))
    for result in cursor.stored_results():
        r= result.fetchall()
    return r[0]

ciudad = [ ConsultaCiudadPorID(1),
    ConsultaCiudadPorID(2),
    ConsultaCiudadPorID(3),
    ConsultaCiudadPorID(4),
    ConsultaCiudadPorID(5),
    ConsultaCiudadPorID(6),
    ConsultaCiudadPorID(7),
    ConsultaCiudadPorID(8),
    ConsultaCiudadPorID(9),
    ConsultaCiudadPorID(10)
    ]


g = Graph()
g.add_edge(ciudad[1-1],ciudad[5-1])
g.add_edge(ciudad[1-1],ciudad[7-1])
g.add_edge(ciudad[2-1],ciudad[5-1])
g.add_edge(ciudad[2-1],ciudad[6-1])
g.add_edge(ciudad[2-1],ciudad[7-1])
g.add_edge(ciudad[3-1],ciudad[6-1])
g.add_edge(ciudad[3-1],ciudad[10-1])
g.add_edge(ciudad[4-1],ciudad[5-1])
g.add_edge(ciudad[4-1],ciudad[10-1])
g.add_edge(ciudad[5-1],ciudad[1-1])
g.add_edge(ciudad[5-1],ciudad[2-1])
g.add_edge(ciudad[5-1],ciudad[4-1])
g.add_edge(ciudad[6-1],ciudad[2-1])
g.add_edge(ciudad[6-1],ciudad[3-1])
g.add_edge(ciudad[7-1],ciudad[1-1])
g.add_edge(ciudad[7-1],ciudad[2-1])
g.add_edge(ciudad[7-1],ciudad[9-1])
g.add_edge(ciudad[8-1],ciudad[9-1])
g.add_edge(ciudad[9-1],ciudad[7-1])
g.add_edge(ciudad[9-1],ciudad[8-1])
g.add_edge(ciudad[10-1],ciudad[3-1])
g.add_edge(ciudad[10-1],ciudad[4-1])

print("*****************************************Primer Grafo*****************************************")
print(g.display_graph())

print("*****************************************Las conecciones de un nodo*****************************************")
conexion = int(input("Ingrese el numero del nodo a conocer sus conexiones;"))
print(g.get_connections(ciudad[conexion-1]))


print("*****************************************Actualiza las conecciones de un nodo*****************************************")
nodoActualizacion = int(input("Ingrese el nodo:"))
vecinoAntiguoActualizacion = int(input("Ingrese el vecino actual:"))
vecinoNuevoActualizacion = int(input("Ingrese el nuevo vecino:"))
g.update_edge(ciudad[nodoActualizacion-1],ciudad[vecinoAntiguoActualizacion-1],ciudad[vecinoNuevoActualizacion-1])


print("*****************************************Nodo a eliminar*****************************************")
nodoEliminar = int(input("Ingrese el numero del nodo a eliminar:"))
g.delete_node(ciudad[nodoEliminar-1])


print("*****************************Grafo final*****************************")
print(g.display_graph())