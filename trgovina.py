# Aplikacija za spletno trgovino

class StanjeAplikacije:
    """ Se obnaša podobno kot enum v drugih jezikih - z pomočjo tega razreda nastavimo 
    stanje na eno izmed možnih vrednosti, brez da bi si morali zapomniti, katere nize
    smo uporabili za katero stanje. Po potrebi lahko stanja dodajama. """

    Domov = 1 # gumb Home - to bo privzeta vrednost
    Opis = 2 # gumb About me
    Trgovina = 3 # gumb Store
    Kosarica = 4 # gumb Basket - do tega lahko dostopamo samo v trgovini
    Racun = 5 # ko zaključimo nakup, se nam prikaže nova stran, na kateri je račun nakupa


class Uporabnik:
    def __init__(self, id_, ime, priimek, email, geslo):
        self.id_ = id_ # id je vgrajeno ime in ne gre..
        self.ime = ime
        self.priimek = priimek
        self.email = email
        self.geslo = geslo

    def __repr__(self):
        return self.ime + " " + self.priimek

    def preveri_ujemanje_prijave(self, email):
        """ Vrne logično vrednost, ki pove, če vstavljeno geslo in email ustrezata tej osebi. """
        return self.email == email


class Slika:
    def __init__(self, id_, dosegljivost, naslov, vrsta, cena):
        self.id_ = id_
        self.dosegljivost = True
        self.naslov = naslov
        self.vrsta = vrsta
        self.cena = cena


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
        pass

    def prikaziMenuOpis(self):
        pass

    def prikaziMenuTrgovina(self):
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
