import sqlite3
from tkinter.simpledialog import askstring
from conectadb import *
from tkinter import*
from tkinter import messagebox

#CREO UN OBJETO VENTANA
root=Tk()

##VENTANAS EMERGENTES
def infoAdicional():
    messagebox.showinfo("Información", "Version codigo 1.0 Realizado por Monica Galarza")
    ##messagebox.showwarning("Advertencia", "Licencia caducada")
    ##messagebox.showinfo("Error", "Error de conexion")
    ##valor = messagebox.askquestion("Atencion", "Desea eliminar una persona")
    ##print(valor)
    #valor =messagebox.askokcancel("Atencion", "Desea salir de la aplicacion")
    #print(valor)

def infoAcerca():
    messagebox.showinfo("Información", "Version codigo 1.0 Realizado por Monica Galarza, Sistema de Administración de Usuarios")
    ##messagebox.showwarning("Advertencia", "Licencia caducada")
    ##messagebox.showinfo("Error", "Error de conexion")
    ##valor = messagebox.askquestion("Atencion", "Desea eliminar una persona")
    ##print(valor)
    #valor =messagebox.askokcancel("Atencion", "Desea salir de la aplicacion")
    #print(valor)

def Salir():
    root.destroy()

def limpiar():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miDireccion.set("")
    miPassword.set("")
    txtComentario.delete("1.0","end")

def conectarDB():
    #Crear una conexión
    miConexion=sqlite3.connect("bd")
    #Crear un cursor
    cursor=miConexion.cursor()
    messagebox.showinfo("Información", "Base de datos db conectada con éxito")

def crearUsuario():
    if miNombre.get() != "" and miApellido.get() != "" and miDireccion.get() != "" and miPassword.get() != "":
        valor = messagebox.askyesno(message="¿Seguro desea crear un usuario?", title="Administracion de usuarios")
        if valor== True:
            btningresar(miNombre.get(),miApellido.get(),miDireccion.get(),miPassword.get(),txtComentario.get("1.0","end"))
            limpiar()
            messagebox.showinfo(message="Guardado con Exito", title="Administracion de")
    else:
        messagebox.showinfo(message="Completar todos los campos de texto", title="Administracion de Usuarios")

def consultarUsuario():
    limpiar()
    miconexion=sqlite3.connect("bd")
    cursor = miconexion.cursor()
    numero = askstring('ID', 'Ingrese el ID a Mostrar?')
    if numero != None:
        cursor.execute("SELECT * FROM usuarios WHERE ID='"+numero+"'")
        listaUSUARIOS=cursor.fetchall()
        for usuario in listaUSUARIOS:
            miId.set(usuario[0])
            miNombre.set(usuario[1])
            miApellido.set(usuario[2])
            miDireccion.set(usuario[3])
            miPassword.set(usuario[4])
            txtComentario.insert("insert", usuario[4])
            btnmostar()
        if miId.get() == "":
            messagebox.showinfo(message="El ID no encontrado", title="Administracion de usuarios")

def modificarUsuario():
    if miNombre.get() != "" and miApellido.get() != "" and miDireccion.get() != "" and miPassword.get() != "":
        valor = messagebox.askyesno(message="¿Seguro desea modificar el usuario?", title="Administracion de usuarios")
        if valor== True:
            btnmodificar(miId.get(),miNombre.get(),miApellido.get(),miDireccion.get(),miPassword.get())
            messagebox.showinfo(message="Datos Actualizacos con Exito", title="Administración de usuarios")
    else:
        messagebox.showinfo(message="Completar todos los campos de texto", title="Administracion de usuarios")

def eliminarUsuario():
    ##consultarUsuario()
    numero = askstring('ID', 'Ingrese el ID a Eliminar?')
    if numero != None :
        valor = messagebox.askyesno(message="¿Seguro desea eliminar el usuario?", title="Administracion de Usuarios")
        if valor== True:
            btneliminar(str(numero))
            messagebox.showinfo(message="Datos eliminados correctamente", title="Administracion de Usuarios")
            limpiar()
            

