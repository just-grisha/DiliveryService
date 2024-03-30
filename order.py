from dataclasses import dataclass


@dataclass
class Order:
    status: str
    items: {Item: int}
    create_order_time: time
    delivery_order_time: time
    storekeeper: Storekeeper
    courier: Courier
