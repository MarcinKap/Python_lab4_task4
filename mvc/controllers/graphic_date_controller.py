from mvc.controllers.abstract_controller import AbstractController


class GraphicDateController(AbstractController):
    def __init__(self, model=None, view=None):
        super().__init__(model, view)
        if view:
            view.clicked.connect(self.get_user_input)

    @AbstractController.view.setter
    def view(self, value):
        if value:
            self._view = value
            self.view.clicked.connect(self.get_user_input)

    def get_user_input(self):
        self.model.modify()