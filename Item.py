from dataclasses import dataclass, asdict


@dataclass
class Item:
    store_id: int
    provider_id: int
    name: str
    price: float



class ItemHandle:
    def __init__(self, store_id: int, provider_id: int, name: str, price: float):
        self.item = Item(store_id, provider_id, name, price)

    def get_item(self):
        return asdict(self.item)

    def change_item(self, key, val):
        self.item.__dict__[key] = val

    def get_name(self):
        return self.item.name

