from flask import Flask, render_template
import urllib.request, json


app = Flask(__name__)


@app.route("/") #ok
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
    
    return render_template("profile.html", profile = character_data)

@app.route("/lista") #Personagens em formato JSON

def get_list_characters():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)
    
    characters = []

    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"],
            "origin": character["origin"],
            "location": character["location"],
            "episode": character["episode"]
        }
        
        characters.append(character)
    return {"characters":characters}

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
    url = "https://rickandmortyapi.com/api/episode?page=2" # abre a URL do api onde estão os episódios
    response = urllib.request.urlopen(url)  # envia a requisição e armezena os dados retornados
    episodes = response.read()  # lê os dados recebidos
    dict = json.loads(episodes) # carrega os dados em json 

    return render_template("episodes.html", episodes = dict["results"]) # mostra os resultados no template criado

# Criando uma rota para a lista de episódios em JSON:
@app.route("/listepisodes")

def get_episodes():
    url = "https://rickandmortyapi.com/api/episode?page=2"
    response = urllib.request.urlopen(url) 
    episodes = response.read() 
    dict = json.loads(episodes) 
    episodes = [] # cria uma lista onde serão armazenados os episódios
    
    for episode in dict["results"]: 
        episode = {  # cria um dicionário com as informações requisitadas de cada ep. para que sejam adicionados na lista
            "episode":episode["episode"],
            "name":episode["name"],
            "air_date":episode["air_date"],
            "id":episode["id"]
        }        
        episodes.append(episode) # adiciona os dados do episódio na lista

    return {"episodes":episodes} # retorno da lista de episódios

# Rota carregar o perfil do episódio
@app.route("/episode/<id>")
def get_profile_episode(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url) 
    data = response.read() 
    episode_data = json.loads(data)    

    characters = []
    for character_url in episode_data["characters"]:
        response = urllib.request.urlopen(character_url)
        character_data = json.loads(response.read())
        characters.append({
            "id": character_data["id"],
            "name": character_data["name"]
        })
    
    return render_template("episode.html", episode=episode_data, characters=characters)
    
