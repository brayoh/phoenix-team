import json
from pprint import pprint

with open('db.json') as read_file:
    data = json.load(read_file)

class BookTrain(object):
    """docstring for BookTrain."""
    def __init__(self, data):
        super(BookTrain, self).__init__()
        self.data = data
        
    def write(self):
        with open('db.json', 'w') as write_file:
            json.dump(self.data, write_file)


if __name__ == "__main__":
    book_train = BookTrain(data)
