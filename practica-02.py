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
        
    def __conect(self):
        pass

    # * Funcion - obtener los datos de generacion & forma & habilidad
    def func_general(self):
        pass
    
    def pokeHabitat(self):
        pass

    def pokeTipo(self, nombre):

        pass

    def details(self):
        pass



if __name__ == '__main__':
    pass
