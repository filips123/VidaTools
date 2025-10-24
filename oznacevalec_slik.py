import os
import random
import shutil
import sys

from PIL import Image


if "--nisem-vida" in sys.argv:
    mapa_slik = input("vnesi pot do mape z nesortiranimi slikami: ")
    mapa_map = input("vnesi pot do mape z označenimi slikami: ")
else:
    # absolutna pot
    # mapa_slik = os.path.join("C:", "Users", "vidam", "Desktop", "Alia", "google_slike")
    mapa_slik = r"C:\Users\vidam\Downloads\Photos-1-001(3)"
    # mapa_slik = r"C:\Users\vidam\Desktop\Alia\slike\videi"
    mapa_map = r"C:\Users\vidam\Desktop\Alia\slike"
    # os.path.join("C:", "Users", "vidam", "Desktop", "Alia", "slike")


nesramen_nacin = True if "--nesramen" in sys.argv else False
prijazen_nacin = True if "--prijazen" in sys.argv else False


nesramni_stavki = [
    "Kako slaba slika!",
    "Slabše slike še nisem videl!",
    "Še opica bi naredila boljšo sliko!",
    "In ti misliš, da si fotograf?",
    "Ne opletaj s telefonom!",
    "Kaj je ta zmazek?",
    "Ali vidim prst?",
    "Abstraktna umetnost brez umetnosti :/",
    "Kamera: 1, estetika: 0",
    "Ubogi telefon!",
    "Še dobro da obstaja fotošop!",
    "Tudi fotošop tu ne bo pomagal!",
    "Vaja ne dela mojstra!",
]

prijazni_stavki = [
    "Mojstrovina!",
    "Kako lepa slika!",
    "Slikaš kot profesionalec!",
    "Trenutek za zgodovino!",
    "Barve življenja!",
    "Kreativnost v akciji!",
    "Fotografija z osebnostjo!",
    "Ujeti trenutek popolnosti!",
    "Kar tako naprej!",
    "Čudovita kompozicija!"
]


tags = next(os.walk(mapa_map))[1]
print(tags)


def dodaj(slika, tag):
    slika_pot = os.path.join(mapa_slik, slika)
    nova_pot = os.path.join(mapa_map, tag, slika)
    shutil.move(slika_pot, nova_pot)

def play_movie(path):
    from os import startfile
    startfile(path)


for slika in os.listdir(mapa_slik):
    slika_pot = os.path.join(mapa_slik, slika)
    if slika.endswith(".jpg"):
        img = Image.open(slika_pot)
        img.show()
    # elif slika.endswith(".mp4"):
    #     play_movie(slika_pot)
    else:
        continue
    if nesramen_nacin:
        print(random.choice(nesramni_stavki))
    if prijazen_nacin:
        print(random.choice(prijazni_stavki))
    while True:
        print(tags)
        print(slika)
        w = input("input (ntag, tagname): ")
        if w == "ntag":
            ntag = input("nov tag: ")
            tags.append(ntag)
            ntag_dir = os.path.join(mapa_map, ntag)
            if not os.path.exists(ntag_dir):
                os.makedirs(ntag_dir)
                dodaj(slika, ntag)
            # nova_pot = os.path.join(ntag_dir, slika)
            # shutil.move(slika_pot, nova_pot)
        elif w in tags:
            dodaj(slika, w)
            break
            # nova_pot = os.path.join(mapa_map, w, slika)
            # shutil.move(slika_pot, nova_pot)
        else:
            moznosti = []
            for c in tags:
                if w.lower() in c.lower():
                    moznosti.append(c)
            if len(moznosti) == 1:
                dodaj(slika, moznosti[0])
                break
            else:
                print("ni v tagih!, možnosti:", moznosti)
                continue
        break
