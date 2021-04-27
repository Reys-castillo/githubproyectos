print('        =============          ')
print('       ===============          ')
print('================================')
print('Sistema de Gestion Universitaria')
print('================================')
print('       ===============          ')
print('        =============          ')

from mysql import connector as conector
import USUARIO
import PASSW

correcto=False
while correcto==False:
        nombre=input('Ingrese nombre de usuario: ')
        if USUARIO.nickname(nombre) == True:
            print('Usuario creado exitosamente')
            correcto=True

while correcto==True:
    contrasenia=input('Ingrese su Password: ')
    if PASSW.clave(contrasenia)==True:
        print('Contraseña creada exitosamente')
        correcto=False

ip = 'localhost'
usuario = 'root'
password = 'lnhre+30'
database = 'db_unphu'

conex = conector.connect(host = 'localhost',user = usuario,password = password,database = database)

myCursor = conex.cursor()

print("Eliga a continuacion la opcion que desea realizar.")

Menu_Op = int(input("[1]: Registar, [2]: Consultar, [3]: Eliminar, [4]: Actualizar, [5]: Listar \n"))

if Menu_Op == 1:
    print("Que desea Registar: \n\
-Estudiantes\n\
-Materias\n\
-Profesores\n\
-Carrera\n\
-Materia por Carrera\n\
-Secciones por Estudiantes\n\
-Secciones por Profesores\n ")

    op = input("Ingrese el nombre de lo que desea Registar: \n")

    if op == "Estudiantes":
        nombre = input('Nombre del estudiante: ')
        apellido = input('Apellido: ')
        cedula  = input('Cedula: ')
        telefono = input('Telefono: ')
        nacionalidad = input('Nacionalidad: ')
        email = input('Email: ')
        sexo = input('Sexo: ')
        carrera = input('Carrera: ')
        comando = 'insert into estudiantes (nombre,apellido,cedula,telefono,nacionalidad,email,sexo,carrera) values (%s, %s, %s, %s, %s, %s, %s, %s)'
        valores =(nombre, apellido, cedula, telefono, nacionalidad, email, sexo, carrera)
    
        myCursor.execute(comando,valores)

        myCursor.execute('select * from estudiantes')

        for x in myCursor:
            print(x)

    if op == "Materia":
        codigo = input('Codigo de materia: ')
        nombre = input('Nombre de materia: ')
        creditos  = int(input('Creditos: '))
        comando = 'insert into MATERIAS(codigo,nombre,creditos) values (%s, %s, int)'
        valores =(codigo, nombre, creditos)

        myCursor.execute(comando,valores)

        myCursor.execute('select * from MATERIAS')

        for x in myCursor:
            print(x)

    if op == "Profesores":
        nombre= input('Nombre del Profesor: ')
        apellido = input('Apellido: ')
        direccion  = int(input('Direccion: '))
        telefono = input('Telefono: ')
        email = input('Email: ')
        cedula  = int(input('Cedula: '))
        comando = 'insert into PROFESORES(nombre,apellido,direccion,telefono,email,cedula) values (%s, %s, %s, %s, %s, %s)'
        valores = (nombre, apellido, direccion, telefono, email, cedula)

        myCursor.execute(comando,valores)

        myCursor.execute('select * from PROFESORES')

        for x in myCursor:
            print(x)

    if op == "Carrera":
        codigo= input('Codigo: ')
        nombre= input('Nombre: ')
        comando = 'insert into CARRERA(codigo, nombre) values (%s, %s)'
        valores = (codigo, nombre)

        myCursor.execute(comando,valores)
    
        myCursor.execute('select * from PROFESORES')

        for x in myCursor:
            print(x)

    if op == "Materia por Carrera":
        CODIGO_CARRERA = input('Codigo de Carrera: ')
        NOMBRE_CARRERA = input('Nombre: ')
        MATERIA_x_CARRERA  = int(input('Materia por Carrera: '))
        comando = 'insert into MATERIA_X_CARRERA(CODIGO_CARRERA,NOMBRE_CARRERA,MATERIA_x_CARRERA) values (%s, %s, int)'
        valores =(CODIGO_CARRERA,NOMBRE_CARRERA,MATERIA_x_CARRERA)

        myCursor.execute(comando,valores)

        myCursor.execute('select * from MATERIA_X_CARRERA')

        for x in myCursor:
            print(x)
  
    if op == "Secciones por Estudiantes":
        CODIDO_MATERIA = input('Codigo de materia: ')
        FECHA_PERIODO = input('Periodo: ')
        NUMERO_SECCION  = int(input('Numero de Seccion: '))
        GRUPOS_DISPONIBLES = int(input('Grupos Disponibles: '))
        NOMBRE_PROFESORES = input('Nombre de profesor: ')
        NOMBRE_MATERIA = input('Nombre de materia: ')

        comando = 'INSERT INTO SECIONES_X_ESTUDIANTES(CODIDO_MATERIA,FECHA_PERIODO,NUMERO_SECCION,GRUPOS_DISPONIBLES,NOMBRE_PROFESORES, NOMBRE_MATERIA) values (%s, %s, int, int, %s, %s)'
        valores =(CODIDO_MATERIA,FECHA_PERIODO,NUMERO_SECCION,GRUPOS_DISPONIBLES,NOMBRE_PROFESORES, NOMBRE_MATERIA)
    
        myCursor.execute(comando,valores)

        myCursor.execute('select * from secciones_x_estudiantes')

        for x in myCursor:
            print(x)

    


    if op == "Secciones por Profesores":
        CODIDO_MATERIA = input('Codigo de materia: ')
        FECHA_PERIODO = input('Periodo: ')
        NUMERO_SECCION  = int(input('Numero de Seccion: '))
        GRUPOS_DISPONIBLES = int(input('Grupos Disponibles: '))
        NOMBRE_MATERIA = input('Nombre de materia: ')

        comando = 'insert into secciones_x_profesores (CODIDO_MATERIA,FECHA_PERIODO,NUMERO_SECCION,GRUPOS_DISPONIBLES,NOMBRE_PROFESORES, NOMBRE_MATERIA) values (%s, %s, int, int, %s, %s)'
        valores =(CODIDO_MATERIA,FECHA_PERIODO,NUMERO_SECCION,GRUPOS_DISPONIBLES,NOMBRE_MATERIA)
    
        myCursor.execute(comando,valores)

        myCursor.execute('select * from secciones_x_profesores')

        for x in myCursor:
            print(x)

