print("        =============          ")
print("       ===============          ")
print("================================")
print("Sistema de Gestion Universitaria")
print("================================")
print("       ===============          ")
print("        =============          ")
import USUARIO
import PASSW
from mysql import connector as conector

host = "localhost"
user = "root"
password = "lnhre+30"
database = "db_unphu"

conexion = conector.connect(host = "localhost", user = user, password = password, database = database)

myCursor = conexion.cursor()

myCursor.execute('show database')

for x in myCursor:
    print(x)


correcto=False
while correcto==False:
        nombre=input("Ingrese nombre de usuario: ")
        if USUARIO.nickname(nombre) == True:
            print("Usuario creado exitosamente")
            correcto=True

while correcto==True:
    contrasenia=input("Ingrese su Password: ")
    if PASSW.clave(contrasenia)==True:
        print("Contraseña creada exitosamente")
        correcto=False

print("Eliga a continuacion la opcion que desea realizar.")


Menu_Op = int(input("[1]: Registar, [2]: Consultar, [3]: Listar,  [4]: Eliminar, [5]: Actualizar, \n"))

if Menu_Op == 1:
    print("Que desea Registar.")

if Menu_Op == 2:
    print("Que desea Consultar.")

if Menu_Op == 3:
    print("Que desea Listar.")

if Menu_Op == 4:
    print("Que desea Eliminar.")

if Menu_Op == 5:
    print("Que desea Actualizar.")


op = int(input("[1]: Materia, [2]: Carrera, [3]:Materia por Carrera, [4]: Estudiante,[5]: Profesores, [6]: Secciones por Estudiantes, [7]: Secciones por Profesores"))

'''if op == 1:
    def registro_materia():'''
        
        

  
