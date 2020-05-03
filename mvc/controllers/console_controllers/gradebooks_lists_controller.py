from mvc.controllers.abstract_controller import AbstractController
from mvc.controllers.console_controllers.gradebook_controller import GradebookController
from mvc.models.abstract_model import AbstractModel
from mvc.models.modele_dziennika.gradebook_model import Gradebook
from mvc.views.widoki_dziennika.console_gradebook_view import ConsoleGradebookView


class GradebooksListController(AbstractController):
    def __init__(self, model=None, view=None):
        super( ).__init__(model, view)

    def get_user_input(self):
        obj = input('Type q to quit or s to show date:\n')
        if obj == 'q':
            return False
        elif obj == 's':
            self.model.modify( )
        else:
            print('Incorrect value')
        return True

    def stworz_dziennik_na_bazie_starego(self, stary_dziennik, nazwa_nowego_dziennika):

        stary_dziennik = self.get_gradebook_model(stary_dziennik)
        nowy_dziennik = Gradebook(nazwa_nowego_dziennika)
        nowy_dziennik.lista_studentow = stary_dziennik.lista_studentow

        nowy_widok = ConsoleGradebookView(nazwa_nowego_dziennika, nowy_dziennik)
        nowy_dziennik.add_observer(nowy_widok)
        nowy_kontroler = GradebookController(nowy_dziennik, nowy_widok, nazwa_nowego_dziennika)
        self.model.gradebooks_controllers.append(nowy_kontroler)
        self.model.lista_dziennikow.append(nowy_dziennik)
        self.model.gradebooks_view.append(nowy_widok)


        # self.model.lista_dziennikow.append(Gradebook(nazwa_nowego_dziennika))
        # self.model.wyszukaj_dziennik_po_nazwie(nazwa_nowego_dziennika).lista_studentow = stary_dziennik.lista_studentow
        # self.model.dodanie_dziennika_na_podstawie_starego(nazwa_nowego_dziennika, stary_dziennik)

    def stworz_dziennik_i_dodaj_do_listy(self, nazwa_nowego_dziennika):
        print("Wykonuje sie: stworz dziennik i dodaj do listy...")
        nowy_dziennik = Gradebook(nazwa_nowego_dziennika)
        nowy_widok = ConsoleGradebookView(nazwa_nowego_dziennika, nowy_dziennik)
        nowy_dziennik.add_observer(nowy_widok)
        nowy_kontroler = GradebookController(nowy_dziennik, nowy_widok, nazwa_nowego_dziennika)
        self.model.gradebooks_controllers.append(nowy_kontroler)
        self.model.lista_dziennikow.append(nowy_dziennik)
        self.model.gradebooks_view.append(nowy_widok)

        # self.model.dodanie_dziennika(nowy_dziennik)
        #
        # self.gradebook_list_controller = gradebook_list_controller
        # self.__gradeBooksList_model = GradebooksList( )
        # self.__gradeBooksList_view = ConsoleGradebookListView('ConsoleGradebookListView', self.__gradeBooksList_model)

    def wypisz_liste_dziennikow(self):
        for x in self.model.lista_dziennikow:
            print(f'{x.nazwa}')
        print('\n')

    def get_gradebook_model(self, nazwa_dziennika):
        print('\nWykonuje sie: znajdz dziennik po nazwie...')
        for x in self.model.lista_dziennikow:
            if x.nazwa == nazwa_dziennika:
                return x

    def get_gradebook_controller(self, nazwa_dziennika):
        print('\nWykonuje sie: znajdz dziennik po nazwie...')
        for x in self.model.gradebooks_controllers:
            print('asdsad')
            if x.name == nazwa_dziennika:
                return x

    def get_gradebook_view(self, nazwa_dziennika):
        print('\nWykonuje sie: znajdz dziennik po nazwie...')
        for x in self.model.gradebooks_view:
            if x.name == nazwa_dziennika:
                return x
