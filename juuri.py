import re

def alusta(sanalista: str) -> tuple:
    koo, nee, vii, kuu, see, kasi = [], [], [], [], [], []
    listan_nimi = {3: koo, 4: nee, 5: vii, 6: kuu, 7: see, 8:kasi}
    with open(sanalista, encoding="utf-8") as f:
        for r in f:
            s = r.split("\t")[0]
            if len(s) in listan_nimi:
                listan_nimi[len(s)].append(s)
    
    return (koo, nee, vii, kuu, see, kasi, listan_nimi)

def syotto(kolmoset: dict) -> tuple:
    while True:
        eka = input("Mikä on annettu sana?:\n\t")
        if len(eka) != 3:
            print("\nNyt tuli vääränpituinen sana :|\n")
            continue
        if eka not in kolmoset:
            print("\n Tätä sanaa ei löydy sanastosta. Typo vai Hesarin moka?\n")
            continue
        break
    while True:
        muut = input("Mitkä ovat muut kirjaimet?:\n\t")
        if len(muut) != 5:
            print("\nViittä kirjainta yhdessä möykyssä haetaan :|\n")
            continue
        break
    return (eka, muut)


koo, nee, vii, kuu, see, kasi, listan_nimi = alusta("sanat.txt")

tyosana, muut = syotto(koo)

while len(tyosana) < 8:
    tyolista = listan_nimi[len(tyosana)+1]
    kirjaimet = set(tyosana)
    useampia = {}
    for k in kirjaimet:
        if tyosana.count(k) > 1:
            useampia[k] = tyosana.count(k)
    for k in kirjaimet:
        tyolista = [sana for sana in tyolista if k in sana]
    if len(useampia) > 0:
        for k in useampia:
            tyolista = [sana for sana in tyolista if sana.count(k) >= useampia[k]]
    
    mahdolliset = []
    for sana in tyolista:
        for k in muut:
            if sana.count(k) >= tyosana.count(k) + 1:
                mahdolliset.append(sana)

    if len(mahdolliset) == 1:
        print(f"\nVain yksi mahdollinen sana:\n\t{mahdolliset[0]}")
        tyosana = mahdolliset[0]
    else:
        print(f"\nMahdollisia sanoja ovat:")
        for sana in mahdolliset:
            print(f"\t{sana}")
        if len(tyosana) < 7:
            while True:
                uusi_tyosana = input("\nKerro mikä sana kelpasi Sanajuurelle:\n\t")
                if uusi_tyosana in mahdolliset:
                    tyosana = uusi_tyosana
                    break
                print("\nNyt tuli sana mahdollisten listan ulkopuolelta. Typo?\n")
        else:
            tyosana = "ratkaistu"
