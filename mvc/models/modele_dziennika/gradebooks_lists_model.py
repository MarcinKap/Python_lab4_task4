from mvc.models.abstract_model import AbstractModel
from mvc.models.modele_dziennika.gradebook_model import Gradebook


class GradebooksList(AbstractModel):
    def __init__(self):
        super( ).__init__( )
        self.lista_dziennikow = []
        self.gradebooks_controllers = []
        self.gradebooks_view = []


    def modify(self, *args, **kwargs):
        self.notify()

    def notify(self):
        for obs in self._obs_list.values():
            obs.update(self.lista_dziennikow)

    # def dodanie_dziennika(self, Gradebook):
    #     self.lista_dziennikow.append(Gradebook)

    # def dodanie_dziennika_na_podstawie_starego(self, nazwa_nowego, stary_dziennik):
    #     self.lista_dziennikow.append(Gradebook(nazwa_nowego))
    #     self.wyszukaj_dziennik_po_nazwie(nazwa_nowego).lista_studentow = stary_dziennik.lista_studentow

    # def wypisz_liste_dziennikow(self):
    #     for x in self.lista_dziennikow:
    #         print(f'{x.nazwa}')
    #     print('\n')