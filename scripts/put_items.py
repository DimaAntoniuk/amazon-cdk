import json
from src.controller import Controller


def put_items(items):
    controller = Controller()
    for item in items:
        controller.put_employee(item)


if __name__ == '__main__':
    with open('items.json') as items_file:
        items = json.load(items_file)
        put_items(items)
