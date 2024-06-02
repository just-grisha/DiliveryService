import time
from datetime import time as time_of_day, datetime, timedelta

from order import Order
from provider import Provider
from store import Store
from workers import Storekeeper, Courier
from User import User
from Item import Item

if __name__ == '__main__':
    # Создаем поставщиков и склады
    provider1 = Provider("Поставщик1", 1)
    store1 = Store("Склад 1", 1, (10, 10), open_time=time_of_day(8, 0), close_time=time_of_day(22, 0))
    store2 = Store("Склад 2", 2,(5,5), open_time=time_of_day(0, 0), close_time=time_of_day(23, 59))
    stores = [store1, store2]

    store1.add_provider(provider1)

    store2.add_provider(provider1)

    # Обновляем сток у поставщика
    stock_items = {
        Item("Item1", 200, 1): 10,
        Item("Item2", 150, 1): 5,
    }
    provider1.update_stocks(stock_items)
    provider1.print_all_provider_items()
    store1.receive_stock(provider1.inventory)
    # Создаем работников
    storekeeper1 = Storekeeper(1, "John")
    courier1 = Courier(2, "Doe")
    storekeeper2 = Storekeeper(3, "Alice")
    courier2 = Courier(4, "Bob")

    # Создаем пользователя
    user = User(1, "Charlie", (10, 10))

    # Пользователь делает заказ
    order_items = {
        Item("Item1", 200, 1): 5,
        Item("Item2", 150, 1): 2,
    }

    user_order = user.make_order(order_items)
    current_time = datetime.now()
    available_stores = []

    for store in stores:
        if store.is_open(current_time):
            delivery_time = store.calculate_delivery_time(user.address)
            available_stores.append((store, delivery_time))

    if available_stores:
        best_store, delivery_time = min(available_stores, key=lambda x: x[1]) # сравниваем по второму элементу ( по времени доставки)
    else:
        best_store, delivery_time = None, None

    print(f"Сток склада {best_store.name}:")
    best_store.print_all_items()

    if best_store:
        available_items = best_store.process_user_order(user_order)
        if available_items != user_order and not user.confirm_order(available_items):
            print("Заказ отменен пользователем из-за нехватки товаров.")
        else:
            order = Order(
                id = 1,
                status="В обработке",
                order_items=available_items,
                create_order_time=datetime.now(),
                delivery_order_time=None,
                storekeeper=None,
                courier=None
            )
            best_store.start_work(order, storekeeper1, courier1,user.address)
            print(f"Заказ передан на склад {best_store.name}")
            if courier1.perform_work(order, best_store, user.address):
                order.delivery_order_time = datetime.now() + timedelta(seconds=delivery_time)
                order.status = "Доставлен",
                print(f"Заказ доставлен")
            else:
                print("Курьер не явился. Заказ отменен.")
                # Применить штраф к курьеру
                courier1.wage_per_hour -= 50

            print(f"Обновленный сток склада {best_store.name}:")
            best_store.print_all_items()
    else:
        print("Нет доступных складов для обработки заказа в данный момент.")
