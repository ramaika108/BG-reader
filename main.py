import json

def read_from_file():
    BG = None
    with open('sorted_bg.json', 'r') as bg_file:
        BG = json.load(bg_file)
    return BG

BG = read_from_file()

print(BG['Chapter 1: Observing the Armies on the Battlefield of Kurukṣetra'][0]['devanagari_sanscrit'])
input()