if Menu_Op == 2:
    print("Que desea Consultar: \n\
-Estudiantes\n\
-Materia\n\
-Profesores\n\
-Carrera\n\
-Materia por Carrera\n\
-Secciones por Estudiantes\n\
-Secciones por Profesores\n ")
    op = input("Ingrese el nombre de lo que desea Consultar: \n")

    if op == "Estudiantes":
        nombre = input('Nombre del estudiante: ')
        apellido = input('Apellido: ')
        comando = 'select * from ESTUDIANTES where nombre = %s and apellido = %s'
        valores =(nombre, apellido,)

        myCursor.execute(comando,valores)

        for x in myCursor:
            print(x)

    if op == "Materia":
        codigo = input('Codigo: ')
        nombre = input('Nombre de Materia: ')
        comando = 'select * from MATERIAS where codigo = %s and nombre = %s'
        valores =(codigo, nombre)

        myCursor.execute(comando,valores)

        for x in myCursor:
            print(x)
    
    if op == "Profesores":
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        cedula = input('Cedula: ')
        comando = 'select * from PROFESORES where codigo = %s and nombre = %s and cedula = %s'
        valores =(nombre, apellido, cedula)

        myCursor.execute(comando,valores)

        for x in myCursor:
            print(x)
                

    if op == "Carrera":
        codigo = input('Codigo: ')
        nombre = input('Nombre de la Carrera: ')
        comando = 'select * from CARRERA where codigo = %s and nombre = %s'
        valores =(codigo, nombre)

        myCursor.execute(comando,valores)

        for x in myCursor:
            print(x)


    if op == "Materia por Carrera":
        CODIGO_CARRERA = input('Codigo de Carrera: ')
        NOMBRE_CARRERA = input('Nombre: ')
        MATERIA_x_CARRERA  = int(input('Materia por Carrera: '))
        comando = 'select * from CARRERA where CODIGO_CARRERA = %s and  NOMBRE_CARRERA = %s and MATERIA_x_CARRERA = %s'
        valores =(CODIGO_CARRERA,NOMBRE_CARRERA,MATERIA_x_CARRERA)

        myCursor.execute(comando,valores)

        myCursor.execute('select * from MATERIA_X_CARRERA')

        for x in myCursor:
            print(x)
    
    
    if op == "Secciones por Estudiantes":
        CODIDO_MATERIA = input('Codigo de materia: ')
        FECHA_PERIODO = input('Periodo: ')
        NUMERO_SECCION  = int(input('Numero de Seccion: '))
        GRUPOS_DISPONIBLES = int(input('Grupos Disponibles: '))
        NOMBRE_PROFESORES = input('Nombre de profesor: ')
        NOMBRE_MATERIA = input('Nombre de materia: ')

        comando = 'select * from secciones_x_estudiantes where CODIDO_MATERIA = %s and FECHA_PERIODO = %s and NUMERO_SECCION = int and GRUPOS_DISPONIBLES = int and NOMBRE_PROFESORES = %s and  NOMBRE_MATERIA = %s'
        valores =(CODIDO_MATERIA,FECHA_PERIODO,NUMERO_SECCION,GRUPOS_DISPONIBLES,NOMBRE_PROFESORES, NOMBRE_MATERIA)
    
        myCursor.execute(comando,valores)

        myCursor.execute('select * from secciones_x_estudiantes')

        for x in myCursor:
            print(x)


    if op == "Secciones por Profesores":
        CODIDO_MATERIA = input('Codigo de materia: ')
        FECHA_PERIODO = input('Periodo: ')
        NUMERO_SECCION  = int(input('Numero de Seccion: '))
        GRUPOS_DISPONIBLES = int(input('Grupos Disponibles: '))
        NOMBRE_MATERIA = input('Nombre de materia: ')

        comando = 'select * from secciones_x_estudiantes where CODIDO_MATERIA = %s and FECHA_PERIODO = %s and NUMERO_SECCION = int and GRUPOS_DISPONIBLES = int and NOMBRE_MATERIA = %s'
        valores =(CODIDO_MATERIA,FECHA_PERIODO,NUMERO_SECCION,GRUPOS_DISPONIBLES,NOMBRE_PROFESORES, NOMBRE_MATERIA)
    
        myCursor.execute(comando,valores)

        myCursor.execute('select * from secciones_x_estudiantes')

        for x in myCursor:
            print(x)
    
