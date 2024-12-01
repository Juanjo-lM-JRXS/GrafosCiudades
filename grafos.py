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

ciudad = { 
    "ciudad1":ConsultaCiudadPorID(1),
    "ciudad2":ConsultaCiudadPorID(2),
    "ciudad3":ConsultaCiudadPorID(3),
    "ciudad4":ConsultaCiudadPorID(4),
    "ciudad5":ConsultaCiudadPorID(5),
    "ciudad6":ConsultaCiudadPorID(6),
    "ciudad7":ConsultaCiudadPorID(7),
    "ciudad8":ConsultaCiudadPorID(8),
    "ciudad9":ConsultaCiudadPorID(9),
    "ciudad10":ConsultaCiudadPorID(10)
}


g = Graph()
g.add_edge(ciudad["ciudad1"],ciudad["ciudad5"])
g.add_edge(ciudad["ciudad1"],ciudad["ciudad7"])
g.add_edge(ciudad["ciudad2"],ciudad["ciudad5"])
g.add_edge(ciudad["ciudad2"],ciudad["ciudad6"])
g.add_edge(ciudad["ciudad2"],ciudad["ciudad7"])
g.add_edge(ciudad["ciudad3"],ciudad["ciudad6"])
g.add_edge(ciudad["ciudad3"],ciudad["ciudad10"])
g.add_edge(ciudad["ciudad4"],ciudad["ciudad5"])
g.add_edge(ciudad["ciudad4"],ciudad["ciudad10"])
g.add_edge(ciudad["ciudad5"],ciudad["ciudad1"])
g.add_edge(ciudad["ciudad5"],ciudad["ciudad2"])
g.add_edge(ciudad["ciudad5"],ciudad["ciudad4"])
g.add_edge(ciudad["ciudad6"],ciudad["ciudad2"])
g.add_edge(ciudad["ciudad6"],ciudad["ciudad3"])
g.add_edge(ciudad["ciudad7"],ciudad["ciudad1"])
g.add_edge(ciudad["ciudad7"],ciudad["ciudad2"])
g.add_edge(ciudad["ciudad7"],ciudad["ciudad9"])
g.add_edge(ciudad["ciudad8"],ciudad["ciudad9"])
g.add_edge(ciudad["ciudad9"],ciudad["ciudad7"])
g.add_edge(ciudad["ciudad10"],ciudad["ciudad3"])
g.add_edge(ciudad["ciudad10"],ciudad["ciudad4"])

print("*****************************************Primer Grafo*****************************************")
print(g.display_graph())

print("*****************************************Las conexiones del un nodo 'Ciudad5'*****************************************")
print(g.get_connections(ciudad.get('ciudad5')))


print("*****************************************Actualiza las conecciones de un nodo*****************************************")
g.update_edge(ciudad["ciudad2"],ciudad["ciudad5"],ciudad["ciudad10"])


print("*****************************************Nodo a eliminar*****************************************")
g.delete_node(ciudad["ciudad1"])


print("*****************************Grafo final*****************************")
print(g.display_graph())