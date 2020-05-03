import sys
from abc import ABC, abstractmethod
# from models.date_time_model import DateTimeModel
# from views.console_view import ConsoleDateView
from mvc.controllers.console_controllers.gradebook_controller import GradebookController
from mvc.models.date_time_model import DateTimeModel
from mvc.models.modele_dziennika.gradebooks_lists_model import GradebooksList
from mvc.views.console_view import ConsoleDateView
from mvc.views.widoki_dziennika.console_gradebook_list_view import ConsoleGradebookListView


class AbstractApp(ABC):
    def __init__(self, controller):
        super().__init__()
        self.__controller = controller

    @abstractmethod
    def run_app(self):
        pass

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, new_controller):
        self.__controller = new_controller


class ConsoleApp(AbstractApp):
    def __init__(self, controller, gradebook_list_controller):
        super().__init__(controller)

        # MODEL I VIEW DATETIME
        self.__model = DateTimeModel()
        self.__view = ConsoleDateView('ConsoleDateView', self.__model)
        self.__model.add_observer(self.__view)
        controller.model = self.__model
        controller.view = self.__view

        #  GRADEBOOKLIST
        self.gradebook_list_controller = gradebook_list_controller
        self.__gradeBooksList_model = GradebooksList()
        self.__gradeBooksList_view = ConsoleGradebookListView('ConsoleGradebookListView', self.__gradeBooksList_model)
        gradebook_list_controller.model = self.__gradeBooksList_model
        gradebook_list_controller.view = self.__gradeBooksList_view

    def run_app(self):
        # self.gradebook_list_controller.stworz_dziennik_i_dodaj_do_listy('nowy_dziennik')
        # self.gradebook_list_controller.stworz_dziennik_i_dodaj_do_listy('nowy_dziennik123')
        # model = self.gradebook_list_controller.get_gradebook_model('nowy_dziennik')
        # ConsoleGradebookListView.wypisz_liste_dziennikow(self.__gradeBooksList_model)
        # self.__gradeBooksList_model.
        # self.gradebook_list_controller.wypisz_liste_dziennikow()
        # self.__gradeBooksList_view.wypisz_liste_dziennikow()
        # while self.controller.get_user_input():
        #     pass

        current_gradebook = None

        while True:
            if current_gradebook is not None:
                print('Aktualny dziennik to: ', current_gradebook)
            print("1 - dodawanie nowego dziennika\n"
                  "2 - dodawanie nowego studenta\n"
                  "3 - przypisanie oceny oraz jej wagi danemu studentowi\n"
                  "4 - policzenie średniej arytmetycznej ocen dla każdego ze studentów\n"
                  "5 - wyświetlenie ocen danego studenta\n"
                  "6 - wyświetl liste studentow\n"
                  "7 - Utwórz nowy dziennik na podstawie starego\n"
                  "8 - Znajdz dziennik po nazwie i przełącz się na niego\n"
                  "9 - Wypisz listę dzienników\n"
                  "10 - exit\n"
                  "\nWybierz: ", end='')

            code = input( )
            if code == '1':
                print('\nDodawanie nowego dziennika...')
                print('\nPodaj nazwe dziennika:', end=' ')
                dziennik = input( )
                self.gradebook_list_controller.stworz_dziennik_i_dodaj_do_listy(dziennik)
                current_gradebook = dziennik
                continue
            if code == '2':
                if current_gradebook is None:
                    print('Najpierw stwórz dziennik ocen')
                else:
                    print('\nDodawanie nowego studenta...')
                    print('\nPodaj imie:', end=' ')
                    nowy_student = input( )
                    # szukamy kontrolera dziennika
                    self.gradebook_list_controller.get_gradebook_controller(current_gradebook).dodaj_studenta(nowy_student)
                continue
            if code == '3':
                if current_gradebook is None:
                    print('Najpierw stwórz dziennik ocen')
                else:
                    print('\nPrzypisanie oceny oraz jej wagi danemu studentowi...')
                    print('\nPodaj imie:', end=' ')
                    szukany_student = input( )
                    print('\nPodaj ocene:', end=' ')
                    ocena = int(input( ))
                    print('\nPodaj wage oceny:', end=' ')
                    waga_oceny = int(input( ))
                    self.gradebook_list_controller.get_gradebook_controller(current_gradebook).get_student_controller(szukany_student).dodaj_ocene(ocena, waga_oceny)
                    # self.gradebook_list_controller.get_gradebook_controller(current_gradebook).dodaj_ocene(
                    #     szukany_student, ocena, waga_oceny)
                continue

            if code == '4':
                if current_gradebook is None:
                    print('Najpierw stwórz dziennik ocen')
                else:
                    print('\nPoliczenie średniej arytmetycznej ocen dla każdego studenta...')
                    self.gradebook_list_controller.get_gradebook_view(current_gradebook)\
                        .wyswietl_srednia_ocen_wszystkich_studentow()
                continue
            if code == '5':
                if current_gradebook is None:
                    print('Najpierw stwórz dziennik ocen')
                else:
                    print('\nWyświetl oceny danego studenta...')
                    print('\nPodaj imie:', end=' ')
                    szukany_student = input( )
                    self.gradebook_list_controller.get_gradebook_controller(current_gradebook)\
                        .get_student_view(szukany_student).wyswietl_oceny()

                continue
            if code == '6' and current_gradebook is not None:
                print('\nWyświetl listę studentów...')
                self.gradebook_list_controller.get_gradebook_view(current_gradebook) \
                    .wypisz_liste_studentow()
                continue
            if code == '7' and current_gradebook is not None:
                print('\nUtwórz nowy dziennik na podstawie starego...')
                print('\nPodaj nazwe:', end=' ')
                nazwa_nowego_dziennika = input( )
                self.gradebook_list_controller.stworz_dziennik_na_bazie_starego(current_gradebook, nazwa_nowego_dziennika)
                current_gradebook = nazwa_nowego_dziennika
                continue
            if code == '8':
                print('\nZnajdz dziennik po nazwie...')
                print('\nPodaj nazwe:', end=' ')
                nazwa_dziennika = input( )
                current_gradebook = nazwa_dziennika
                continue
            if code == '9':
                print('\nWypisz listę dzienników...')
                self.gradebook_list_controller.wypisz_liste_dziennikow()
                continue
            elif code == '10':
                sys.exit( )
            else:
                print("Error - zły numer ")

