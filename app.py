from flask import Flask, render_template
import urllib.request, json


app = Flask(__name__)


@app.route("/") 
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url) # envia a req e recebe a res
    data = response.read() # leitura dos dados vindos da api
    dict = json.loads(data) # transforma esses dados em json p/ python
    
    return render_template("characters.html", characters = dict["results"])

@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/"+id
    response = urllib.request.urlopen(url) 
    data = response.read(); 
    character_data = json.loads(data);
    location_id= character_data["location"]["url"].split("/")[-1]
    return render_template("profile.html", profile = character_data, location_id=location_id)

@app.route("/locations") # rota de locations
def get_list_locations_page():
        url = "https://rickandmortyapi.com/api/location"
        response = urllib.request.urlopen(url) # envia a req e recebe a res
        data = response.read(); # leitura dos dados vindos da api
        locations_data = json.loads(data); # transforma esses dados em json p/ python
    
        locations = [];
    
        #para cada localizacao cria um objeto com id, nome, tipo e dimensao
        for location in locations_data["results"]:
            location = {
                "id":location["id"],
                "name":location["name"],
                "type":location["type"],
                "dimension":location["dimension"]
            }
            # adiciona esse elemento a lista de localizações
            locations.append(location)
        #envia os dados para o template locations.html
        return render_template("locations.html", locations = locations_data["results"])


@app.route("/location/<id>") # obter uma location
def get_location(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url)
    location_data = response.read()
    location_dict = json.loads(location_data)
    
    characters = []

    for character_url in location_dict.get("residents", []):
        response = urllib.request.urlopen(character_url)
        character_data = response.read()
        character_dict = json.loads(character_data)
        characters.append({
            "id": character_dict["id"],
            "name": character_dict["name"]
        })
    
    return render_template("location.html", location=location_dict, characters=characters)

# Criando uma rota para episódios:
@app.route("/episodes")
def get_list_episodes_page():
    all_episodes = [] # cria uma lista para armazenar todos os episódios

    for page in range(1, 4):  # cria um loop para puxar os episódios de todas as páginas 
        url = f"https://rickandmortyapi.com/api/episode?page={page}" # abre a URL do api onde estão os episódios
        response = urllib.request.urlopen(url) # envia a requisição e armezena os dados retornados
        episodes = response.read() # lê os dados recebidos
        dict = json.loads(episodes) # carrega os dados em json 
        all_episodes.extend(dict["results"]) # adiciona os dados carregados de cada página na lista

    return render_template("episodes.html", episodes=all_episodes) # mostra os resultados no template criado

# Rota carregar o perfil do episódio
@app.route("/episode/<id>")
def get_profile_episode(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url) # envie a requisição e armazena os dados retornados
    data = response.read() # leitura dos dados vindo da API
    episode_data = json.loads(data) # transforma esses dados em json p/ python

    characters = [] # cria uma lista vazia para os personagens
    for character_url in episode_data["characters"]: # for para listar todos os personagens do episódio
        response = urllib.request.urlopen(character_url) # envie a requisição e armazena os dados retornados
        character_data = json.loads(response.read()) # transforma os dados em JSON e faz a leitura
        characters.append({ # insere o id e nome dos personagens em um dicionário
            "id": character_data["id"],
            "name": character_data["name"]
        })
    
    return render_template("episode.html", episode=episode_data, characters=characters)
    
