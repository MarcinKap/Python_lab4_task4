from mvc.views.abstract_view import AbstractView


class ConsoleGradebookListView(AbstractView):
    def __init__(self, name, model):
        super( ).__init__(name, model)
        self.model = model

    def add_component(self, comp):
        pass

    def update(self, *args, **kwargs):
        print('Current date is {0}'.format(args[0]))

    def show(self):
        self.model.notify( )

    @staticmethod
    def wypisz_liste_dziennikow(gradebook_list):
        print('\nWypisz listę dzienników...')
        for x in gradebook_list.lista_dziennikow:
            print(f'{x.nazwa}')
        print('\n')

