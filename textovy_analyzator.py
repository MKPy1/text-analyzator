"""
Textový analyzátor
"""

#statické proměnné
global samohlasky, souhlasky
samohlasky = ("a","e","i","o","u","y", "á", "é","í","ó","ú","ý")
souhlasky = ("h","k","r","d","t","n","b","f","l","m","p","s","v","z", "ž","š","č","ř","c","j","ď","ť","ň", "g")

def uvod():
    text = "Vitejte v textovém analyzátoru".upper()
    stred=text.center(40)
    print(stred)
    print("="*40)
uvod()

def oddelovac():
    print("="*40)

def moznosti():
    volba = """
    1) Výskyt daného písmeno dle zadaného slovo/větě
    2) Počet samohlásek a souhlásek v zadaném slově/větě
    3) Kolikrát je daná hodnota v listu
    4) Seřazení listu podle abecedy
    """
    print(volba)
moznosti()

oddelovac()

vstup = input("""Zadej, jakou akci chceš, provést (1-4).
Pro ukončení ('K'): """)
oddelovac()


while True:
    if vstup=="K":
        print("Program se ukončí...")
        break
    else:
        if vstup=="1": #najdi určitý výraz dle zadání
            kolikrat = int(input("Kolikrát chcete akci opakovat: "))
            for i in range(0,kolikrat):
                veta = input("Zadej slovo/větu, ve které budeme hledat: ")
                nachazi = input("Co mám hledat: ")
                for slovo in veta:
                    if slovo in nachazi:
                        print("Zadaný výraz se v daném výrazu NACHÁZÍ")
                        oddelovac()
                        break
                else:
                    print("Zadaný výraz se v daném výrazu NENACHÁZÍ")
                    oddelovac()
                    break
            break
        elif vstup=="2": #samohlásky a souhlásky
            kolikrat = input("Kolikrát chcete akci opakovat: ")

            while True:
                if not kolikrat.isdigit():
                    print("Je nutné zadat číslo. Opakujte akci.")
                    oddelovac()
                    break
                else:

                    kolikrat=int(kolikrat)
                    for i in range(0, kolikrat):
                        vstup = input("Zadej slovou/věku, ve které budeme počítat: ")
                        vstup=vstup.lower()
                        pocet_samohlasky=0
                        pocet_souhlasky=0

                        for znak in vstup:
                            if znak in samohlasky:
                                pocet_samohlasky += 1
                            elif znak in souhlasky:
                                pocet_souhlasky += 1
                        print("Počet samohlásek: ", str(pocet_samohlasky))
                        print("Počet souhlásek: ", str(pocet_souhlasky))
                        oddelovac()
                    print(input("ENTER pro ukončení"))
                    exit()
                    break
        elif vstup=="3": #zjištění počtu daných znaků, uložení do slovníku
            zadej = input("Zadej za sebou znaky pro výpočet výskytu: ")
            while True:
                    if zadej=="K":
                        print("Program se ukončí...")
                        exit()
                    else:
                        slovnik = dict()
                        for i in zadej:
                            slovnik[str(i)] = slovnik.setdefault(str(i),0)+1
                        print(slovnik)
                        break
            break
        elif vstup=="4": #vygenerování počtu zadaných jmén
            zadej_jmena = int(input("Zadej počet jmén pro vygenerování: "))
            novy_slovnik = dict()
            databaze = {}
            databaze_serad = []
            for i in range(0, zadej_jmena):
                zadej_nazvy_jmen = input("Zadej jednotlivá jména: ").title()
                jmeno_klic = zadej_nazvy_jmen
                novy_slovnik[jmeno_klic] = {"jméno": zadej_nazvy_jmen}
                databaze.update(novy_slovnik)
                oddelovac()
            print("Databáze teď obsahuje následující údaje: ",databaze)
            oddelovac()
            print(input("Pokračujte stisknutím klávesy ENTER..."))

            print("Seřazené jména dle abecedy A-Z jsou:")
            for znak in databaze: #seřazení dle abecedy (vzestupně)
                for i, s_znak in enumerate(databaze_serad):
                    if znak < s_znak:
                        databaze_serad.insert(i,znak)
                        break
                else:
                    databaze_serad.append(znak)
            print(databaze_serad)
            oddelovac()
            break










