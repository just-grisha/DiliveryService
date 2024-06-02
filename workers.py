from abc import ABC, abstractmethod
import time
import random

class Worker(ABC):
    def __init__(self, worker_id, name, wage_per_hour=300):
        self.worker_id = worker_id
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.shift_start_time = None
        self.shift_hours = 0

    def perform_work(self,order):
        pass

    def start_shift(self, hours):
        self.shift_start_time = time.time()
        self.shift_hours = hours

    def end_shift(self):
        if self.shift_start_time is None:
            raise Exception("Shift not started")
        elapsed_time = time.time() - self.shift_start_time
        earned_wage = (elapsed_time / 3600) * self.wage_per_hour
        self.shift_start_time = None
        self.shift_hours = 0
        return earned_wage

class Storekeeper(Worker):
    def perform_work(self, order):
        if random.random() < 0.1:  # 10% вероятность, что сборщик не явится
            print(f"Сборщик {self.name} не пришел")
            return False
        print(f"{self.name} пакует заказ")
        time.sleep(1 * len(order.order_items))  # Предположим, что сборка каждого товара занимает 1 секунду
        print(f"{self.name} упаковал заказ")
        return True
class Courier(Worker):
    def perform_work(self, order, warehouse_coords, user_coords,):
        if random.random() < 0.1:  # 10% вероятность, что курьер не явится
            print(f"Курьер {self.name} Не пришел")
            return False
        delivery_time = self.calculate_delivery_time(warehouse_coords, user_coords)
        print(f"Дотавляет заказ {order.id}. Время ожидния: {delivery_time} секунд.")
        time.sleep(1)# ну тут он должен доставлять delivery_time
        return True

    def calculate_delivery_time(self, user_coords, store_coords):
        try:
            distance = ((user_coords[0] - store_coords[0])**2 + (user_coords[1] - store_coords[1])**2)**0.5
        except:
            distance = 1

        delivery_time = distance * 30 + 60 + 60
        return delivery_time
