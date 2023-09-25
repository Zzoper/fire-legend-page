import os
import msvcrt
import random

# Definimos los caracteres especiales para el usuario, obstáculos y entrenadores Pokémon
user_character = 'P'
obstacle_character = '#'
trainer_character = 'T'
empty_space_character = ' '

# Definimos el tamaño del mapa
map_width = 10
map_height = 10

# Creamos el mapa como una lista de listas (matriz)
mapa = [[empty_space_character] * map_width for _ in range(map_height)]

# Colocamos obstáculos en el mapa (por ejemplo, en coordenadas aleatorias)
obstacle_count = 10  # Cambia esto para agregar más obstáculos
for _ in range(obstacle_count):
    x, y = random.randint(0, map_width - 1), random.randint(0, map_height - 1)
    mapa[y][x] = obstacle_character

# Definimos entrenadores Pokémon y sus Pokémon
trainers = [
    {
        "name": "Entrenador 1",
        "x": random.randint(0, map_width - 1),
        "y": random.randint(0, map_height - 1),
        "pokemon": {
            "Squirtle": {
                "HP": 40,
                "Ataques": {
                    "Burbuja": 10,
                    "Pistola Agua": 8
                }
            }
        }
    },
    {
        "name": "Entrenador 2",
        "x": random.randint(0, map_width - 1),
        "y": random.randint(0, map_height - 1),
        "pokemon": {
            "Charmander": {
                "HP": 45,
                "Ataques": {
                    "Lanzallamas": 12,
                    "Garra Dragon": 9
                }
            }
        }
    },
    {
        "name": "Entrenador 3",
        "x": random.randint(0, map_width - 1),
        "y": random.randint(0, map_height - 1),
        "pokemon": {
            "Bulbasaur": {
                "HP": 38,
                "Ataques": {
                    "Látigo Cepa": 9,
                    "Gruñido": 7
                }
            }
        }
    }
]

# Colocamos a los entrenadores Pokémon en el mapa
for trainer in trainers:
    x, y = trainer["x"], trainer["y"]
    mapa[y][x] = trainer_character

# Colocamos al usuario en una posición inicial
user_x = 1
user_y = 1
mapa[user_y][user_x] = user_character

# Definimos Pokémon y sus ataques (solo dos ataques en este caso)
pokemon = {
    "Pikachu": {
        "HP": 50,
        "Ataques": {
            "Impactrueno": 10,
            "Onda Chispa": 8
        }
    },
    "Charizard": {
        "HP": 60,
        "Ataques": {
            "Lanzallamas": 15,
            "Garra Dragon": 12
        }
    },
    "Blastoise": {
        "HP": 65,
        "Ataques": {
            "Hidrobomba": 14,
            "Pistola Agua": 11
        }
    }
}

# Función para imprimir el mapa
def print_map():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
    for row in mapa:
        print(' '.join(row))

# Función para mover al usuario
def move_user(direction):
    global user_x, user_y
    new_x, new_y = user_x, user_y
    
    if direction == 'W':
        new_y -= 1
    elif direction == 'S':
        new_y += 1
    elif direction == 'A':
        new_x -= 1
    elif direction == 'D':
        new_x += 1
    
    # Verificamos si la nueva posición es válida y no es un obstáculo
    if 0 <= new_x < map_width and 0 <= new_y < map_height and mapa[new_y][new_x] != obstacle_character:
        if mapa[new_y][new_x] == trainer_character:
            initiate_battle(new_x, new_y)
        else:
            mapa[user_y][user_x] = empty_space_character
            user_x, user_y = new_x, new_y
            mapa[user_y][user_x] = user_character

# Función para iniciar una batalla Pokémon
def initiate_battle(x, y):
    trainer = None
    for t in trainers:
        if t["x"] == x and t["y"] == y:
            trainer = t
            break

    if trainer is None:
        return

    print(f"¡El entrenador {trainer['name']} te desafía a una batalla!")

    # Seleccionar un Pokémon del entrenador
    enemy_pokemon_name, enemy_pokemon_data = random.choice(list(trainer["pokemon"].items()))

    print(f"Enemigo Pokémon: {enemy_pokemon_name}")

    user_pokemon_name = random.choice(list(pokemon.keys()))
    user_pokemon_data = pokemon[user_pokemon_name]

    print(f"Tu Pokémon: {user_pokemon_name}")

    user_hp = user_pokemon_data["HP"]
    enemy_hp = enemy_pokemon_data["HP"]

    while user_hp > 0 and enemy_hp > 0:
        print(f"{user_pokemon_name} tiene {user_hp} puntos de vida.")
        print(f"{enemy_pokemon_name} tiene {enemy_hp} puntos de vida.")

        user_attack = input(f"Elige un ataque ({', '.join(user_pokemon_data['Ataques'].keys())}): ")
        if user_attack in user_pokemon_data["Ataques"]:
            user_damage = user_pokemon_data["Ataques"][user_attack]
        else:
            print("Ataque no válido. Elige un ataque válido.")
            continue

        enemy_attack_name, enemy_attack_damage = random.choice(list(enemy_pokemon_data["Ataques"].items()))
        print(f"{user_pokemon_name} usa {user_attack} y hace {user_damage} de daño.")
        print(f"{enemy_pokemon_name} usa {enemy_attack_name} y hace {enemy_attack_damage} de daño.")

        user_hp -= enemy_attack_damage
        enemy_hp -= user_damage

        if user_hp <= 0:
            print(f"Tu Pokémon {user_pokemon_name} ha sido derrotado. ¡Has perdido!")
            break
        elif enemy_hp <= 0:
            print(f"Has derrotado al Pokémon {enemy_pokemon_name} del entrenador {trainer['name']}. ¡Has ganado!")
            # Eliminamos al entrenador derrotado del mapa
            mapa[y][x] = empty_space_character
            trainer["x"] = -1
            trainer["y"] = -1
            break

# Bucle principal del juego
while True:
    print_map()
    
    # Espera hasta que se presione una tecla
    key = msvcrt.getch().decode('utf-8').upper()
    
    if key == 'W' or key == 'A' or key == 'S' or key == 'D':
        move_user(key)
    elif key == 'Q':
        break  # Salir del juego si se presiona 'Q'
