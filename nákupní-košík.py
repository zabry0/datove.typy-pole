zbozi = ["CPU", "RAM", "HDD", "SSD", "MOTHERBOARD", "CHLAZENI"]
kosik = []

def vyber_polozky(seznam):
    print("Vyberte položku ze seznamu:")
    for i, polozka in enumerate(seznam):
        print(f"{i + 1}. {polozka}")
    volba = input("Zadejte číslo položky nebo 'k' pro konec: ")
    return volba

while True:
    volba = vyber_polozky(zbozi)
    if volba.lower() == 'k':
        print zbozi