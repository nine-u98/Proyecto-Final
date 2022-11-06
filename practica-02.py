import requests

 

# listar pokemons involucra: nombre, habilidad y URL de la imagen
class Pokemon:
    def __init__(self):

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
    
    def pokeHabitat(self):
        pass

    def pokeTipo(self, nombre):

        pass

    def details(self):
        pass



if __name__ == '__main__':
    pass
