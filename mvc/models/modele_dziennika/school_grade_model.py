from mvc.models.abstract_model import AbstractModel


class School_grade(AbstractModel):

    def __init__(self, ocena, waga_oceny):
        super( ).__init__( )
        self.ocena = ocena
        self.waga_oceny = waga_oceny

    def modify(self, *args, **kwargs):
        self.notify()

    def notify(self):
        for obs in self._obs_list.values():
            obs.update(self.ocena)
            obs.update(self.waga_oceny)