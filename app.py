from flask import Flask, render_template
import urllib.request, json

app = Flask (__name__)

@app.route("/") # rota de  URL raiz
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url) # envia a req e recebe a res
    data = response.read() # leitura dos dados vindos da api
    dict = json.loads(data) # transforma esses dados em json p/ python
    
    return render_template("characters.html", characters = dict["results"])

@app.route("/profile/<id>") # obter um personagem

def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/"+id
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

# Rota carregar o perfil do episódio
@app.route("/episode/<id>")
def get_profile_episodes(id):
    url = "https://rickandmortyapi.com/api/episode/"+id
    response = urllib.request.urlopen(url) 
    data = response.read() 
    dict = json.loads(data)


    return render_template("episode.html", episode = dict)

