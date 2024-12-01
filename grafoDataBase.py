import mysql.connector;

db = mysql.connector.connect(user="root", password="",
                            host="localhost", database="ciudadescolombia",
                            auth_plugin="mysql_navite_password")

cursor = db.cursor()

def CreaUnaConexion(nodoIngreso, nuevaConexion):
    cursor.callproc("CreaUnaConexion",(nodoIngreso,nuevaConexion,))
    for result in cursor.stored_results():
        print(result.fetchall())

def LeerUnaConexion(nodoIngreso):
    cursor.callproc("LeerUnaConexion",(nodoIngreso,))
    for result in cursor.stored_results():
        print(result.fetchall())

def ActualizaLasAristasNodo(nodoIngreso, nodoActiguo,nuevaConexion):
    cursor.callproc("ActualizaLasAristasNodo",(nodoIngreso,nodoActiguo,nuevaConexion,))
    for result in cursor.stored_results():
        print(result.fetchall())

def EliminarConexionesNodo(nodoIngreso):
    cursor.callproc("EliminarConexionesNodo",(nodoIngreso,))
    for result in cursor.stored_results():
        print(result.fetchall())

print("**************************************Crea una conexion**************************************")
nodoActual = int(input("Ingrese el nodo actual:"))
nuevaConexion = int(input("Ingrese la nueva arista:"))
CreaUnaConexion(nodoActual, nuevaConexion)
print("**************************************Lee una conexion**************************************")
LeerUnaConexion(nodoActual)
print("**************************************Actualizar una conexion**************************************")
nodoActual = int(input("Ingrese el nodo actual:"))
aristaAntiguo = int(input("Ingrese la arista antigua:"))
aristaNuevo = int(input("Ingrese la nueva arista:"))
ActualizaLasAristasNodo(nodoActual,aristaAntiguo,aristaNuevo)
print("**************************************Eliminar un nodo**************************************")
nodoActual = int(input("Ingrese el nodo a eliminar:"))
EliminarConexionesNodo(nodoActual)
print("Nodo eliminado con exito!")