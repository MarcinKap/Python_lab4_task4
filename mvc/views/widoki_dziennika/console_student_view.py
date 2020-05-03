from mvc.views.abstract_view import AbstractView


class ConsoleStudentView(AbstractView):
    def __init__(self, name, model):
        super( ).__init__(name, model)
        self.model = model

    def add_component(self, comp):
        pass

    def update(self, *args, **kwargs):
        print('Current date is {0}'.format(args[0]))

    def show(self):
        self.model.notify( )

    def wyswietl_oceny(self):
        if (len(self.model.lista_ocen) > 0):
            print('Lista ocen: ')
            for obiekt_school_grade in self.model.lista_ocen:
                print(f'Ocena: {obiekt_school_grade.ocena}, waga oceny: {obiekt_school_grade.waga_oceny}')

            print("\n")
        else:
            print('Ten student nie ma żadnej oceny')

    def przedstaw_sie(self):
        print(f"Jestem {self.model.imie} ")