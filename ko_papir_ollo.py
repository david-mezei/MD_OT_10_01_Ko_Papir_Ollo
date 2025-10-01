"""
Kő-Papír-Olló játék
V0.01
Mezei Dávid, Óvári Tamás
2025. 10. 01
"""

import random as r

print("""
.-------------------------------------------------------.
| _  __ ___   ____             __        ___  _ _   __  |
|| |/ //_/_/ |  _ \ __ _ _ __ /_/_ __   / _ \| | | /_/  |
|| ' // _ \  | |_) / _` | '_ \| | '__| | | | | | |/ _ \ |
|| . \ |_| | |  __/ (_| | |_) | | |    | |_| | | | (_) ||
||_|\_\___/  |_|   \__,_| .__/|_|_|     \___/|_|_|\___/ |
|                       |_|                             |
'-------------------------------------------------------'
""")

nyertes = 0
vesztes = 0
dontetlen = 0

game = True

print("Üdv a játékban!")

choices = ["kő", "papír", "olló"]

while game:

    user_choice = input("Kérem a választásodat! (kő/papír/olló) ")

    while user_choice.lower() not in ["kő" , "papír", "olló"]:
        print("Kérlek megfelelő választ adj meg!")
        user_choice = input("Kérem a választásodat! (kő/papír/olló) ")


    pc_choice = r.choice(choices)
    print(pc_choice)

    # Kő beats olló
    # Olló beats pépörke
    # Pépörke beats kő
    # Nothing beats a jet2 holiday

    ## Kő ##
    if user_choice == choices[0] and pc_choice == choices[0]:
        print("Döntetlen")
        dontetlen += 1
    elif user_choice == choices[0] and pc_choice == choices[2]:
        print("Nyertél")
        nyertes += 1
    elif user_choice == choices[0] and pc_choice == choices[1]:
        print("Vesztettél")
        vesztes += 1


    ## Papír ##
    if user_choice == choices[1] and pc_choice == choices[1]:
        print("Döntetlen")
        dontetlen += 1
    elif user_choice == choices[1] and pc_choice == choices[0]:
        print("Nyertél")
        nyertes += 1
    elif user_choice == choices[1] and pc_choice == choices[2]:
        print("Vesztettél")
        vesztes += 1

    ## Olló ##
    if user_choice == choices[2] and pc_choice == choices[2]:
        print("Döntetlen")
        dontetlen += 1
    elif user_choice == choices[2] and pc_choice == choices[0]:
        print("Vesztettél")
        vesztes += 1
    elif user_choice == choices[2] and pc_choice == choices[1]:
        print("Nyertél")
        nyertes += 1

    input("Szeretnél még játszani? (i/n)")
    if input == "n":
        game = False