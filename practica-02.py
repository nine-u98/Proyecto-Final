import requests
import time
from os import system


class Pokemon:
    def __init__(self):
        self.urlPokemon = 'https://pokeapi.co/api/v2/pokemon/'
        self.urlGeneracion = "https://pokeapi.co/api/v2/generation/"
        self.urlForma = "https://pokeapi.co/api/v2/pokemon-shape/"
        self.urlHabilidad = "https://pokeapi.co/api/v2/ability/"
        self.urlHabitat = "https://pokeapi.co/api/v2/pokemon-habitat/"
        self.urlTipo = "https://pokeapi.co/api/v2/type/"

    def __conect(self, url: str):
        r = requests.get(url)
        status = r.status_code
        if status != 200:
            quit()
        else:
            return r.json()

    def all_pokemons(self, types: str):
        if types:
            pokeRes = self.__conect(types)
            if types == self.urlHabilidad or types == self.urlTipo:
                lista: list = [i['name'] for i in pokeRes["results"]]
            else:
                lista = [pokeRes["results"][i]["name"] for i in range(int(pokeRes["count"]))]
            print("Selecciona una opcion")
            for index, item in enumerate(lista, 1):
                print(f'{index}) {item.capitalize()}')
            res = ""
            while res not in range(1, len(lista) + 1):
                res = int(input("Ingresa un número comprendido en la lista: "))
                if res == 19:
                    print("Pokemon no encontrado")
            listpokemon = self.__conect(types + (str(res)))
            if types == self.urlHabilidad or types == self.urlTipo:
                for i in range(len(listpokemon["pokemon"])):
                    nomPokemon = listpokemon["pokemon"][int(i)]["pokemon"]["name"]
                    self.details(nomPokemon)
            else:
                for i in range(len(listpokemon["pokemon_species"])):
                    nomPokemon = listpokemon["pokemon_species"][int(i)]["name"]
                    self.details(nomPokemon)

    def details(self, nombre):
        infopokemon = self.__conect(self.urlPokemon + nombre)
        print(nombre.upper())
        print("\tImagen: ", infopokemon['sprites']['front_default'])
        print("\tHabilidades:")
        for j in infopokemon["abilities"]:
            print("\t\t*", j["ability"]["name"].capitalize())


if __name__ == '__main__':
    obj = Pokemon()
    while True:
        print("""\
"OPCIONES A SELECCIONAR:

1) Listar por generación.
2) Listar por forma.
3) Listar por habilidad.
4) listar por habitat.
5) Listar por tipo.""")
        options = input("Ingresar número de la opción a listar: ").strip()
        match options:
            case '1':
                obj.all_pokemons(obj.urlGeneracion)
                break
            case '2':
                obj.all_pokemons(obj.urlForma)
                break
            case '3':
                obj.all_pokemons(obj.urlHabilidad)
                break
            case '4':
                obj.all_pokemons(obj.urlHabitat)
            case '5':
                obj.all_pokemons(obj.urlTipo)
                break
            case _:
                print("Debe ingresar un número entre el 1 al 6.")
                time.sleep(1)
                system('clear')
