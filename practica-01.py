import sys
from os import system
import pandas as pd
import time

def again(x="Quieres volver al menu? : "):
    if input(x).lower().strip() in ['s', 'si']:
        system('clear')
        if x == "Quieres volver al menu? : ":
            menu()
        return True


def menu():
    print("""\
Lista de [OPCIONES]
Opción 1: Listar libros.
Opción 2: Agregar libro.
Opción 3: Eliminar libro.
Opción 4: Buscar libro por ISBN, Titulo, Autor, Genero, Editorial.
Opción 5: Ordenar libros por título.
Opción 6: Buscar libros por número de autores.
Opción 7: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).
Opción 8: Guardar libros en archivo de disco duro (.txt o csv).
Opcion 9: Finalizar programa""")


def modlibros():
    print("""\
Lista de categorias
1) Titulo
2) Genero
3) ISBN
4) Editorial
5) Autor""")
    cat = int(input('=> '))

    if 6 > cat >= 1:
        search = input("Texto a buscar : ")
        print(obj.buscarLibro(cat, search))
def timing():
    for i in range(10, 0, -1):
        sys.stdout.write(str('%') + ' ')
        sys.stdout.flush()
        time.sleep(1)
    print("\n")

class Libro():

    def __init__(self, csv):
        self.csv = csv
    def listarLibros(self):
        pass

    def ordenarLibros(self):
        pass

    def buscarLibro(self):
        pass
    def buscar_num_Autores(self):
        pass

    def agregarLibro(self):
        pass

    def actualizarLibro(self):
        pass

    def guardalibro(self):
        self.dt.to_csv(self.libros, index=False)
        print("Archivo guardado")

    def eliminar_libro(self, num): 
        self.dt.drop(num, inplace=True)
        self.dt.to_csv(self.libros)
        print(f"Eliminando")

if __name__ == '__main__':
    if again("Quieres iniciar la lectura de un archivo CSV: "):
        ruta = input(r"Ingresa una ruta absoluta de la ubicacion de tu CSV sin la extension : ") + ".csv"
        if ruta:
            obj = Libro(ruta)
            print("Procesando archivo ...")
            timing()

             if again("Quieres ver opciones "):
                system('clear')
                timing()
                menu()
                while True:
                    options = input("=> ")

                    match int(options):
                        case 1:
                            obj.listarLibros()
                            again()
                        case 2:
                            obj.agregarLibro()
                            again()
                        case 3:
                            obj.eliminar_libro()
                            again()
                        case 4:
                            modlibros()
                            obj.listarLibros()

                        case 5:
                            obj.ordenarLibros()
                            again()
                        case 6:
                            obj.buscar_num_Autores()
                            again()
                        case 7:
                            obj.actualizarLibro()
                            again()
                        case 8:
                            obj.guardaLibro()
                            again()
                        case 9:
                            break

    else:
        print("ad")
