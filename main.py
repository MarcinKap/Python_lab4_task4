from mvc.app import ConsoleApp
from mvc.controllers.console_date_controller import ConsoleDateController
from mvc.controllers.console_controllers.gradebooks_lists_controller import GradebooksListController
from mvc.graph_app import GraphApp
from mvc.controllers.graphic_date_controller import GraphicDateController


def main_win():
    controller = GraphicDateController()
    app = GraphApp(controller)
    app.run_app()

def main_console():
    controller = ConsoleDateController()
    gradebook_list_controller = GradebooksListController()
    app = ConsoleApp(controller, gradebook_list_controller)
    app.run_app()

if '__main__' == __name__:
    # main_win()
    main_console()
