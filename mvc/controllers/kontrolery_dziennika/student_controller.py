from mvc.controllers.abstract_controller import AbstractController
from mvc.models.abstract_model import AbstractModel
from mvc.models.modele_dziennika.school_grade_model import School_grade


class StudentController(AbstractController):
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

    def dodaj_ocene(self,dziennik_ocen, student, dodawana_ocena, waga_dodawanej_oceny):
        print('\nPrzypisanie oceny oraz jej wagi danemu studentowi...')
        print('\nPodaj imie:', end=' ')
        wyszukany_student = dziennik_ocen.wyszukaj_studenta_po_imieniu(student)
        if wyszukany_student is not None:
            wyszukany_student.dodaj_ocene(School_grade(dodawana_ocena, waga_dodawanej_oceny))
        else:
            print('Nie udalo sie znaleźć studenta\n')
