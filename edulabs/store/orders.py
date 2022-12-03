
import random

class Shipment:

    STATUES = ("processing", "shipped" , "deliverd")
    counter = 0

    def __init__(self,address):
        self.address = address
        self.status = 0
        Shipment.counter += 1

    def __str__(self):
        return f"{self.status}"


    def change_status_to_next(self):
        if self.status == len(Shipment.STATUES) - 1:
            print('Error')
            return False
        self.status += 1
        return True

    def shipment_status(self):
       print(Shipment.STATUES[self.status])


class Order:

    def __init__(self,customer, address: Shipment):
        self.order_id: int = random.randint(100,100_000)
        self.shipment: Shipment = address
        self.customer = customer
        self.order_items = []


    def __str__(self):
        return  f"customer: {self.customer} | address: {self.shipment} | modle: {self.model} "

    def add_item_to_order(self, sku: str,qty):
        pass


    def total_price(self, amount: int):
        if amount > 0:
            return self.price * amount
        else:
            return "Error"


















































if __name__ == "__main__":
    pass
