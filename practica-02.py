import requests


# listar pokemons involucra: nombre, habilidad y URL de la imagen
class Pokemon:
    def __init__(self, sel):
        self.sel = sel

    def __conect(self, url):
        r = requests.get(url)
        status = r.status_code
        if status != 200:
            quit()
        else:
            return r.json()
    
    def __conectaAPI(self, url):
        pass

    def __str__(self) -> None:
        pass

    # * Funcion - obtener los datos de generacion & forma & habilidad
    def funcion_universal(self):
        pass

    # ! Eliminar
    def pokeGeneracion(self):
        '''Listar pokemons por generación.
        Se ingresa alguna generación (1, 2, 3, ..)
        y se listan todos los pokemon respectivos.'''
        pass

    # ! Eliminar
    def pokeForma(self):
        '''Listar pokemons por forma. Se ingresa
        alguna forma (deben sugerir valores) y se
        listan todos los pokemons respectivos.'''
        pass

    # ! Eliminar
    def pokeHabilidad(self):
        '''Listar pokemons por habilidad. Se deben
        sugerir opciones a ingresar para interactuar.'''

    def pokeHabitat(self):
        pass

    def pokeDetalles(self, nombre):

        pass

    def pokeTipo(self):
        '''Listar pokemons por tipo. Se deben sugerir
        opciones a ingresar para interactuar.'''
        pass



if __name__ == '__main__':
    pass
