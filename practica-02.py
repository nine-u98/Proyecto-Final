import requests


# listar pokemons involucra: nombre, habilidad y URL de la imagen
class Pokemon:
    def __init__(self):
        self.urlPokemon = 'https://pokeapi.co/api/v2/pokemon/'
        self.urlGeneracion = "https://pokeapi.co/api/v2/generation/"
        self.urlForma = "https://pokeapi.co/api/v2/pokemon-shape/"
        self.urlHabilidad = "https://pokeapi.co/api/v2/ability/"
        self.urlHabitat = "https://pokeapi.co/api/v2/pokemon-habitat/"
        self.urlTipo = "https://pokeapi.co/api/v2/type/"
        self.__pokeRes = ""

    def __pokeSeleccion(self):
        pass
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
