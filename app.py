from flask import Flask
from flask import render_template 
import urllib.request, json


app = Flask(__name__) 

@app.route('/') 
def get_list_elements_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url) 
    data = response.read() 
    dict = json.loads(data) 
    
    return render_template("characters.html", characters=dict['results'])

# Obter um personagem
@app.route('/profile/<id>') 
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/"+ id 
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    
# pega os ids dos episodios
    list_episodes_ids = []   
    for episode in dict['episode']:
        episode_id = episode.split("/")[-1]
        list_episodes_ids.append(episode_id)
        
# pega o id da localização do personagem 
    location_id= dict["location"]["url"].split("/")[-1]
    
#Converte os elementos da lista para inteiro 
    list_episodes_ids = [int(id) for id in list_episodes_ids]
   
#Consulta para montar os dados do episodio    
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url) 
    data = response.read()
    episodes_dict = json.loads(data) 
    
    episodes_found = []
    
    for episode in episodes_dict["results"]:
        if episode["id"] in list_episodes_ids:
            episodes_found.append ({
            "id":episode["id"],
            "name":episode["name"],
            "episode":episode["episode"]
        })
            
# Verifica erros de episódios
    if not episodes_found:
        error_message = "Episódios não encontrados."
        return render_template("profile.html", profile=dict, error_message=error_message, location_id=location_id)

    return render_template("profile.html", profile=dict, episodes_found=episodes_found, location_id=location_id)

# Listando elementos de uma busca
@app.route('/lista')
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