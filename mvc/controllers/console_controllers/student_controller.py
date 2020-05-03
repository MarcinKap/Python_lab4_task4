from mvc.controllers.abstract_controller import AbstractController
from mvc.models.abstract_model import AbstractModel
from mvc.models.modele_dziennika.school_grade_model import School_grade


class StudentController(AbstractController):
    def __init__(self, model, view, name):
        super().__init__(model, view)
        self.name = name

    def get_user_input(self):
        obj = input('Type q to quit or s to show date:\n')
        if obj == 'q':
            return False
        elif obj == 's':
            self.model.modify()
        else:
            print('Incorrect value')
        return True

    def dodaj_ocene(self, dodawana_ocena, waga_dodawanej_oceny):
        ocena = School_grade(dodawana_ocena, waga_dodawanej_oceny)
        self.model.lista_ocen.append(ocena)

    def srednia_ocen(self):
        if (len(self.model.__lista_ocen) > 0):
            sum = 0
            suma_wag = 0
            for x in self.model.__lista_ocen:
                sum = sum + x.ocena * x.waga_oceny
                suma_wag = suma_wag + x.waga_oceny
            return sum / suma_wag
        else:
            return 0