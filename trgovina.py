# Aplikacija za spletno trgovino

import modeli # delo z bazo


class StanjeAplikacije:
    """ Se obnaša podobno kot enum v drugih jezikih - z pomočjo tega razreda nastavimo 
    stanje na eno izmed možnih vrednosti, brez da bi si morali zapomniti, katere nize
    smo uporabili za katero stanje. Po potrebi lahko stanja dodajama. """

    Domov = 1 # gumb Home - to bo privzeta vrednost
    Opis = 2 # gumb About me
    Trgovina = 3 # gumb Store
    Kosarica = 4 # gumb Basket - do tega lahko dostopamo samo v trgovini
    Racun = 5 # ko zaključimo nakup, se nam prikaže nova stran, na kateri je račun nakupa


class Trgovina:
    def __init__(self):
        self.stanjeAp = StanjeAplikacije.Domov

        self.uporabnik = None
        self.nakup = None
        self.kosarica = None

        self.nalozi()

    def nalozi(self):
        """ Nalozi ustrezno stran. """
        if self.stanjeAp == StanjeAplikacije.Domov:
            self.prikaziMenuDomov()
        elif self.stanjeAp == StanjeAplikacije.Opis:
            self.prikaziMenuOpis()
        elif self.stanjeAp == StanjeAplikacije.Trgovina:
            self.prikaziMenuTrgovina()
        elif self.stanjeAp == StanjeAplikacije.Kosarica:
            self.prikaziKosarico()
        elif self.stanjeAp == StanjeAplikacije.Racun:
            self.prikaziRacun()

    # Metode za prikazovanje ustreznih strani:

    def prikaziMenuDomov(self):
        """ Morema napisati html """
        pass

    def prikaziMenuOpis(self):
        """ Morema napisati html """
        pass

    def prikaziMenuTrgovina(self):
        """ Morema napisati html """
        pass

    def prikaziKosarico(self):
        """ Uporabnika napoti na novo stran, na kateri mu prikaže košarico v obliki seznama, tako da
         vidi, katere slike ima zaenkrat v njej, koliko posamezna slika stane in kakšna je vrednost
         celotnega nakupa. V kolikor se odloči za nakup, ima tukaj možnost zaključiti nakup, sicer 
         lahko nadaljuje z nakupom ali odstrani posamezne izdelke iz košarice. """
        pass

    def prikaziRacun(self):
        pass

    # Pomožne metode:

    def dodajVKosarico(self, slika):
        """ Dodamo izbrano sliko v uporabnikovo košarico. Shranimo datum vstavljanja. """
        pass

    def odstraniIzKosarice(self, slika):
        """ Odstranimo izbrano sliko iz uporabnikove košarice. Shranimo datum odstranitve. """
        pass

    def pretvoriKosaricoVNakup(self):
        """ Nastavimo datum nakupa in vrednost. Slikam nakupa nastavimo dosegljivost na false. """
        pass



Trgovina()

# Igranje z bazo:

#modeli.dodajUporabnika("Larisa", "Carli", "lara.carli@gmail.com", "1234")
#modeli.dodajUporabnika("Anja", "Trop", "anya.trop@gmail.com", "4321")
#print(modeli.uporabniki())
#modeli.dodajSliko("Morje", "oljna slika", 150)
#modeli.dodajSliko("Haloze", "pastelna slika", 120) # naslov bi lahko nastavili unique

modeli.prijavaUporabnika("lara.carli@gmail.com", "1234")
modeli.prijavaUporabnika("lara.carli@gmail.com", "1232")
modeli.prijavaUporabnika("la.carli@gmail.com", "1234")
