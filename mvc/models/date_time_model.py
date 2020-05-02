from .abstract_model import AbstractModel
from datetime import datetime


class DateTimeModel(AbstractModel):
    def __init__(self):
        super().__init__()
        self.__current_date = datetime.now()

    def modify(self, *args, **kwargs):
        self.__current_date = datetime.now()
        self.notify()

    def notify(self):
        for obs in self._obs_list.values():
            obs.update(self.__current_date)