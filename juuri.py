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

def loput(kaikki: list, tyosana: str) -> list:
    riisuttava = kaikki.copy()
    for k in tyosana:
        riisuttava.remove(k)
    return riisuttava

koo, nee, vii, kuu, see, kasi, listan_nimi = alusta("sanat.txt")

tyosana, muut = syotto(koo)
kaikki = [k for k in tyosana + muut]

while len(tyosana) < 8:
    tyolista = listan_nimi[len(tyosana)+1]
    kirjaimet = set(tyosana)
    for k in kirjaimet:
        tyolista = [sana for sana in tyolista if sana.count(k) >= tyosana.count(k)]
    
    uudet_kirjaimittain = {k: [] for k in set(muut)}
    for sana in tyolista:
        for k in set(muut):
            if sana.count(k) >= tyosana.count(k) + 1:
                uudet_kirjaimittain[k].append(sana)

    for k in set(muut):
        if k in uudet_kirjaimittain and len(uudet_kirjaimittain[k]) == 0:
            uudet_kirjaimittain.pop(k)
    
    if len(uudet_kirjaimittain) == 1:
        print(f"\n\nVain yksi kelvollinen uusi kirjain sanoineen:")
        for k in uudet_kirjaimittain.keys():
            mahdolliset = uudet_kirjaimittain[k]
            print(f"{k}:\t{', '.join(mahdolliset)}")
        tyosana = mahdolliset[0]
        muut = loput(kaikki, tyosana)
    
    else:
        kaikki_mahdolliset = []
        print(f"\n\nMahdollisia uusia kirjaimia sanoineen ovat:")
        for k in uudet_kirjaimittain.keys():
            mahdolliset = uudet_kirjaimittain[k]
            print(f"{k}:\t{', '.join(mahdolliset)}")
            kaikki_mahdolliset += mahdolliset

        if len(tyosana) < 6:
            while True:
                uusi_tyosana = input("\nKerro mikä sana kelpasi Sanajuurelle:\n\t")
                if uusi_tyosana in kaikki_mahdolliset:
                    tyosana = uusi_tyosana
                    muut = loput(kaikki, tyosana)
                    break
                print("\nNyt tuli sana mahdollisten listan ulkopuolelta. Typo?\n")
        
        elif len(tyosana) == 6:
            tyosana = kaikki_mahdolliset[0]
            muut = loput(kaikki, tyosana)

        else:
            tyosana = "ratkaistu"
            print("\n\n")
