from mvc.views.abstract_view import AbstractView


class ConsoleGradebookView(AbstractView):
    def __init__(self, name, model):
        super( ).__init__(name, model)

    def add_component(self, comp):
        pass

    def update(self, *args, **kwargs):
        print('Current date is {0}'.format(args[0]))

    def show(self):
        self.model.notify( )

    def srednia_arytmetyczna_ocen(self, dziennik_ocen):
        print('\nPoliczenie średniej arytmetycznej ocen dla każdego studenta...')
        # self.model.\
        #     dziennik_ocen.wyswietl_srednia_ocen_wszystkich_studentow( )

    def oceny_danego_studenta(self, dziennik_ocen, szukany_student):
        wyszukany_student = dziennik_ocen.wyszukaj_studenta_po_imieniu(szukany_student)
        if (wyszukany_student != None):
            dziennik_ocen.wyszukaj_studenta_po_imieniu(szukany_student).wyswietl_oceny( )
        else:
            print('Nie udalo sie znaleźć studenta\n')

    def wypisz_liste_studentow(self, dziennik_ocen):
        print('\nWyświetl listę studentów...')
        print('Lista studentów:')
        dziennik_ocen.wypisz_liste_studentow( )
