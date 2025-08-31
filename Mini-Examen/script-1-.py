import csv
import sqlite3


#conexion con la base de datos
conn = sqlite3.connect('datos.db')
cursor = conn.cursor()

#Crear tabla si no existe
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS usuarios_mayores(
        nombre TEXT,
        edad INTEGER
        
    )
    '''
)


#Leer el archivo csv
with open ('datos.csv', newline='') as infile, open('mayores.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    #procesar cada fila
    for row in reader:
        if int(row['edad']) >= 18:
            writer.writerow(row)
            cursor.execute("INSERT INTO usuarios_mayores values (?, ?)", (row["nombre"], int(row["edad"])))
            
#Guardar cambios
conn.commit()



#leer el contenido del archivo con los usuarios de menor edad
print("")
print("++++++++++++++++++++++++++++++++")
print("")
#Guardar en otro archivo los usuarios de menor edad
with open('datos.csv') as f, open('menores.csv', 'w', newline='') as outfie:
    reader = csv.DictReader(f)
    writer = csv.DictWriter(outfie, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        if int(row['edad']) < 18:
            print(row["nombre"], row["edad"])
            writer.writerow(row)
            
print("Insertar un usuario")

cursor.execute('INSERT INTO usuarios_mayores values (?, ?)', ('carlos', 30))
conn.commit()

for row in cursor.execute('select * from usuarios_mayores'):
    print(row)
print("Usuario insertado.")


print("")
print("Consulta en base de datos")


for row in cursor.execute('select * from usuarios_mayores where edad >= 20 '):
    print(row)
    
conn.close()



print("Actualizacion completada.")