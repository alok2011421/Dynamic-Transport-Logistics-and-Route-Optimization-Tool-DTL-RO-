class Order:
    def __init__(self, id, weight, lat, lng):
        self.id = id
        self.weight = weight
        self.lat = lat
        self.lng = lng


class Vehicle:
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity
        self.current_load = 0
        self.route = []

    def can_add(self, order):
        return self.current_load + order.weight <= self.capacity

    def add_order(self, order):
        if self.can_add(order):
            self.route.append(order)
            self.current_load += order.weight
            return True
        return False