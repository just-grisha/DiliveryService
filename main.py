import time
import asyncio

from create_items import create_items_to_provider
from Item import Item
from random import randint
from order import Order
from provider import Provider
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

class Store:
    store_id= randint(1,1000)
    store_items = dict()
    provider = Provider()

    def __init__(self,name,store_id):
        self.name = name
        self.store_id = store_id

    def print_all_items(self):
        print("Название   |   стоимость")
        for item in self.store_items:
            print(item.name, "|", item.price * 2)

    def find_provider(self):
        pass # для 2 части

    def send_request(self,request,provider):
        self.provider = provider
        provider.take_order(request)
    # send_request - отправить заказ для провайдера (что привезти)

    def take_order(self):
        # set_storekeeper()
        order = self.provider.send_order()
        for key, value in order.order_items.items():
            item_to_add = self.provider.find_item_by_name(key)
            item_to_add.store_id = self.sotre_id
            self.store_items[item_to_add] = value
        pass

    # принять заказ и начать его обрабатывать

    def set_courier(self):
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