if Menu_Op == 3:
    print("Que desea Eliminar: \n\
-Estudiantes\n\
-Materia\n\
-Profesores\n\
-Carrera\n\
-Materia por Carrera\n\
-Secciones por Estudiantes\n\
-Secciones por Profesores\n ")
    op = input("Ingrese el nombre de lo que desea Eliminar: \n")

    if op == "Estudiantes":
        nombre = input('Nombre del estudiante: ')
        apellido = input('Apellido: ')
        comando = 'delete from estudiantes where nombre = %s and apellido = %s'
        valores =(nombre, apellido)
    
        myCursor.execute(comando,valores)
        for x in myCursor:
            print(x)

    if op == "Materia":
        codigo = input('Codigo: ')
        nombre = input('Nombre de Materia: ')
        comando = 'delete from estudiantes where codigo = %s and nombre = %s'
        valores =(codigo, nombre)
    
        myCursor.execute(comando,valores)
        for x in myCursor:
            print(x)
    
    if op == "Profesores":
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        cedula = input('Cedula: ')
        comando = 'delete from estudiantes where nombre = %s and apellido = %s and cedula = %s'
        valores =(nombre, apellido, cedula)
    
        myCursor.execute(comando,valores)
        for x in myCursor:
            print(x)

    if op == "Carrera":
        codigo = input('Codigo: ')
        nombre = input('Nombre de la Carrera: ')
        comando = 'delete from estudiantes where codigo = %s and nombre = %s '
        valores =(codigo, nombre)
    
        myCursor.execute(comando,valores)
        for x in myCursor:
            print(x)
            
    if op == "Materia por Carrera":
        CODIGO_CARRERA = input('Codigo de Carrera: ')
        NOMBRE_CARRERA = input('Nombre: ')
        MATERIA_x_CARRERA  = int(input('Materia por Carrera: '))
        comando = 'delete from MATERIA_X_CARRERA where CODIGO_CARRERA = %s and NOMBRE_CARRERA = %s and MATERIA_x_CARRERA = %s'
        valores =(CODIGO_CARRERA,NOMBRE_CARRERA,MATERIA_x_CARRERA)

        myCursor.execute(comando,valores)
        for x in myCursor:
            print(x)
        
    
    if op == "Secciones por Estudiantes":
        CODIDO_MATERIA = input('Codigo de materia: ')
        FECHA_PERIODO = input('Periodo: ')
        NUMERO_SECCION  = int(input('Numero de Seccion: '))
        GRUPOS_DISPONIBLES = int(input('Grupos Disponibles: '))
        NOMBRE_PROFESORES = input('Nombre de profesor: ')
        NOMBRE_MATERIA = input('Nombre de materia: ')

        comando = 'delete from secciones_x_estudiantes where CODIDO_MATERIA = %s and FECHA_PERIODO = %s and NUMERO_SECCION = int and GRUPOS_DISPONIBLES = int and NOMBRE_PROFESORES = %s and  NOMBRE_MATERIA = %s'
        valores =(CODIDO_MATERIA,FECHA_PERIODO,NUMERO_SECCION,GRUPOS_DISPONIBLES,NOMBRE_PROFESORES, NOMBRE_MATERIA)
    
        myCursor.execute(comando,valores)

        for x in myCursor:
            print(x)

    if op == "Secciones por Profesores":
        CODIDO_MATERIA = input('Codigo de materia: ')
        FECHA_PERIODO = input('Periodo: ')
        NUMERO_SECCION  = int(input('Numero de Seccion: '))
        GRUPOS_DISPONIBLES = int(input('Grupos Disponibles: '))
        NOMBRE_MATERIA = input('Nombre de materia: ')

        comando = 'delete * from secciones_x_estudiantes where CODIDO_MATERIA = %s and FECHA_PERIODO = %s and NUMERO_SECCION = int and GRUPOS_DISPONIBLES = int and NOMBRE_PROFESORES = %s and  NOMBRE_MATERIA = %s'
        valores =(CODIDO_MATERIA,FECHA_PERIODO,NUMERO_SECCION,GRUPOS_DISPONIBLES,NOMBRE_PROFESORES, NOMBRE_MATERIA)
    
        myCursor.execute(comando,valores)

        for x in myCursor:
            print(x)
    
