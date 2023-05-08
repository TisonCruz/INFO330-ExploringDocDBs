import sqlite3
from pymongo import MongoClient

# Connect to MongoDB
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']




def some_function(pokemonid):
   return pokemonColl.find_one({"pokedex_number":pokemonid})


generalquery = (
    'SELECT name, pokedex_number, pokemon_type_view.type1, pokemon_type_view.type2, hp, attack, defense, speed, sp_attack, sp_defense'
    'FROM pokemon'
    'JOIN pokemon_types_view'
    'ON pokemon.name = pokemon_types_view.name'
)
abilityquery = (
    'SELECT ability.name'
    'FROM ability'
    'JOIN pokemon'
    'ON ability.id = pokemon.id'
)

# CReate a dict containing a key-value array in JSON format
pokemon = {
       "name": generalquery[1],
       "pokedex_number": generalquery[2],
       "types": [generalquery[3],   generalquery[4]],
       "hp": generalquery[5],
       "attack": generalquery[6],
       "defense": generalquery[7],
       "speed": generalquery[8],
       "sp_attack": generalquery[9],
       "sp_defense": generalquery[10],
       "abilities": abilityquery
   }
# Add dictionary to collection
pokemonColl.insert_one(pokemon)


pikachu = pokemonColl.find_one({"name": "Pikachu"})