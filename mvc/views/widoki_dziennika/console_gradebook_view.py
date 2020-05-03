from mvc.views.abstract_view import AbstractView


class ConsoleGradebookView(AbstractView):
    def __init__(self, name, model):
        super( ).__init__(name, model)
        self.model = model

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

    def wypisz_liste_studentow(self):
        print('\nWyświetl listę studentów...')
        print('Lista studentów:')
        for x in self.model.lista_studentow:
            print(f'{x.imie}')
        print('\n')
        # dziennik_ocen.wypisz_liste_studentow( )

    def wyswietl_srednia_ocen_wszystkich_studentow(self):
        for student in self.model.lista_studentow:
            if (len(student.lista_ocen) > 0):
                sum = 0
                suma_wag = 0
                for ocena in student.lista_ocen:
                    sum = sum + ocena.ocena * ocena.waga_oceny
                    suma_wag = suma_wag + ocena.waga_oceny
                srednia = sum / suma_wag
            else:
                srednia = 0

            if srednia == 0:
                print(f'Student {student.imie} nie ma żadnych ocen')
            else:
                print(f'Średnia ocen dla studenta {student.imie} to', end=' ')
                print(srednia)
        print('\n')