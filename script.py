#Procesa el CSV, filtra mayores de edad y los inserta en una tabla SQL.
import csv
import sqlite3

#Conectamos a base de datos 
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

#Crear tabla si no existe

cursor.execute('''
               CREATE TABLE IF NOT EXISTS usuarios_mayores (
                   nombre TEXT,
                   correo TEXT,
                   edad INTEGER
                   )
                   '''
)

# Leer archivo CSV y procesar
with open('usuarios.csv', newline='') as infile, open("mayores.csv", "w", newline="") as outfie:
     reader = csv.DictReader(infile)
     writer = csv.DictWriter(outfie, fieldnames=reader.fieldnames)
     writer.writeheader()
     
     for row in reader:
         if int(row['edad']) >= 18:
             writer.writerow(row)
             cursor.execute("INSERT INTO usuarios_mayores values (?, ?, ?)", (row["nombre"], row["correo"], int(row["edad"])))

#Guardar cambios
conn.commit()
#Cerrar conexion
conn.close()

print("Proceso completado.")             

print("")
print("")
print("+++++++++++++++++++++++++++++++")
print("")
print("")


# Leer el contenido del archivo
with open("usuarios.csv") as f:
    reader = csv.DictReader(f)
    print("Nombre de los usuarios y su edad ")
    for row in reader:
        print(row["nombre"], row["edad"])

print("")
print("")        
print("+++++++++++++++++++++++++++++++")
print("")
print("")        
        
# escribir 

with open("out.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["nombre","edad"])
    writer.writeheader()
    writer.writerow({"nombre":"Juan","edad":22})
    
    
print("Archivo out.csv creado")

