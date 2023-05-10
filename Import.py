import sqlite3  # This is the package for all sqlite3 access in Python
connection = sqlite3.connect("pokemon.sqlite")
con = connection.cursor()
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['anotherOne_10']
count = con.execute("Select count(*) from pokemon").fetchone()
counter = count[0]

for i in range (1, counter + 1):
    name = con.execute("Select name from pokemon where pokedex_number = "+ str(i) +";").fetchone()
    name1 = str(name[0])
    pokedex_number = i
    type1Id = con.execute("Select type_id from pokemon_type where pokemon_id = "+ str(i) +" and which = 1;").fetchone()
    type2Id = con.execute("Select type_id from pokemon_type where pokemon_id = "+ str(i) +" and which = 2").fetchone()
    type1 = con.execute("Select name from type where id ="+ str(type1Id[0]) +";").fetchone()
    type2 = con.execute("Select name from type where id ="+ str(type2Id[0]) +";").fetchone()
    types = [str(type1[0]), str(type2[0])]
    hp = con.execute("Select hp from pokemon where pokedex_number ="+ str(i) +";").fetchone()
    hp1 = str(hp[0])
    attack = con.execute("Select attack from pokemon where pokedex_number ="+ str(i) +";").fetchone()
    attack1 = int(attack[0])
    defense = con.execute("Select defense from pokemon where pokedex_number ="+ str(i) +";").fetchone()
    defense1 = str(defense[0])
    speed = con.execute("Select speed from pokemon where pokedex_number ="+ str(i) +";").fetchone()
    speed1 = str(speed[0])
    sp_attack = con.execute("Select sp_attack from pokemon where pokedex_number ="+ str(i) +";").fetchone()
    sp_attack1 = str(sp_attack[0])
    sp_defense = con.execute("Select sp_defense from pokemon where pokedex_number ="+ str(i) +";").fetchone()
    sp_defense1 = str(sp_defense[0])
    abilities = con.execute("Select name from ability join pokemon_abilities on ability.id=pokemon_abilities.ability_id where pokemon_abilities.pokemon_id ="+ str(i) +";").fetchall()
    abilities2 = []

    pokemon = {
        "name": name1,
        "pokedex_number": pokedex_number,
        "types": types,
        "hp": hp1,
        "attack": attack1,
        "defense": defense1,
        "speed": speed1,
        "sp_attack": sp_attack1,
        "sp_defense": sp_defense1,
        "abilities": abilities2
    }
    
    for j in range(len(abilities)):
        abilities2.append(str(abilities[j][0]))

    pokemonColl.insert_one(pokemon)