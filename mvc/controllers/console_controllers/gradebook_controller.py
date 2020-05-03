from mvc.controllers.abstract_controller import AbstractController
from mvc.controllers.console_controllers.student_controller import StudentController
from mvc.models.abstract_model import AbstractModel
from mvc.models.modele_dziennika import gradebook_model
from mvc.models.modele_dziennika.gradebook_model import Gradebook
from mvc.models.modele_dziennika.school_grade_model import School_grade
from mvc.models.modele_dziennika.student_model import Student
from mvc.views.widoki_dziennika.console_gradebook_view import ConsoleGradebookView
from mvc.views.widoki_dziennika.console_student_view import ConsoleStudentView


class GradebookController(AbstractController):
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

    def dodaj_studenta(self, imie_nowego_studenta):
        print('wchodzimy tu 1')

        wyszukany_student = self.wyszukaj_studenta_po_imieniu(imie_nowego_studenta)
        if wyszukany_student != None:
            print('Taki student już istnieje - spróbuj ponownie\n')
        else:
            print('Zapisujemy studenta do dziennika')
            nowy_student_model = Student(imie_nowego_studenta)
            nowy_widok_studenta = ConsoleStudentView(imie_nowego_studenta, nowy_student_model)
            nowy_student_model.add_observer(nowy_widok_studenta)
            nowy_kontroler_studenta = StudentController(nowy_student_model, nowy_widok_studenta, imie_nowego_studenta )

            self.model.lista_studentow.append(nowy_student_model)
            self.model.students_view.append(nowy_widok_studenta)
            self.model.students_controllers.append(nowy_kontroler_studenta)
            # dziennik_ocen.dodaj_studenta(Student(nowy_student))

    def dodaj_ocene(self, student, dodawana_ocena, waga_dodawanej_oceny):
        wyszukany_student = self.wyszukaj_studenta_po_imieniu(student)
        ocena = School_grade(dodawana_ocena, waga_dodawanej_oceny)
        if wyszukany_student is not None:
            wyszukany_student.lista_ocen.append(ocena)
            return True
        else:
            return False


    def wyszukaj_studenta_po_imieniu(self, imie):
        for x in self.model.lista_studentow:
            if (x.imie == imie):
                return x

    def get_student_controller(self, imie_studenta):
        for x in self.model.students_controllers:
            if x.name == imie_studenta:
                return x

    def get_student_view(self, imie_studenta):
        for x in self.model.students_view:
            if x.name == imie_studenta:
                return x
