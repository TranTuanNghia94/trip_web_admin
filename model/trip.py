import datetime


class Trip(object):
    def __init__(self, id_customer, id_driver, distance, pick_up, drop_off,
                 state, driver_cancel, customer_cancel, price):
        self.id_customer = id_customer
        self.id_driver = id_driver
        self.id_trip = id_driver + id_customer
        self.distance = distance
        self.pick_up = pick_up
        self.drop_off = drop_off
        self.state = state
        self.driver_cancel = driver_cancel
        self.customer_cancel = customer_cancel
        self.price = price
        self.date_Create = datetime.datetime.utcnow()

    def convert_trip_to_json(self):
        return {
            'id_trip': self.id_trip,
            'id_customer': self.id_customer,
            'id_driver': self.id_driver,
            'distance': self.distance,
            'pick_up': self.pick_up,
            'drop_off': self.drop_off,
            'price': self.price,
            'state': self.state,
            'customer_cancel': self.customer_cancel,
            'driver_cancel': self.driver_cancel,
            'date_create': self.date_Create

        }


