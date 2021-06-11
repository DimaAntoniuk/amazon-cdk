from src.controller import Controller


def get_items(city):
    controller = Controller()
    return controller.query_by_city(city)


if __name__ == '__main__':
    city = ''
    print(str(get_items(city)))