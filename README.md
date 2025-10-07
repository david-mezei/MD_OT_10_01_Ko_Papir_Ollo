
# Kő-Papír-Olló játék
~~~
.-------------------------------------------------------.
| _  __ ___   ____             __        ___  _ _   __  |
|| |/ //_/_/ |  _ \ __ _ _ __ /_/_ __   / _ \| | | /_/  |
|| ' // _ \  | |_) / _` | '_ \| | '__| | | | | | |/ _ \ |
|| . \ |_| | |  __/ (_| | |_) | | |    | |_| | | | (_) ||
||_|\_\___/  |_|   \__,_| .__/|_|_|     \___/|_|_|\___/ |
|                       |_|                             |
'-------------------------------------------------------'
~~~
Egy egyszerű kő-papír-olló játék, Pythonbn írva.

## Funkciók
- A program köszönti a felhasználót
- Megkérdezi a választását
- Kielemzi az eredményeket, majd kiírja
- A játék addig fut, amíg a felhasználó a **Ctrl+C** billentyűkombinációt le nem nyomja
## Kódrészletek
A játék alap logikája: 
```python
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
```

Kilépés kezelése:
```python
while game:
    try:
        ...
except KeyboardInterrupt:
        ...
        print("Köszönjük, hogy játszottál!")
        game = False

```

## Készítők

- [Mezei Dávid](https://www.github.com/david-mezei)
- [Óvári Tamás](https://github.com/ovaritamas)

## Észrevételek

A programmal kapcsolatos észrevételeket várjuk emailben:
- mezei.david.sandor@diak.szbi-pg.hu
- ovari.tamas@diak.szbi-pg.hu 