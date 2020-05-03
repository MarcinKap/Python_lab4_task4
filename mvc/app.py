from abc import ABC, abstractmethod
# from models.date_time_model import DateTimeModel
# from views.console_view import ConsoleDateView
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

        self.gradebook_list_controller.stworz_dziennik_i_dodaj_do_listy('nowy_dziennik')

        while self.controller.get_user_input():
            pass