from mvc.controllers.app import ConsoleApp
from mvc.controllers.console_date_controller import ConsoleDateController
from mvc.controllers.graph_app import GraphApp
from mvc.controllers.models_controllers.graphic_date_controller import GraphicDateController


def main_win():
    controller = GraphicDateController()
    app = GraphApp(controller)
    app.run_app()

def main_console():
    controller = ConsoleDateController()

    app = ConsoleApp(controller)
    app.run_app()

if '__main__' == __name__:
    # main_win()
    main_console()
