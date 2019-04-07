### Ejemplo: insert into ventas (codpro, codpie, codpj, cantidad, fecha) values('S1', 'P1', 'J1', 150, to_date('18/09/1997','dd/mm/yyyy'));

from random import randint, random
import datetime, os, sys

#Declaración de variables globales

sentencia = "insert into ventas (codpro, codpie, codpj, cantidad, fecha) values(";

proveedores = ['S1','S2','S3','S4','S5']
piezas = ['P1','P2','P3','P4','P5']
proyectos = ['J1','J2','J3','J4']

#Año,mes,día
start_date = datetime.date(1999, 10, 5)
end_date = datetime.date(2015, 4, 19)

#Rango de valores que tomarán las cantidades
cantidad_min = 50
cantidad_max = 1000


#---------------
#Declaración de funciones

def getProveedor():
    tope = len(proveedores) - 1
    n = randint(0,tope)
    return proveedores[n]

def getPieza():
    tope = len(piezas) - 1
    n = randint(0,tope)
    return piezas[n]

def getProyecto():
    tope = len(proyectos) - 1
    n = randint(0,tope)
    return proyectos[n]

def getDate(start_date, end_date):
    number_of_days = (end_date - start_date).days
    days_random = randint(1, number_of_days)
    return(start_date + datetime.timedelta(days=days_random))

def getCantidad():
    c = randint(cantidad_min,cantidad_max)
    return c

def getVenta():
    codpro = "'" + getProveedor() + "'"
    codpie = "'" + getPieza() + "'"
    codpj = "'" + getProyecto() + "'"
    date = "to_date(" + "'" + str(getDate(start_date, end_date)) + "','dd/mm/yyyy'"
    cantidad = "'" + str(getCantidad()) + "'"
    tupla = sentencia + codpro + ", " + codpie + ", " + codpj + ", " + cantidad + ", " + date + "));"
    return tupla


# Fin declaración de funciones
# -------------------------------------------

if len(sys.argv) != 3 :
    print("Funcionamiento: ./programa num_tuplas_a_generar fichero.sql")
    exit()

ngenerar = sys.argv[1]
path = sys.argv[2]

file = open(path, 'w')

ngenerar = int(ngenerar)
for i in range(ngenerar):
    cadena = getVenta()
    file.write(cadena + '\n')

file.close()
print("Done.")
