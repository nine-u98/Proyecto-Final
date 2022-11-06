import requests

 

# listar pokemons involucra: nombre, habilidad y URL de la imagen
class Pokemon:
    def __init__(self):
        pass
        
    def __conect(self):
        pass
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
         else:
            return r.json()
    def poke_generacion(self):
        pokeRes = self.__conect(self.urlGeneracion)
        lista = [pokeRes["results"][i]["name"] for i in range(int(pokeRes["count"]))]
        print("Selecciona una opcion")
        for index, item in enumerate(lista, 1):
            print(f'{index}) {item.capitalize()}')
        res = ""
        while res not in range(1, len(lista) + 1):
            res = int(input("Ingresa un número comprendido en la lista: "))
        listpokemon = self.__conect(self.urlGeneracion + (str(res)))
        for i in range(len(listpokemon["pokemon_species"])):  # cambiar para mostrar menos
            nomPokemon = listpokemon["pokemon_species"][int(i)]["name"]
            self.details(nomPokemon)
    
    def pokeforma(self):
        pokeRes = self.__conect(self.urlForma)
        lista = [pokeRes["results"][i]["name"] for i in range(int(pokeRes["count"]))]
        print("Selecciona una opcion")
        for index, item in enumerate(lista, 1):
            print(f'{index}) {item.capitalize()}')
        res = ""
        while res not in range(1, len(lista) + 1):
            res = int(input("Ingresa un número comprendido en la lista: "))
        listpokemon = self.__conect(self.urlForma + (str(res)))
        for i in range(len(listpokemon["pokemon_species"])):  # cambiar para mostrar menos
            nomPokemon = listpokemon["pokemon_species"][int(i)]["name"]
            self.details(nomPokemon)
    def pokeHabitat(self):
        pass

    def pokeTipo(self, nombre):

        pass

    def details(self):
        pass



if __name__ == '__main__':
    pass
