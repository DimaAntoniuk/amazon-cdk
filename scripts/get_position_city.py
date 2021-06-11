from src.controller import Controller


def get_items(position_city):
    controller = Controller()
    return controller.query_by_warehouse(position_city)


if __name__ == '__main__':
    position_city = ''
    print(str(get_items(position_city)))