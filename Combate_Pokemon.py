import os
import random

TAMAÑO_BARRA_VIDA = 20

titulo = "Antes de empezar con el combate tienes que elegir un pokemon"
print("\n" + "-" * len(titulo) + "\n" + titulo + "\n" + "-" * len(titulo))

input("Presiona el ENTER...")
os.system("cls")

titulo = "Squirtle\n" \
         "vida = 70\n" \
         "ataques: Placaje - 10\n" \
         "         Burbuja - 15"
print("\n" + "-" * 22 + "\n" + titulo + "\n" + "-" * 22)

input("Presiona el ENTER...")

titulo = "Charmander\n" \
         "vida = 60\n" \
         "ataques: Placaje - 10\n" \
         "         Ascuas - 17"
print("\n" + "-" * 22 + "\n" + titulo + "\n" + "-" * 22)

input("Presiona el ENTER...")

titulo = "Vulvasaur\n" \
         "vida = 80\n" \
         "ataques: Placaje - 10\n" \
         "         Latigo cepa - 13"
print("\n" + "-" * 26 + "\n" + titulo + "\n" + "-" * 26)

tu_pokemon = "Ninguno"
vida_tu_pokemon = 0
ataque_especial = "Ninguno"

pokemon = None
while pokemon != "S" and pokemon != "C" and pokemon != "V":
    pokemon = input("\n¿Que pokemon elges?(S/C/V): ")
if pokemon == "S":
    VIDA_INICIAL_TU_POKEMON = 70
    vida_tu_pokemon = VIDA_INICIAL_TU_POKEMON
    tu_pokemon = "Squirtle"
    ataque_especial = "[B]urbuja (quita 15 de vida)"
elif pokemon == "C":
    VIDA_INICIAL_TU_POKEMON = 60
    vida_tu_pokemon = VIDA_INICIAL_TU_POKEMON
    tu_pokemon = "Charmander"
    ataque_especial = "[A]scuas (quita 17 de vida)"
elif pokemon == "V":
    VIDA_INICIAL_TU_POKEMON = 80
    vida_tu_pokemon = VIDA_INICIAL_TU_POKEMON
    tu_pokemon = "Vulvasaur"
    ataque_especial = "[L]atigo cepa (quita 13 de vida)"

os.system("cls")

print("\n¡Enhorabuena, el pokemon que has elegido es " + tu_pokemon + "!")

rival = random.randint(1, 6)
nombre_rival = "Ninguno"

if rival == 1:
    nombre_rival = "Carmen"
elif rival == 2:
    nombre_rival = "Eva"
elif rival == 3:
    nombre_rival = "Marta"
elif rival == 4:
    nombre_rival = "Pedro"
elif rival == 5:
    nombre_rival = "Jose"
elif rival == 6:
    nombre_rival = "Carlos"

pokemon = random.randint(1, 3)
pokemon_rival = "Ninguno"
VIDA_INICIAL_POKEMON_RIVAL = 0
if pokemon == 1:
    VIDA_INICIAL_POKEMON_RIVAL = 70
    vida_pokemon_rival = VIDA_INICIAL_POKEMON_RIVAL
    pokemon_rival = "Squirtle"
elif pokemon == 2:
    VIDA_INICIAL_POKEMON_RIVAL = 60
    vida_pokemon_rival = VIDA_INICIAL_POKEMON_RIVAL
    pokemon_rival = "Charmander"
elif pokemon == 3:
    VIDA_INICIAL_POKEMON_RIVAL = 80
    vida_pokemon_rival = VIDA_INICIAL_POKEMON_RIVAL
    pokemon_rival = "Vulvasaur"

print("\nY vas a luchar contra " + nombre_rival + " que tiene un " + pokemon_rival)

input("\nPresiona el ENTER...\n")
os.system("cls")

while vida_tu_pokemon > 0 and vida_pokemon_rival > 0:

    print("Tus ataques son: [P]lacaje (quita 10 de vida)\n"
          "                 " + ataque_especial)
    tu_ataque = None
    while tu_ataque != "P" and tu_ataque != "B" and tu_ataque != "A" and tu_ataque != "L":
        tu_ataque = input("\n¿Que ataque usaras? ")

    if tu_ataque == "P":
        vida_pokemon_rival -= 10
    elif tu_ataque == "B":
        vida_pokemon_rival -= 15
    elif tu_ataque == "A":
        vida_pokemon_rival -= 17
    elif tu_ataque == "L":
        vida_pokemon_rival -= 13

    ataque_rival = random.randint(1, 2)
    if pokemon_rival == "Squirtle":
        if ataque_rival == 1:
            print("\nel " + pokemon_rival + "de " + nombre_rival + " usa placaje")
            vida_tu_pokemon -= 10
        else:
            print("\nel " + pokemon_rival + "de " + nombre_rival + " usa burbuja")
            vida_tu_pokemon -= 15
    elif pokemon_rival == "Charmander":
        if ataque_rival == 1:
            print("\nel " + pokemon_rival + "de " + nombre_rival + " usa placaje")
            vida_tu_pokemon -= 10
        else:
            print("\nel " + pokemon_rival + "de " + nombre_rival + " usa ascuas")
            vida_tu_pokemon -= 17
    elif pokemon_rival == "Vulvasaur":
        if ataque_rival == 1:
            print("\nel " + pokemon_rival + "de " + nombre_rival + " usa placaje")
            vida_tu_pokemon -= 10
        else:
            print("\nel " + pokemon_rival + "de " + nombre_rival + " usa latigo cepa")
            vida_tu_pokemon -= 13

    barras_de_vida_tu_pokemon = int(vida_tu_pokemon * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_TU_POKEMON)
    print("\n{}:    [{}{}] ({}/{})".format(tu_pokemon, "*" * barras_de_vida_tu_pokemon,
                                           " " * (TAMAÑO_BARRA_VIDA - barras_de_vida_tu_pokemon), vida_tu_pokemon,
                                           VIDA_INICIAL_TU_POKEMON))

    barras_de_vida_pokemon_rival = int(vida_pokemon_rival * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_POKEMON_RIVAL)
    print("{}:    [{}{}] ({}/{})".format(pokemon_rival, "*" * barras_de_vida_pokemon_rival,
                                         " " * (TAMAÑO_BARRA_VIDA - barras_de_vida_pokemon_rival), vida_pokemon_rival,
                                         VIDA_INICIAL_POKEMON_RIVAL))

    input("\nPulsa el ENTER...\n")
    os.system("cls")

if vida_tu_pokemon > vida_pokemon_rival:
    print("Enhorabuena, has ganado el combate!!!")

else:
    print("Vaya, parece que has perdido.")
