from src.controller import Controller


def get_items(position, city):
    controller = Controller()
    return controller.query_by_position_in_a_city(position, city)


if __name__ == '__main__':
    position = 'pJiCZTf'
    city = 'eOSRWnPGBZ'
    print(str(get_items(position, city)))