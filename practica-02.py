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


    def conect(self):
        pass
        
    def __conect(self, url):
        r = requests.get(url)
        status = r.status_code
        if status != 200:
            quit()

    # * Funcion - obtener los datos de generacion & forma & habilidad
    def func_general(self):
        pass
    
    def pokeHabitat(self):
        self.__pokeRes = self.__conect(self.urlHabitat)
        lista = [self.__pokeRes["results"][i]["name"] for i in range(int(self.__pokeRes["count"]))]
        print("Selecciona una opcion")
        for index, item in enumerate(lista, 1):
            print(f'{index}) {item.capitalize()}')
        res = ""
        while res not in range(1, len(lista) + 1):
            res = int(input("Ingresa un número comprendido en la lista: "))
        listpokemon = self.__conect(self.urlHabitat + (str(res)))

        for i in range(len(listpokemon["pokemon_species"])): #cambiar para mostrar menos
            self.nomPokemon = listpokemon["pokemon_species"][int(i)]["name"]
            self.details(self.nomPokemon)

    def pokeTipo(self):
        self.__pokeRes = self.__conect(self.urlTipo)
        lista = [self.__pokeRes["results"][i]["name"] for i in range(int(self.__pokeRes["count"]))]
        print("Selecciona una opcion")
        for index, item in enumerate(lista, 1):
            print(f'{index}) {item.capitalize()}')
        res = ""
        while res not in range(1, len(lista) + 1):
            res = int(input("Ingresa un número comprendido en la lista: "))
        if res == 19:
            res = 10001
            print("No hay ningún Pokemón agregado a esta lista.")
        elif res == 20:
            res = 10002
            print("No hay ningún Pokemón agregado a esta lista.")
        listpokemon = self.__conect(self.urlTipo + (str(res)))
        for i in range(len(listpokemon["pokemon"])):  # cambiar para mostrar menos
            self.nomPokemon = listpokemon["pokemon"][int(i)]["name"]
            self.details(self.nomPokemon)
    def details(self):
        pass



if __name__ == '__main__':
    pass
