class Pojazd: # tworzenie klasy ze wszystkimi obiektami dla wszystkich klasow
    def __init__(self, TypPojazdu, Marka, Kolor, Rok):
        self.TypPojazdu = TypPojazdu
        self.Marka = Marka
        self.Kolor = Kolor
        self.Rok = Rok
    def show(self): # tworzenie funkcji wyswietlenia danych
        pass

    
class Auto(Pojazd):# tworzenie klasy "Auto" z wartosciami klasy "Pojazd" i unikalnymi wartosciami dla obiektow klasy "Auto"
    def __init__(self, TypPojazdu, Marka, Kolor, Rok, KM, PojemnoscSkokowa):
        super().__init__(TypPojazdu, Marka, Kolor, Rok)
        self.KM = KM
        self.PojemnoscSkokowa = PojemnoscSkokowa
    def show(self): # tworzenie funkcji wyswietlenia danych
        print(f"Typ pojazdu: {self.TypPojazdu}")
        print(f"Marka pojazdu: {self.Marka}")
        print(f"Kolor pojazdu: {self.Kolor}")
        print(f"Rok produkcji: {self.Rok}")
        print(f"Moc: {self.KM} KM")
        print(f"Pojemnosc skokowa: {self.PojemnoscSkokowa}\n")

class Dwukolowiec(Pojazd):
    def __init__(self, TypPojazdu, Marka, Kolor, Rok, MaSilnik):
        super().__init__(TypPojazdu, Marka, Kolor, Rok)
        self.MaSilnik = MaSilnik
    def show(self):
        print(f"Typ pojazdu: {self.TypPojazdu}")
        print(f"Marka pojazdu: {self.Marka}")
        print(f"Kolor pojazdu: {self.Kolor}")
        print(f"Rok produkcji: {self.Rok}")
        print(f"Pojazd {self.MaSilnik} silnik\n")

class Przyczepa(Pojazd):
    def __init__(self, TypPojazdu, Marka, Kolor, Rok, Masa, MiejscDoSpania):
        super().__init__(TypPojazdu, Marka, Kolor, Rok)
        self.Masa = Masa
        self.MiejscDoSpania = MiejscDoSpania
    def show(self):
        print(f"Typ pojazdu: {self.TypPojazdu}")
        print(f"Marka pojazdu: {self.Marka}")
        print(f"Kolor pojazdu: {self.Kolor}")
        print(f"Rok produkcji: {self.Rok}")
        print(f"Masa: {self.Masa}")
        print(f"Miejsc do spania: {self.MiejscDoSpania}\n")

Porsche = Auto("Samochod", "Porsche 911 Cabrio 992", "Niebieski", "2019", "385", "3.0") #dane elementu
Porsche.show() #wyswietlenie elementu
Wigry3 = Dwukolowiec("Rower", "Wigry 3", "Pomaranczowy", "1990", "nie ma")
Wigry3.show()
Golf = Auto("Samochod", "Volkswagen Golf V", "Szary", "2004", "75", "1.9")
Golf.show()
Polonez = Auto("Samochod", "FSO Polonez", "Bialy", "1997", "78", "1.6")
Polonez.show()
LadaSamara = Auto("Samochod", "Lada Samara", "Czerwony", "1995", "64", "1.3")
LadaSamara.show()
Junak = Dwukolowiec("Motocykl", "Junak SR400", "Brazowy", "2022", "ma")
Junak.show()
PrzyczepaKempingowa = Przyczepa("Przyczepa Kempingowa", "Hobby 470 KMF ONTOUR 2022R", "Bialy", "2022", "1009 kg", "5")
PrzyczepaKempingowa.show()
F1 = Auto("Samochod", "Formula Jeden", "Szary", "2019", "950", "1.6")
F1.show()
Mazda3 = Auto("Samochod", "Mazda 3", "Czarny", "2012", "105", "1.6")
Mazda3.show()
HulajnogaElektryczna = Dwukolowiec("Hulajnoga Elektryczna", "Xiaomi Mi Electric Scooter Essential", "Czarny", "2021", "ma eletryczny")
HulajnogaElektryczna.show()