if Menu_Op == 4:
    print("Que desea Actualizar: \n\
-Estudiantes\n\
-Materia\n\
-Profesores\n\
-Carrera\n\
-Materia por Carrera\n\
-Secciones por Estudiantes\n\
-Secciones por Profesores\n ")
    op = input("Ingrese el nombre de lo que desea Actualizar: \n")
    if op == "Estudiantes":
        old_nombre = input('Nombre del estudiante: ')
        old_apellido = input('Apellido: ')
        old_cedula  = input('Cedula: ')
        old_telefono = input('Telefono: ')
        old_nacionalidad = input('Nacionalidad: ')
        old_email = input('Email: ')
        old_sexo = input('Sexo: ')
        old_carrera = input('Carrera: ')
        print("Favor de ingresar los nuevos datos: ")
        new_nombre = input('Nombre del estudiante: ')
        new_apellido = input('Apellido: ')
        new_cedula  = input('Cedula: ')
        new_telefono = input('Telefono: ')
        new_nacionalidad = input('Nacionalidad: ')
        new_email = input('Email: ')
        new_sexo = input('Sexo: ')
        new_carrera = input('Carrera: ')
        comando = 'UPDATE ESTUDIANTES SET old_nombre =%s, old_apellido = %s, old_cedula = %s, old_telefono = %s, old_nacionalidad = %s, old_email = %s, old_sexo = %s, old_carrera = %s WHERE new_nombre =%s, new_apellido = %s, new_cedula = %s, new_telefono = %s, new_nacionalidad = %s, new_email = %s, new_sexo = %s, new_carrera = %s'
        
        valores =(new_nombre,new_apellido,new_cedula,new_telefono,new_nacionalidad,new_email,new_sexo,new_carrera, old_nombre,old_apellido,old_cedula,old_telefono,old_nacionalidad,old_email,old_sexo,old_carrera)
    
        myCursor.execute(comando,valores)

        myCursor.execute('select * from ESTUDIANTES')

        for x in myCursor:
            print(x)

    if op == "Materia":
        codigo = input('Codigo: ')
        nombre = input('Nombre de Materia: ')
        creditos = int(input("Creditos: "))
        print("Favor de ingresar los nuevos datos: ")
        codigo = input('Codigo: ')
        nombre = input('Nombre de Materia: ')
        creditos = int(input("Creditos: "))

        comando = 'UPDATE MATERIAS SET codigo = %s, nombre = %s, creditos = int WHERE codigo = %s, nombre = %s, creditos = int'
        
        valores =(codigo,nombre,creditos,codigo,nombre,creditos)
    
        myCursor.execute(comando,valores)

        for x in myCursor:
            print(x)

    if op == "Profesores":
        old_nombre= input('Nombre del Profesor: ')
        old_apellido = input('Apellido: ')
        old_direccion  = int(input('Direccion: '))
        old_telefono = input('Telefono: ')
        old_email = input('Email: ')
        old_cedula  = int(input('Cedula: '))
        print("Favor de ingresar los nuevos datos: ")
        new_nombre= input('Nombre del Profesor: ')
        new_apellido = input('Apellido: ')
        new_direccion  = int(input('Direccion: '))
        new_telefono = input('Telefono: ')
        new_email = input('Email: ')
        new_cedula  = int(input('Cedula: '))


    
        comando = 'UPDATE ESTUDIANTES SET old_nombre =%s, old_apellido = %s, old_direccion = %s, old_telefono = %s, old_email = %s, old_cedula = %s WHERE new_nombre =%s, new_apellido = %s, new_direccion = %s, new_telefono = %s, new_email = %s, new_cedula = %s'
        valores = (new_nombre, new_apellido, new_direccion, new_telefono, new_email, new_cedula,old_nombre,old_apellido,old_direccion,old_telefono,old_email,old_cedula)

        myCursor.execute(comando,valores)

        myCursor.execute('select * from PROFESORES')

        for x in myCursor:
            print(x)


    if op == "Carrera":
        old_codigo= input('Codigo: ')
        old_nombre= input('Nombre: ')
        print("Favor de ingresar los nuevos datos: ")
        new_codigo= input('Codigo: ')
        new_nombre= input('Nombre: ')
                            
        comando = 'UPDATE CARRERA SET old_codigo =%s, old_nombre = %s WHERE new_codigo =%s, new_nombre = %s'
        
        valores =(new_codigo,new_nombre,old_codigo,old_nombre)

        myCursor.execute(comando,valores)
    
        myCursor.execute('select * from PROFESORES')

        for x in myCursor:
            print(x)



    if op == "Materia por Carrera":
        old_CODIGO_CARRERA = input('Codigo de Carrera: ')
        old_NOMBRE_CARRERA = input('Nombre: ')
        old_MATERIA_x_CARRERA  = int(input('Materia por Carrera: '))
        print("Favor de ingresar los nuevos datos: ")
        new_CODIGO_CARRERA = input('Codigo de Carrera: ')
        new_NOMBRE_CARRERA = input('Nombre: ')
        new_MATERIA_x_CARRERA  = int(input('Materia por Carrera: '))

        comando = 'UPDATE CARRERA SET old_CODIGO_CARRERA =%s, old_NOMBRE_CARRERA = %s, old_MATERIA_x_CARRERA = int WHERE old_CODIGO_CARRERA =%s, old_NOMBRE_CARRERA = %s, old_MATERIA_x_CARRERA = int'
        valores = (new_CODIGO_CARRERA,new_NOMBRE_CARRERA,new_MATERIA_x_CARRERA,old_CODIGO_CARRERA,old_NOMBRE_CARRERA,old_MATERIA_x_CARRERA)

        myCursor.execute(comando,valores)

        myCursor.execute('select * from MATERIAS')

        for x in myCursor:
            print(x)


    if op == "Secciones por Estudiantes":
        old_CODIGO_MATERIA = input('Codigo de materia: ')
        old_FECHA_PERIODO = input('Periodo: ')
        old_NUMERO_SECCION = int(input('Numero de Seccion: ' ))
        old_GRUPOS_DISPONIBLES = int(input('Grupos Disponibles: '))
        old_NOMBRE_PROFESORES = input('Nombre de profesor: ')
        old_NOMBRE_MATERIA= input('Nombre de materia: ')
        print("Favor de ingresar los nuevos datos: ")
        new_CODIGO_MATERIA = input('Codigo de materia: ')
        new_FECHA_PERIODO = input('Periodo: ')
        new_NUMERO_SECCION = int(input('Numero de Seccion: '))
        new_GRUPOS_DISPONIBLES = int(input('Grupos Disponibles: '))
        new_NOMBRE_PROFESORES = input('Nombre de profesor: ')
        new_NOMBRE_MATERIA= input('Nombre de materia: ')

        comando = 'UPDATE SECCIONES_X_ESTUDIANTES SET old_CODIGO_MATERIA =%s,  old_FECHA_PERIODO = %s,  old_NUMERO_SECCION = int, old_GRUPOS_DISPONIBLES = int, old_NOMBRE_PROFESORES = %s, old_NOMBRE_MATERIA = %s WHERE new_CODIGO_MATERIA =%s,  new_FECHA_PERIODO = %s,  new_NUMERO_SECCION = int, new_GRUPOS_DISPONIBLES = int, new_NOMBRE_PROFESORES = %s, new_NOMBRE_MATERIA = %s'

        valores =(new_CODIGO_MATERIA,new_FECHA_PERIODO,new_NUMERO_SECCION,new_GRUPOS_DISPONIBLES,new_NOMBRE_PROFESORES,new_NOMBRE_MATERIold_CODIGO_MATERIA,old_FECHA_PERIODO,old_NUMERO_SECCION,old_GRUPOS_DISPONIBLES,old_NOMBRE_PROFESORES,old_NOMBRE_MATERIA)
    
        myCursor.execute(comando,valores)

        myCursor.execute('select * from SECCIONES_X_ESTUDIANTES')

        for x in myCursor:
            print(x)


    if op == "Secciones por Profesores":
        old_CODIGO_MATERIA = input('Codigo de materia: ')
        old_FECHA_PERIODO = input('Periodo: ')
        old_NUMERO_SECCION = int(input('Numero de Seccion: ' ))
        old_GRUPOS_DISPONIBLES = int(input('Grupos Disponibles: '))
        old_NOMBRE_MATERIA= input('Nombre de materia: ')
        print("Favor de ingresar los nuevos datos: ")
        new_CODIGO_MATERIA = input('Codigo de materia: ')
        new_FECHA_PERIODO = input('Periodo: ')
        new_NUMERO_SECCION = int(input('Numero de Seccion: '))
        new_GRUPOS_DISPONIBLES = int(input('Grupos Disponibles: '))
        new_NOMBRE_MATERIA= input('Nombre de materia: ')

        comando = 'UPDATE SECCIONES_X_ESTUDIANTES SET old_CODIGO_MATERIA =%s,  old_FECHA_PERIODO = %s,  old_NUMERO_SECCION = int, old_GRUPOS_DISPONIBLES = int, old_NOMBRE_PROFESORES = %s, old_NOMBRE_MATERIA = %s WHERE new_CODIGO_MATERIA =%s,  new_FECHA_PERIODO = %s,  new_NUMERO_SECCION = int, new_GRUPOS_DISPONIBLES = int, new_NOMBRE_PROFESORES = %s, new_NOMBRE_MATERIA = %s'

        valores =(new_CODIGO_MATERIA,new_FECHA_PERIODO,new_NUMERO_SECCION,new_GRUPOS_DISPONIBLES,new_NOMBRE_MATERIA,old_CODIGO_MATERIA,old_FECHA_PERIODO,old_NUMERO_SECCION,old_GRUPOS_DISPONIBLES,old_NOMBRE_MATERIA)
    
        myCursor.execute(comando,valores)

        myCursor.execute('select * from SECCIONES_X_ESTUDIANTES')

        for x in myCursor:
            print(x)

