import pandas as pd
import time
import sys
from os import system


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

    def agregarLibro(self):
        pass

    def actualizarLibro(self):
        pass

    def guardaLibro(self):
        pass

    def eliminar_libro(self):
        pass


if __name__ == '__main__':
    pass
