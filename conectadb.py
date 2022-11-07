import sqlite3
#Crear una conexion
miconexion=sqlite3.connect("bd")
### Crear un cursor
def btnconectarbd():
    cursor = miconexion.cursor()

def btningresar(nombre,apellido,direccion,password,comentario):
    miconexion=sqlite3.connect("bd")
    cursor = miconexion.cursor()
    cursor.execute("CREATE TABLE usuarios (ID INTEGER PRIMARY KEY AUTOINCREMENT,nombre VARCHAR(25),apellido VARCHAR(25),direccion VARCHAR(25),passwprd VARCHAR(25), comentario VARCHAR(25))")
    cursor.execute("DROP TABLE usuarios")
    miconexion.commit()
    cursor.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT,nombre VARCHAR(25),apellido VARCHAR(25),direccion VARCHAR(25),password VARCHAR(25), comentario VARCHAR(25))")
    miconexion.commit()

    ##cursor.executescript("INSERT INTO usuarios VALUES (NULL,'"+nombre+"','"+apellido+"','"+direccion+"','"+password+"','"+comentario+"')")
    print("insert into usuarios values (null,'"+nombre+"','"+apellido+"','"+direccion+"','"+password+"','"+comentario+"')")
    cursor.execute("insert into usuarios values (null,'"+nombre+"','"+apellido+"','"+direccion+"','"+password+"','"+comentario+"')")
    
    miconexion.commit()
    miconexion.close()

def btnmostar():
    miconexion=sqlite3.connect("bd")
    cursor = miconexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    listaUSUARIOS=cursor.fetchall()
    for usuario in listaUSUARIOS:
        print("id: ",usuario[0],"nombre: ",usuario[1],"apellido: ",usuario[2],"direccion: ",usuario[3],"password: ",usuario[4],"comentario: ",usuario[5])

def btneliminar(id):
    miconexion=sqlite3.connect("bd")
    cursor = miconexion.cursor()
    cursor.executescript("DELETE FROM usuarios WHERE id='"+id+"'")

def btnmodificar(id,nom,ape,dir,pas):
    miconexion=sqlite3.connect("bd")
    cursor = miconexion.cursor()
    print("UPDATE usuarios SET nombre='"+nom+"', apellido='"+ape+"', direccion='"+dir+"', password='"+pas+"' WHERE id="+id)
    cursor.execute("UPDATE usuarios SET nombre='"+nom+"', apellido='"+ape+"', direccion='"+dir+"', password='"+pas+"' WHERE id="+id)
    miconexion.commit()