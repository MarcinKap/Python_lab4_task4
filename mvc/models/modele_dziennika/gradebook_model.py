from mvc.models.abstract_model import AbstractModel


class Gradebook(AbstractModel):
    def __init__(self, nazwa):
        super( ).__init__( )
        self.__lista_studentow = []
        self.__nazwa = nazwa

    def dodaj_studenta(self, Student):
        self.__lista_studentow.append(Student)

    def wypisz_liste_studentow(self):
        for x in self.__lista_studentow:
            print(f'{x.imie}')
        print('\n')

    def wyszukaj_studenta_po_imieniu(self, imie):
        for x in self.__lista_studentow:
            if (x.imie == imie):
                return x

    def wyswietl_srednia_ocen_wszystkich_studentow(self):
        for x in self.__lista_studentow:
            sr = x.srednia_ocen( )
            if sr == 0:
                print(f'Student {x.imie} nie ma żadnych ocen')
            else:
                print(f'Średnia ocen dla studenta {x.imie} to', end=' ')
                print(x.srednia_ocen( ))
        print('\n')

    def modify(self, *args, **kwargs):
        self.notify( )

    def notify(self):
        for obs in self._obs_list.values( ):
            obs.update(self.__nazwa)
            obs.update(self.__lista_studentow)
