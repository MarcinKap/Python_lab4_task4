from mvc.controllers.abstract_controller import AbstractController
from mvc.models.abstract_model import AbstractModel
from mvc.models.modele_dziennika.student_model import Student


class GradebookController(AbstractController):
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

    def dodaj_studenta(self, dziennik_ocen, nowy_student):
        wyszukany_student = dziennik_ocen.wyszukaj_studenta_po_imieniu(nowy_student)
        if wyszukany_student != None:
            print('Taki student już istnieje - spróbuj ponownie\n')
        else:
            print('wchodzimy zapisac uz')
            dziennik_ocen.dodaj_studenta(Student(nowy_student))

    def srednia_arytmetyczna_ocen(self, dziennik_ocen):
        print('\nPoliczenie średniej arytmetycznej ocen dla każdego studenta...')
        dziennik_ocen.wyswietl_srednia_ocen_wszystkich_studentow( )

    def ocena_danego_studenta(self, dziennik_ocen, szukany_student):
        print('\nWyświetl oceny danego studenta...')
        wyszukany_student = dziennik_ocen.wyszukaj_studenta_po_imieniu(szukany_student)
        if (wyszukany_student != None):
            dziennik_ocen.wyszukaj_studenta_po_imieniu(szukany_student).wyswietl_oceny( )
        else:
            print('Nie udalo sie znaleźć studenta\n')

    def wypisz_liste_studentow(self, dziennik_ocen):
        print('\nWyświetl listę studentów...')
        print('Lista studentów:')
        dziennik_ocen.wypisz_liste_studentow( )
