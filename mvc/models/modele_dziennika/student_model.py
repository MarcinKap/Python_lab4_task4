from mvc.models.abstract_model import AbstractModel


class Student(AbstractModel):

    def __init__(self, imie):
        super( ).__init__( )
        self.lista_ocen = []
        self.imie = imie

    def modify(self, *args, **kwargs):
        self.notify()

    def notify(self):
        for obs in self._obs_list.values():
            obs.update(self.lista_ocen)
            obs.update(self.imie)

    # def przedstaw_sie(self):
    #     print(f"Jestem {self.imie} ")