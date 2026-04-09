import math

def get_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def optimize_route(order_objects, vehicle):
    """
    Nearest Neighbor Optimization with Vehicle Constraint
    """

    if not order_objects:
        return []

    current = order_objects[0]
    vehicle.add_order(current)

    remaining = order_objects[1:]

    while remaining:
        nearest = None
        min_dist = float('inf')

        for order in remaining:
            dist = get_dist(
                (current.lat, current.lng),
                (order.lat, order.lng)
            )

            if dist < min_dist and vehicle.can_add(order):
                min_dist = dist
                nearest = order

        if nearest is None:
            break

        vehicle.add_order(nearest)
        remaining.remove(nearest)
        current = nearest

    return vehicle.route