if Menu_Op == 5:
    print("Que desea Listar: \n\
-Estudiantes\n\
-Materia\n\
-Profesores\n\
-Carrera\n\
-Materia por Carrera\n\
-Secciones por Estudiantes\n\
-Secciones por Profesores\n ")
    op = input("Ingrese el nombre de lo que desea Listar: \n")
    if op == "Estudiantes":
        myCursor.execute('select * from estudiantes')
        for x in myCursor:
            print(x)
            
    if op == "Materia":
        myCursor.execute('select * from materias')
        for x in myCursor:
            print(x)

    if op == "Profesores":
        myCursor.execute('select * from profesores')
        for x in myCursor:
            print(x)

    if op == "Carrera":
        myCursor.execute('SELECT * from carrera')
        for x in myCursor:
            print(x)

    if op == "Materia por Carrera":
        myCursor.execute('SELECT * from MATERIA_X_CARRERA')
        for x in myCursor:
            print(x)

    if op == "Secciones por Estudiantes":
        myCursor.execute('SELECT * from SECCIONES_X_ESTUDIANTES')
        for x in myCursor:
            print(x)

    if op == "Secciones por Profesores":
        myCursor.execute('SELECT * from SECCIONES_X_ESTUDIANTES')
        for x in myCursor:
            print(x)

        
print("Fin del programa!!!!! ")


 
       





