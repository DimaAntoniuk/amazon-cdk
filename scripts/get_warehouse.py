from src.controller import Controller


def get_items(warehouse):
    controller = Controller()
    return controller.query_by_warehouse(warehouse)


if __name__ == '__main__':
    warehouse = ''
    print(str(get_items(warehouse)))