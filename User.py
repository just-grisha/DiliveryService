class User:
    def __init__(self, user_id, name, address):
        self.user_id = user_id
        self.name = name
        self.address = address

    def make_order(self, order_items):
        return order_items

    def confirm_order(self, available_items):
        # Возвращает True, если пользователь соглашается с уменьшенным заказом
        return input("Некоторые товары отсутствуют. Хотите подтвердить заказ? (да/нет) ").strip().lower() == 'да'
