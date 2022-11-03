import pandas as pd


class Libro():

    def __init__(self, csv):
        pd.set_option('display.max_rows', None)
        self.libros = pd.read_csv(csv)  # index_col=0

    def listarLibros(self):
        print(self.libros)

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

    def guardaLibro(self):
        pass

    def eliminar_libro(self):
        pass


if __name__ == '__main__':
    pass
