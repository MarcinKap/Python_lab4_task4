from mvc.views.abstract_view import AbstractView


class ConsoleStudentView(AbstractView):
    def __init__(self, name, model):
        super( ).__init__(name, model)

    def add_component(self, comp):
        pass

    def update(self, *args, **kwargs):
        print('Current date is {0}'.format(args[0]))

    def show(self):
        self.model.notify( )
