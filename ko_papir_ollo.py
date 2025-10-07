"""
Kő-Papír-Olló játék
V0.02
Mezei Dávid, Óvári Tamás
2025. 10. 07
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

# Inicializáljuk a változókat

nyertes = 0
vesztes = 0
dontetlen = 0

game = True

# Köszöntjük a játékost
print("Üdv a játékban!")
print("Fontos: A kilépéshez nyomd le a CTRL+C billentyűkombinációt!")
print("Jó játékot!\n")

choices = ["kő", "papír", "olló"]

while game:
    try:
        # A felhasználó beadott adatait kezeljük

        user_choice = input("Kérem a választásodat! (kő/papír/olló) ")

        while user_choice.lower() not in ["kő" , "papír", "olló"]:
            print("Kérlek megfelelő választ adj meg!")
            user_choice = input("Kérem a választásodat! (kő/papír/olló) ")


        pc_choice = r.choice(choices)

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
        
        print(f"A gép ezt választotta: {pc_choice}")

    # A Ctrl+C billentyűkombinációra kilépünk a programból és kiírjuk a végeredményeket

    except KeyboardInterrupt:
        print(f"""\n
    Statisztikák: 
        - Nyertes játékok száma: {nyertes} 
        - Vesztes játékok száma: {vesztes}
        - Döntetlen játékok száma: {dontetlen}""")
        print("\nKöszönjük, hogy játszottál!")
        game = False