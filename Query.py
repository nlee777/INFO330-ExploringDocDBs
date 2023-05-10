from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['anotherOne_10']

pikachu = pokemonColl.find_one({"name": "Pikachu"})
attack = pokemonColl.find({"attack": {"$gt": 150}})
attack2 = []

for attack_value in attack:
    attack2.append(attack_value)
ability = pokemonColl.find({"abilities": {"$in": ["Overgrow"]}})
ability2 = []

for ability_value in ability:
    ability2.append(ability_value)

print(len(attack2))