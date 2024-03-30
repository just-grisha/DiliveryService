from datetime import time


class Worker:
    name: str
    age: int
    month_time: time
    is_busy: bool

    def get_order(self):  #
        pass

    # принять заказ, если возможно

    def get_shift(self):  # отработка по времени

        pass  # докрутить статрт рабочей смены придумать график и т.д.
    # получить смену, когда работает


class Courier(Worker):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_order(self):
        pass


class Storekeeper(Worker):
    pass
