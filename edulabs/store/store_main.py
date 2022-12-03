from store import Store


if __name__ == '__main__':

    # create a store
    gadget_store = Store('Ivory')

    # create a new customer
    gadget_store.add_customer('123123123', 'Valeria', 'netanya', '0456456')
    gadget_store.add_customer('333333333', 'Ziv Attias', 'Yaffo', '0545555555')

    gadget_store.display_customers()

    # create a product
    gadget_store.add_product_to_inventory("aa34v", "laptop", "Apple",
                                          10, 8000, "MacBook Pro 15'", 12)
    gadget_store.add_product_to_inventory("45ghf3", "phone", "Samsumg",
                                          23, 3500, "Galaxy 22", 12)

    gadget_store.place_order('2323232',"zofit",{})


