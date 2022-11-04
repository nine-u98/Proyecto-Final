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

    def guardaLibro(self):
        pass

    def eliminar_libro(self):
        pass

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
