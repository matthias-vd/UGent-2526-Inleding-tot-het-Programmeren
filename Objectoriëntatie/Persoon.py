import datetime


class Persoon:
    def __init__(self, naam, voornaam, woonplaats, jaar_geboorte_datum, maand_geboorte_datum, dag_geboorte_datum):
        self.naam, self.voornaam, self.woonplaats = naam, voornaam, woonplaats
        self.geboortedatum = datetime.date(jaar_geboorte_datum, maand_geboorte_datum, dag_geboorte_datum)

    def get_naam(self):
        return self.naam

    def get_voornaam(self):
        return self.voornaam

    def get_woonplaats(self):
        return self.woonplaats

    def get_geboorte_datum(self):
        return self.geboortedatum

    def set_voornaam(self, new_voornaam):
        self.voornaam = new_voornaam

    def set_woonplaats(self, new_woonplaats):
        self.woonplaats = new_woonplaats

    def is_ouder_dan(self, other_persoon):
        return int(str(self.geboortedatum - other_persoon.geboortedatum).split(' ')[0]) < 0

    def is_jonger_dan(self, other_persoon):
        return int(str(self.geboortedatum - other_persoon.geboortedatum).split(' ')[0]) > 0

    def wonen_in_zelfde_stad(self, other_persoon):
        return self.woonplaats == other_persoon.woonplaats

