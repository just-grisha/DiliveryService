import time
import asyncio

from create_items import create_items_to_provider
from Item import Item
from random import randint
from order import Order
from workers import Storekeeper, Courier


class Time:
    async def start_global_time(self):
        print("зашло")
        seconds = 0
        while True:
            print(f"Время: {seconds} сек")
            await asyncio.sleep(1)
            seconds += 1
    def get_current_time(self):
        pass
class Provider:  # поставщик

    provider_id = randint(1, 1000)  # пока что реализация такая TODO сделать уникальный id
    items = dict()

    def __init__(self, name, provider_id):
        self.name = name

    def find_item_by_name(self, name):
        for item in self.items.keys():
            if item.name == name:
                return item
        return None

    def send_order(self, request):
        """
        :param request: {item: amount}
        :return: {item: amount}
        """
        order = dict()
        # что если такого товара не существует?
        for key, value in request.items():
            available_amount = self.items[key]
            order[key] = available_amount - request[key]
            self.items[key] -= request[key]
        return order

    # send_order - принять и отправить заказ складу

    def update_stocks(self, what_to_update):
        '''
        Обновляет товары, если товара нет, то создает
        :param what_to_update: { item : amount}
        '''
        # что делать когда нет такого товара?
        for key, value in what_to_update.items():
            item = self.find_item_by_name(key)
            if item is not None:
                self.items[item] += value

    # update_stocks - обновить число товаров на складе

    def create_stock(self):
        self.items = create_items_to_provider(self.provider_id)

    def print_all_provider_items(self):
        print(self.items)
        for key, value in self.items.items():
            print(f"Название: {key.name} | Количество: {value}")


class Store:
    items: [Item]

    def print_all_items(self):
        print("Название   |   стоимость")
        for item in self.items:
            print(item.name, "|", item.price * 2)

    def send_request(self):
        pass

    # send_request - отправить заказ для провайдера (что привезти)

    def take_order(self):
        # set_storkeeper
        pass

    # принять заказ и начать его обрабатывать

    def set_courier(self, items):
        pass

    # дать заказу курьера

    def set_storekeeper(self):
        pass

    # дать заказу кладовщика

    def get_worker(self):
        pass

    # взять работника к себе и дать ему смену


# Что находится в заказе? Статус доставки, список товаров, время создания-время доставки, кто собирал-доставлял


class User:
    def make_order(self):
        # get_order_data_from_user()
        pass

    # сделать заказ

    def take_order(self):
        pass
    # забрать заказ


if __name__ == '__main__':
    provider1 = Provider("Поставщик1", 77)
    provider1.create_stock()
    provider1.print_all_provider_items()
    what_to_update = {"Чайник": 5000}
    provider1.update_stocks(what_to_update)
    provider1.print_all_provider_items()
    mytime = Time()
    time_task = asyncio.create_task(mytime.start_global_time())
    # Другие команды, которые могут выполняться параллельно с таймером

    # Пример:
    asyncio.sleep(5)
    print("Прошло 5 секунд")

    # Ждем завершения задачи таймера
    await time_task


