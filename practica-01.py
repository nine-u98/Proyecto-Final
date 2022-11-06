import time
from os import system
import sys
import pandas as pd

def borrar():
    num = input("Ingresa el numero de la fila a borrar : ")
    if num.isdecimal():
        num = int(num)
        return num
    else:
        print("No es un numero")
def timing():
    for i in range(10, 0, -1):
        sys.stdout.write(str('█'))
        sys.stdout.flush()
        time.sleep(1)
    print("\n")


def again(x="Quieres volver al menu? [s/n] : "):
    inpt = input(x).lower().strip() in ['s', 'si']
    if inpt:
        system('clear')
        if x == "Quieres volver al menu? : ":
            menu()
        return True
    elif inpt in ['n', 'no']:
        return False
    else:
        print('Valor ingresado desconocido')
        return False


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
    if cat == 3:
        print(f"""\
Estos son los ISBN copia al que quieres buscar        
{obj.dt["ISBN"]}""")

    if 6 > cat >= 1:
        search = input("Texto a buscar : ")
        print(obj.buscarlibro(cat, search))


class Libro():
    def __init__(self, csv):
        self.libros = csv
        pd.set_option('display.max_rows', None)
        self.dt = pd.read_csv(self.libros)  # index_col=0
        self.dt['ID'] = self.dt['ID'].astype(str).replace('\.0', '', regex=True)

    def listarlibros(self):
        print(self.dt)

    def ordenarlibros(self):
        print(self.dt.sort_values(by="Titulo", ascending=True).head(8))

    def buscarlibro(self, cat, search):
        if cat in self.dt.columns.values:           # Verificar funcionamiento
            data = self.dt.columns.tolist()[cat - 1]
            match data:
                case 'ISBN':
                    dataFrame = self.dt[self.dt['ISBN'] == int(search)]
                    return dataFrame
                case _:
                    dataFrame = self.dt[self.dt[data].str.contains(search)]
                    return dataFrame
        else:
            print("No esta en las categorias")

    def buscar_num_autores(self, num):
        self.numAutores = num
        dictcc = {}
        for e, i in enumerate([i for i in self.dt['Autor']]):
            dictcc[e] = i.count(',') + 1
        print([self.dt.iloc[[i]] for i in dictcc.keys() if dictcc[i] == self.numAutores])

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

    def guardalibro(self):
        self.dt.to_csv(self.libros, index=False)
        print("Archivo guardado")

    def eliminar_libro(self, num): # validar q num este en el rango de los indices
        self.dt.drop(num, inplace=True)
        self.dt.to_csv(self.libros)
        print(f"Eliminando")

if __name__ == '__main__':
    if again("Quieres iniciar la lectura de un archivo CSV: "):
        ruta = input(r"Ingresa una ruta absoluta de la ubicacion de tu CSV sin la extension : ") + ".csv"
        if ruta:
            obj = Libro(ruta)
            print("Procesando archivo ...")
            #timing()
            if again("Quieres ver opciones "):
                while True:
                    menu()
                    options = input("=> ")
                    match int(options):
                        case 1:
                            obj.listarlibros()
                            again()
                        case 2:
                            obj.agregarlibro()
                            again()
                        case 3:
                            obj.listarlibros()
                            obj.eliminar_libro(borrar())
                            again()
                        case 4:
                            modlibros()
                            again()
                        case 5:
                            obj.ordenarlibros()
                            again()
                        case 6:
                            numAutores = int(input("Ingresa un numero de autores a buscar : "))
                            obj.buscar_num_autores(numAutores)
                            again()
                        case 7:
                            obj.listarlibros()
                            obj.actualizarlibro()
                            again()
                        case 8:
                            obj.guardalibro()
                            again()
                        case 9:
                            print("Hasta la proxima!")
                            break
                        case _:
                            print("Selecciona una de las opciones permitidas")
                            time.sleep(1)

    else:
        print("Hasta la proxima!")
