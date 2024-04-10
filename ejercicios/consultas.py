import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("personal.db")
# insertar 2 departamentos
#conn.execute(
#    """
#    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion)
#    VALUES ("Ventas", "10-04-2020")
#    """
#)
#conn.commit()
#conn.execute(
#    """
#    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion)
#    VALUES ("Marketing", "11-04-2020")
#    """
#)
#conn.commit()

# Crear 3 nuevos cargos

#conn.execute(
#    """
#    INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
#    VALUES ("Gerente de Ventas", "Senior", "10-04-2020")
#    """
#)
#conn.commit()

#conn.execute(
#    """
#    INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
#    VALUES ("Analista de Marketing", "Junior", "11-04-2020")
#    """)
#conn.commit()

#conn.execute(
#    """
#    INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
#    VALUES ("Representante de Ventas", "Junior", " 12-04-2020")
#    """
#)

#conn.commit()

#Crear 2 nuevos Empleados
#conn.execute(
#    """
#    INSERT INTO EMPLEADOS (nombre, apellido_paterno, apellido_materno, fecha_contratcion, departamento_id, cargo_id, fecha_creacion)
#    VALUES ("Juan","Gonzales","Perez","15-05-2023",1,1,"15-05-2023")
#    """
#)
#conn.commit()
#conn.execute(
#    """
#    INSERT INTO EMPLEADOS (nombre, apellido_paterno, apellido_materno, fecha_contratcion, departamento_id, cargo_id, fecha_creacion)
#    VALUES ("Maria","Lopez","Martinez","20-06-2023",2,2,"20-06-2023")
#    """
#)
#conn.commit()
#Registrar dos Salarios 
#conn.execute(
#    """
#    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio,fecha_fin,fecha_creacion)
#    VALUES (1,3000,"01-04-2024","30-04-2025","01-04-2024")
#   """
#)
#conn.commit()
#conn.execute(
#    """
#    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio,fecha_fin,fecha_creacion)
#    VALUES (2,3500,"01-07-2023","30-04-2024","01-04-2024")
#    """
#)
#conn.commit()

# Listar datos de matriculación
#print("\nlISTAR EMPLEADOS:")
#cursor = conn.execute(
#    """
#    SELECT EMPLEADOS.id, EMPLEADOS.nombre, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, SALARIOS.salario
#    FROM SALARIOS
#    JOIN EMPLEADOS ON SALARIOS.empleado_id = EMPLEADOS.id
#    """
#)
#for row in cursor:
#    print(row)
    

    
conn.execute(
    """
    UPDATE EMPLEADOS
    SET cargo_id = 3
    WHERE id = 2
    """
)
conn.execute(
    """
    UPDATE SALARIOS
    SET salario = 3600
    WHERE empleado_id = 2
    """
)
conn.commit()
#Eliminar EMPLEADO
conn.execute(
    """
    DELETE FROM EMPLEADOS
    WHERE id = 2
    """
)
#ELIMINAR SUELDO
conn.execute(
    """
    DELETE FROM SALARIOS
    WHERE id = 2
    """
)


#

print("\nlISTAR EMPLEADOS cargo departamento:")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.id, EMPLEADOS.nombre, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, DEPARTAMENTOS.nombre, CARGOS.nombre
    FROM EMPLEADOS
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
    JOIN CARGOS ON EMPLEADOS.cargo_id = CARGOS.id
    
    """
)
for row in cursor:
    print(row)
    
    
conn.execute(
    """
    INSERT INTO EMPLEADOS (nombre, apellido_paterno, apellido_materno, fecha_contratcion, departamento_id, cargo_id, fecha_creacion)
    VALUES ("Carlos","Sanchez","Rodriguez","09-04-2024",1,3,"9-04-2024")
    """
)
conn.commit()

conn.execute(
    """
    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio,fecha_fin,fecha_creacion)
    VALUES (2,3500,"05-05-2023","05-012-2024","5-05-2023")
    """
)
conn.commit()

    
  
 
print("\nlISTAR EMPLEADOS cargo departamento:")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombre, EMPLEADOS.apellido_paterno,EMPLEADOS.apellido_materno, DEPARTAMENTOS.nombre , CARGOS.nombre, SALARIOS.salario 
    FROM EMPLEADOS 
    JOIN DEPARTAMENTOS  ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
    JOIN CARGOS  ON EMPLEADOS.cargo_id = CARGOS.id
    JOIN SALARIOS ON EMPLEADOS.id = SALARIOS.empleado_id;
    """
)
for row in cursor:
    print(row)
conn.commit()
conn.close()









