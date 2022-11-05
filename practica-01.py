class Libro():

    def __init__(self, csv):
        self.csv = csv
    def listarLibros(self):
        pass

    def ordenarLibros(self):
        pass

    def buscarLibro(self):
        pass
    
    def buscar_num_autores(self, num):
        self.numAutores = num
        dictcc = {}
        for e, i in enumerate([i for i in self.dt['Autor']]):
            dictcc[e] = i.count(',') + 1
        print([self.dt.iloc[[i]] for i in dictcc.keys() if dictcc[i] == self.numAutores])

    def agregarlibro(self):
        pass

    def actualizarLibro(self):
        pass

    def guardaLibro(self):
        pass

    def eliminar_libro(self):
        pass


if __name__ == '__main__':
    pass
