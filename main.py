import os.path
import pickle
import time
from modulo import *


def menu():
    print('MENU DE OPCIONES'
          '\n1- Mostrar Totales'
          '\n2- SALIR')
    op = int(input('Ingrese su opcion: '))
    return op


def add_in_order(v, venta):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].nombre == venta.nombre:
            pos = c
            break
        if venta.nombre < v[c].nombre:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [venta]


def leer_archi():
    ar = 'noviembre_22.txt'
    suma = 0
    verdus = 0
    vino = 0
    boxes_t = (4 + 6 + 2 + 1 + 2 + 2)
    boxes = (14000 + 15000 + 5000 + 3500 + 7000 + 6000)
    guille_dio = (247700 + 30000 + 25000 + 60000 + 16000 + 14400)
    vinos = ('Al Campo ', 'Boulevard Sarmiento ', 'Baracat Rivera ', 'Alberto Duarte Quirós ', 'Mabel ', 'Viejo Molino ', 'Drinks cordillera ', 'Vinoteca Tomate ', 'Drinks Tejeda ', 'Vanguardia ', 'Tinto y Blanco ', 'Drinks Recta ', 'La Cava ', 'Las Condes ', 'Cosecha Tardia ', 'Belen ', 'La Cava ', 'Fran Catamarca ', 'Barrica ', 'C&C ', 'Fratelli ', 'Marchelino ', 'Fondo Blanco ', 'Al Campo Warcalde ', 'Alm Mario ', 'Tijuana arroyito ', 'Tijuana ', 'Mae ', 'Daddy ', 'Daddy Colon ', 'Vineria recta ', 'El Roble ', 'Frank ', 'Romi Calera ', 'La Nueva Bodega ', 'Vineria Nuniez ', 'Baco Rey ', 'Caucel ', 'Curry ', 'Leon Blanco ', 'Krusty ', 'Cava Gauss ', 'Almacen Bebidas ')
    m = open(ar, 'rt')
    for linea in m:
        #linea = linea[:-1]
        campos = linea.split('$')
        print('Local: ', campos[0], '|', 'Importe: ', campos[1])
        suma += int(campos[1])
        if campos[0] in vinos:
            vino += int(campos[1])
        else:
            verdus += int(campos[1])
    print('Cargando Ventas...')
    time.sleep(1)
    print('\nTOTAL DE VENTAS: ', '$', suma + boxes)
    print('\nVinotecas: ', '$', vino)
    print('\nCondimentos: ', '$', verdus)
    print('\nBoxes: ', '$', boxes)
    print('\nTOTAL DE Boxes vendidas: ', boxes_t)
    sueldo_v = (20 * vino / 100)
    sueldo_c = (25 * verdus / 100)
    box_sueldo = (boxes_t * 500)
    sueldo_t = sueldo_c + sueldo_v + box_sueldo
    print('Cargando Sueldos...')
    time.sleep(1)
    tot = suma + boxes
    print('\nEl sueldo total es: ', '$', sueldo_t)
    print('\nEl 25% de CONDIMENTOS: ', '$', sueldo_c)
    print('\nEl 20% de BOTANICOS: ', '$', sueldo_v)
    print('\n$500 por caja vendida: ', '$', boxes_t * 500)
    print('\nGuille dio: ', '$', guille_dio)
    print('\nDebe haber en casa: ', '$', tot - guille_dio)
    print('\nNafta: $5000')
    print('\nGrego DEBE: $4500')
    print('\nGuille DEBE: $12000')
    #sueldo_neto = sueldo_t - (0)
    print('\nSueldo Neto: ')
    m.close()


def cargar_archivo_vector(v):
    ar = 'noviembre_22.txt'
    m = open(ar)
    line = m.readline()
    line = line[:-1]
    while True:
        xs = m.readline()
        if xs == '':
            break
        if xs[-1] == '\n':
            xs = xs[:-1]
        x = xs
        v.append(x)

    m.close()
    return v


def mostrar_datos(v):
    elem_dato = 0
    for elem in v:
        print(elem)
        #if elem['$':-1] == '123456789':
            #elem = elem_dato
            #print(elem_dato)


def cargar(v):
    for i in range(len(v)):
        pass


def filtrar_datos(v):
    suma = 0
    for elem in v:
        if elem['$':-1]:
            pass


def main():
    v2 = []
    v = []
    op = 0
    while op != 6:
        op = menu()
        if op == 1:
            leer_archi()
            #cargar_archivo_vector(v)
        elif op == 2:
            mostrar_datos(v)
        elif op == 3:
            filtrar_datos(v)
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            print('Hasta Luego! ')
        else:
            print('Ingrese una opcion correcta')


if __name__ == '__main__':
    main()
