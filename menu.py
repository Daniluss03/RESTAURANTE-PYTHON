import sqlite3

from tkinter import*
#configuracion de la raiz 
root = Tk()
root.title("Bar don Costa")
root.resizable(0,0)
root.config(bd=25,relief="sunken")

Label(root,text="   Bar Don Costa"  ,fg="darkgreen",font=("Times New Roman ",28,"bold italic")).pack()
Label(root,text="   Menu del dia"  ,fg="darkgreen",font=("Times New Roman ",28,"bold italic")).pack()

#separacion de titulos y categorias 

Label(root,text="").pack()

conexion = sqlite3.connect("restaurante.db")
Cursor= conexion.cursor()
#buscar las categorias y platos de la base de datos 
categorias =  Cursor.execute("SELECT * FROM  categoria").fetchall()
for categoria in categorias:
        Label(root,text=categoria[1],fg="darkgreen",font=("Times New Roman ",28,"bold italic")).pack()
        
        
        platos = Cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
        for plato in platos:
            Label(root,text=plato[1],fg="darkgreen",font=("Times New Roman ",28,"bold italic")).pack()


conexion.close()
#finalmente ejecutamos el bucle
root.mainloop()