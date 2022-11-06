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


    def pokehabilidad(self):
        data = self.__conect(self.urlHabilidad)
        lista: list = [i['name'] for i in data["results"]]

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

        listpokemon = self.__conect(self.urlHabilidad + (str(res)))

        for i in range(len(listpokemon['pokemon'])):  # cambiar para mostrar menos
            nomPokemon = listpokemon['pokemon'][i]["pokemon"]["name"]

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
        pokeRes = self.__conect(self.urlHabitat)
        lista = [pokeRes["results"][i]["name"] for i in range(int(pokeRes["count"]))]
        print("Selecciona una opcion")
        for index, item in enumerate(lista, 1):
            print(f'{index}) {item.capitalize()}')
        res = ""
        while res not in range(1, len(lista) + 1):
            res = int(input("Ingresa un número comprendido en la lista: "))
        listpokemon = self.__conect(self.urlHabitat + (str(res)))

        for i in range(len(listpokemon["pokemon_species"])):  # cambiar para mostrar menos
            nomPokemon = listpokemon["pokemon_species"][int(i)]["name"]
            self.details(nomPokemon)

    def poketype(self):
        pk_resp = self.__conect(self.urlTipo)
        lista = [pk_resp["results"][i]["name"] for i in range(int(pk_resp["count"]))]
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
                nomPokemon = listpokemon["pokemon"][int(i)]["pokemon"]["name"]
                self.details(nomPokemon)
    def details(self):
        pass



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
                obj.poke_generacion()
                break
            case '2':
                obj.pokeforma()
                break
            case '3':
                obj.pokehabilidad()
                break
            case '4':
                obj.pokeHabitat()
                break
            case '5':
                obj.poketype()
                break
            case _:
                print("Debe ingresar un número entre el 1 al 6.")
