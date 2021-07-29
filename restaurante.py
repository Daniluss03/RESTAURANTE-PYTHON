import sqlite3

def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor= conexion.cursor()
    try:
        cursor.execute('''CREATE TABLE  categoria(
        id INTEGER  PRIMARY KEY  AUTOINCREMENT,
        nombre VARCHAR (100)UNIQUE  NOT NULL)''')
    except sqlite3.OperationalError:
        print(" la tabla de categorias ya existe.")
    else:
        print("la tablas de categorias se ha credo correctamente")  
    try:      
        cursor.execute('''CREATE TABLE  plato(
        id INTEGER  PRIMARY KEY  AUTOINCREMENT,
        nombre VARCHAR (100) UNIQUE  NOT NULL,
        categoria_id INTEGER NOT NULL,
        FOREIGN KEY   (categoria_id)REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print(" la tabla de platos ya existe.")
    else:
        print("la tablas de platos se ha credo correctamente")    
 

    conexion.close()


def agregar_categoria():
    categoria=input("Nombre de la categoria?")
    conexion=sqlite3.connect("restaurante.db")
    cursor=conexion.cursor()
    try:
        cursor.execute("INSERT INTO  categoria VALUES (null,'{}')".format(categoria) )
    except sqlite3.IntegrityError:
        print("La categoria '{}' ya existe.".format(categoria))
    else:
        print("Categoria '{}' creada correctamente".format(categoria))    

    conexion.commit()
    conexion.close()


def  agregar_plato():
    conexion=sqlite3.connect("restaurante.db")
    cursor=conexion.cursor()

    categorias = cursor.execute("SELECT * FROM  categoria").fetchall()
    print("selecciona una categoria  para adjuntar el plato:")
    for categoria in categorias:
        print("[{}]{}".format(categoria[0],categoria[1]))

    categoria_usuario = int(input(">  "))  



    plato=input("Nombre del nuevo plato?\n> ")
    
    try:
        cursor.execute("INSERT INTO  plato VALUES (null,'{}',{})".format(plato,categoria_usuario) )
    except sqlite3.IntegrityError:
        print("El plato '{}' ya existe.".format(plato))
    else:
        print("plato '{}' creado correctamente".format(plato))   
    conexion.commit()
    conexion.close() 
def mostrar_menu():
    conexion=sqlite3.connect("restaurante.db")
    cursor=conexion.cursor()
    
    categorias =  cursor.execute("SELECT * FROM  categoria").fetchall()
    for categoria in categorias:
        print(categoria[1])
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
        for plato in platos:
            print("\t{}".format(plato[1]))


    conexion.close()             
#crear la base de datos      
crear_bd() 
# Menu de opciones del programa
while True:
    print("\nBienvenido al gestor del restaurante")
    opcion= input("\nIntroduce una opcion :\n[1]Agregar una categoria\n[2]agregar un plato \n[3]Salir del programa\n[4]Mostrar Menu\n\n")

    if opcion=="1":
        agregar_categoria()
    elif opcion=="2":
        agregar_plato()
    elif opcion=="3":
        print("Nos vemos")
        break
    elif opcion=="4":
        mostrar_menu()
        
    else:
        print("Opcion incorrecta")

