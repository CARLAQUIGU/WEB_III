# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("personal.db")

# Crear tabla de DEPARTAMENTOS
try :
    conn.execute(
        """
        CREATE TABLE DEPARTAMENTOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla DEPARTAMENTOS ya existe")

# Crear tabla de CARGOS
try :
    conn.execute(
        """
        CREATE TABLE CARGOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL
       );
        """
    )
except sqlite3.OperationalError:
    print("La tabla CARGOS ya existe")

# Crear tabla de empleados
try :
    conn.execute(
        """
        CREATE TABLE EMPLEADOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratcion DATE NOT NULL,
        departamento_id INTEGER NOT NULL,
        cargo_id INTEGER NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (departamento_id) REFERENCES departamentos(id),
        FOREIGN KEY (cargo_id) REFERENCES cargos(id)
        );
        """
    )
except sqlite3.OperationalError:
    print("La tabla EMPLEADOS ya existe")

# Crear tabla de SALARIOS
try :
    conn.execute(
        """
        CREATE TABLE SALARIOS
        (id INTEGER PRIMARY KEY,
        empleado_id INTEGER NOT NULL,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES empleados(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla SALARIOS ya existe")
    
# Confirmar cambios
conn.commit()

# Cerrar conexión
conn.close()