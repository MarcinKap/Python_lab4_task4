from .abstract_controller import AbstractController


class ConsoleDateController(AbstractController):
    def __init__(self, model=None, view=None):
        super().__init__(model, view)

    def get_user_input(self):
        obj = input('Type q to quit or s to show date:\n')
        if obj == 'q':
            return False
        elif obj == 's':
            self.model.modify()
        else:
            print('Incorrect value')
        return True