root.geometry("500x300")
root.title("Ingreso de datos")
#CONFIGURO PARA QUE LA VENTANA NO SE PUEDA CAMBIAR EL TAMAÑO
root.resizable(0,0)
#AGREGO UN ICONO A LA VENTANA
root.iconbitmap("imagen.ico")
miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miDireccion=StringVar()
miPassword=StringVar()
miComentario=StringVar()
#CREO EL MENU
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)
###PRIMER NIVEL MENU
menubd=Menu(barraMenu, tearoff=0)
menuBorrar=Menu(barraMenu, tearoff=0)
menuCrud=Menu(barraMenu, tearoff=0)
menuAyuda=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="BD", menu=menubd)
barraMenu.add_cascade(label="Borrar", menu=menuBorrar)
barraMenu.add_cascade(label="CRUD   ", menu=menuCrud)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)

###SEGUNDO NIVEL MENU
##submenu BD
menubd.add_command(label="Conectar", command=conectarDB)
menubd.add_command(label="Salir", command=Salir)
##submenu BORRAR
menuBorrar.add_command(label="Borrar Campos", command=limpiar)
##submenu CRUD
menuCrud.add_command(label="Crear", command=crearUsuario)
menuCrud.add_command(label="Leer", command=consultarUsuario)
menuCrud.add_command(label="Actualizar", command=modificarUsuario)
menuCrud.add_command(label="Eliiminar", command=eliminarUsuario)
##submenu ayuda
menuAyuda.add_command(label="Acerca de ", command=infoAcerca)
menuAyuda.add_command(label="Licencia", command=infoAdicional)

miPanel3=Frame(root,width=300,height=300)
miPanel3.pack()
lblTitulo=Label(miPanel3, text="Sistema de Administración de Personas ")
lblTitulo.config(fg="Blue",font="Arial 13 bold" )
lblTitulo.grid(row=0,column=0,padx=5)

miPanel=Frame(root,width=300,height=300)
miPanel.pack()

lbl0=Label(miPanel, text="Id")
lbl0.grid(row=0,column=0,padx=5)

txtId=Entry(miPanel,textvariable=miId,state="disabled")
txtId.grid(row=0,column=1,padx=5)
txtId.config(fg="blue",  justify="left")

lbl1=Label(miPanel, text="Nombre")
lbl1.grid(row=1,column=0,padx=5)

txtNombre=Entry(miPanel,textvariable=miNombre)
txtNombre.grid(row=1,column=1,padx=5)
txtNombre.config(fg="blue",  justify="left")

lbl2=Label(miPanel, text="Apellido")
lbl2.grid(row=2,column=0,padx=5)

txtApellido=Entry(miPanel, textvariable=miApellido)
txtApellido.grid(row=2,column=1,padx=5)
txtApellido.config(fg="blue",  justify="left")

lbl3=Label(miPanel, text="Dirección")
lbl3.grid(row=3,column=0,padx=5)

txtDireccion=Entry(miPanel, textvariable=miDireccion)
txtDireccion.grid(row=3,column=1,padx=5)
txtDireccion.config(fg="blue",  justify="left")

lbl4=Label(miPanel, text="Password")
lbl4.grid(row=4,column=0)

txtPassword=Entry(miPanel, textvariable=miPassword)
txtPassword.grid(row=4,column=1,padx=5)
txtPassword.config(show="*", fg="blue",  justify="left")

##AREA DE TEXTO
lbl5=Label(miPanel, text="Comentario")
lbl5.grid(row=5,column=0)

txtComentario=Text(miPanel, width=15, height=5)
txtComentario.grid(row=5,column=1,padx=5)


##BOTÓN
#botonEnvio=Button(root, text="Enviar", command=codigoBoton)
#botonEnvio.pack()

miPanel2=Frame()
miPanel2=Frame(root,width=1200,height=600)
miPanel2.pack()

botonCrear=Button(miPanel2,text="Crear",command=crearUsuario)
botonCrear.grid(row=0,column=0,padx=5,pady=5)

botonLeer=Button(miPanel2,text="Leer",command=consultarUsuario)
botonLeer.grid(row=0,column=1,padx=5,pady=5)

botonActualizar=Button(miPanel2,text="Actualizar",command=modificarUsuario)
botonActualizar.grid(row=0,column=2,padx=5,pady=5)

botonActualizar=Button(miPanel2,text="Eliminar",command=eliminarUsuario)
botonActualizar.grid(row=0,column=3,padx=5,pady=5)

root.mainloop()