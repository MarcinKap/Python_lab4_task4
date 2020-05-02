from .abstract_view import AbstractView
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class MetaView(type(AbstractView), type(QWidget)):
    pass


class MainWindowView(AbstractView, QWidget, metaclass=MetaView):
    def __init__(self, name='MainWindow', model=None):
        super().__init__(name, model)
        self.setLayout(QVBoxLayout())

    def add_component(self, comp):
        super().add_component(comp)
        self.layout().addWidget(comp)

    def update(self, *args, **kwargs):
        pass

    def show(self):
        QWidget.show(self)


class GraphDateView(AbstractView, QLabel, metaclass=MetaView):
    def __init__(self, name, model):
        super().__init__(name, model)

    def add_component(self, comp):
        pass

    def update(self, *args, **kwargs):
        self.setText(str(args[0]))

    def show(self):
        self.model.notify()


class GraphActionButton(AbstractView, QPushButton, metaclass=MetaView):
    def __init__(self, name, model=None):
        super().__init__(name, model)
        self.setText('Click')

    def add_component(self, comp):
        pass

    def update(self, *args, **kwargs):
        pass

    def show(self):
        pass