from mvc.controllers.abstract_controller import AbstractController
from mvc.models.abstract_model import AbstractModel
from mvc.models.modele_dziennika.gradebook_model import Gradebook


class GradebooksListController(AbstractController):
    def __init__(self, model=None, view=None):
        super().__init__(model, view)

    def get_user_input(self):
        obj = input('Type q to quit or s to show date:\n')
        if obj == 'q':
            return False
        elif obj == 's':
            self.model.modify()
        else:
            print('Incorrect value')
        return True

    def stworz_dziennik_na_bazie_starego(self, stary_dziennik, nazwa_nowego_dziennika):
        print('\nUtwórz nowy dziennik na podstawie starego...')
        lista_dziennikow.dodanie_dziennika_na_podstawie_starego(nazwa_nowego_dziennika, stary_dziennik)

    def wypisz_liste_dziennikow(self):
        print('\nWypisz listę dzienników...')
        lista_dziennikow.wypisz_liste_dziennikow( )

    def znajdz_dziennik(self, nazwa_dziennika):
        print('\nZnajdz dziennik po nazwie...')
        print('\nPodaj nazwe:', end=' ')
        return lista_dziennikow.wyszukaj_dziennik_po_nazwie(nazwa_dziennika)