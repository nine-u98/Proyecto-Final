import pandas as pd
import time
import sys
from os import system

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
        pd.set_option('display.max_rows', None)
        self.libros = pd.read_csv(csv)  # index_col=0

    def listarLibros(self):
        print(self.libros)

    def ordenarLibros(self):
        print(self.libros.sort_values(by="Titulo", ascending=True).head(8))

    def buscarLibro(self, cat, search):
        data = self.libros.columns.tolist()[cat-1]
        match data:
            case 'ISBN':
                dataFrame = self.libros[self.libros['ISBN'] == search]
                return dataFrame
            case _:
                dataFrame = self.libros[self.libros[data].str.contains(search)]
                return dataFrame
            
    def buscar_num_Autores(self):
        pass

    def agregarlibro(self):
        indice = [i for i in self.dt.index][-1] + 1

        for i in list(self.dt.columns.values):
            if i.lower() in ['id']:
                print(int(self.dt['ID'].tail(1)) + 1)
                self.dt.loc[indice, i] = int(self.dt['ID'].tail(1)) + 1
            else:
                x = input(f"Valor a agregar {i} : ")    # input
                self.dt.loc[indice, i] = x
        self.guardalibro()

    def actualizarlibro(self):
        y = int(input("Ingresa el index de la fila : "))   # input
        for i in list(self.dt.columns.values):
            if i.lower() == ['id']:

                self.dt.loc[i, i] = int(self.dt['ID'].tail(1)) + 1
            x = input(f"Valor a modificar {i} : ")  # input
            self.dt.loc[y, i] = x

    def guardaLibro(self):
        pass

    def eliminar_libro(self):
        pass

if __name__ == '__main__':

    pass

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
