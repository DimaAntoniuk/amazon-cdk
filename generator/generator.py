import random
import string
import uuid
import datetime
import json
from ..src.model import Employee

class Generator:
    def generate_random_date():
        start_date = datetime.date(2000, 1, 1)
        end_date = datetime.date(2002, 1, 1)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)

        return random_date


    def genrate_item(self):
        letters = string.ascii_letters
        employee = Employee(
            country = ''.join(random.choice(letters) for _ in range(10)),
            city = ''.join(random.choice(letters) for _ in range(10)),
            warehouse = ''.join(random.choice(letters) for _ in range(10)),
            employee = uuid.uuid4(),
            name = ''.join(random.choice(letters) for _ in range(5)),
            address = ''.join(random.choice(letters) for _ in range(12)),
            date_of_birth = self.generate_random_date(),
            position = ''.join(random.choice(letters) for _ in range(7))
        )
        return employee.__dict__


    def generate_items(self, number):
        with open('items.json', 'w') as items_file:
            items = []
            
            for _ in number:
                item = self.genrate_item()
                items.append(item)
            
            items_file.write(json.dumps(items))
            
            print(f'{number} items generated')


if __name__ == '__main__':
    generator = Generator()
    generator.generate_items()