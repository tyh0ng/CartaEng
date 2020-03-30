import json
from flask import Flask, escape, request, jsonify, abort

app = Flask(__name__)

with open('../data/pokemon.json') as f:
  data = json.load(f)

POKEMON_TYPES = ['normal', 'fire', 'fighting', 'water', 'flying', 'grass', 'poison', \
    'electric', 'ground', 'psychic', 'rock', 'ice', 'bug', 'dragon', 'ghost', 'dark', 'steel', 'fairy']

@app.route('/pokemon/info/<int:pokemon_id>', methods=['GET'])
def get_info_by_id(pokemon_id):
    if pokemon_id < 1 or pokemon_id > len(data):
        abort(404)

    return jsonify({'pokemon': data[pokemon_id - 1]})

@app.route('/pokemon/names/english', methods=['GET'])
def get_all_names_english():
    names = []
    for pokemon in data:
        names.append(pokemon['name']['english'])

    return jsonify({'names': names})

@app.route('/pokemon/names/japanese', methods=['GET'])
def get_all_names_japanese():
    names = []
    for pokemon in data:
        names.append(pokemon['name']['japanese'])

    return jsonify({'names': names})

@app.route('/pokemon/names/chinese', methods=['GET'])
def get_all_names_chinese():
    names = []
    for pokemon in data:
        names.append(pokemon['name']['chinese'])

    return jsonify({'names': names})

@app.route('/pokemon/names/french', methods=['GET'])
def get_all_names_french():
    names = []
    for pokemon in data:
        names.append(pokemon['name']['french'])

    return jsonify({'names': names})

@app.route('/pokemon/type/<pokemon_type>', methods=['GET'])
def get_pokemon_by_type(pokemon_type):
    pokemon_type = pokemon_type.lower()
    if pokemon_type not in POKEMON_TYPES:
        abort(404)

    pokemon_with_type = []
    for pokemon in data:
        if pokemon['type'][0].lower() == pokemon_type or \
                (len(pokemon['type']) > 1 and pokemon['type'][1].lower() == pokemon_type):

            pokemon_with_type.append(pokemon)

    return jsonify({'pokemon_with_type': pokemon_with_type})

    
