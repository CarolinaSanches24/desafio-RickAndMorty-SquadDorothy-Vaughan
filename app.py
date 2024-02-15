from flask import Flask, render_template
import urllib.request, json

app = Flask (__name__)

@app.route("/") # rota de  URL raiz
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url) # envia a req e recebe a res
    data = response.read(); # leitura dos dados vindos da api
    dict = json.loads(data); # transforma esses dados em json p/ python
    
    return render_template("characters.html", characters = dict["results"])

@app.route("/profile/<id>") # obter um personagem

def get_profile(id):
    url = "https://rickandmortyapi.com/api/character"+id
    response = urllib.request.urlopen(url) 
    data = response.read()
    dict = json.loads(data)
    
    return render_template("profile.html", profile = dict)

@app.route("/lista")

def get_list_characters():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)
    
    characters = []
    
    for character in dict["results"]:
        character = {
            "name":character["name"],
            "status":character["status"]
        }
        
        characters.append(character)
    return {"characters":characters}

# Criando uma rota para episódios:
@app.route("/episodes")  

def get_list_episodes_page():
    url = "https://rickandmortyapi.com/api/episode" # abre a URL do api onde estão os episódios
    response = urllib.request.urlopen(url)  # envia a requisição e armezena os dados retornados
    episodes = response.read()  # lê os dados recebidos
    dict = json.loads(episodes) # carrega os dados em json 

    return render_template("episodes.html", episodes = dict["results"]) # mostra os resultados no template criado

# Criando uma rota para a lista de episódios em JSON:
@app.route("/listepisodes")

def get_episodes():
    url = "https://rickandmortyapi.com/api/episode"
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

#Criando uma rota para detalhes de um episódio específico, de acordo com o id:    
# @app.route("/episode/<id>") 

# def get_episode(id):
#     url = f"https://rickandmortyapi.com/api/episode/{id}"
#     response = urllib.request.urlopen(url) 
#     data = response.read(); 
#     episode_dict = json.loads(data)
    
#     return render_template("episode.html", episode=episode_dict) # mostra os detalhes do episódio no template criado