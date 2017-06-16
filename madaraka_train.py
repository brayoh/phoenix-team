import json
from pprint import pprint

with open('db.json') as read_file:
    data = json.load(read_file)

class BookTrain(object):
    """docstring for BookTrain."""
    def __init__(self, data):
        super(BookTrain, self).__init__()
        self.data = data
        self.get_user_details()

    def get_user_details(self):
        option = 0
        print("Select option:")
        print(1,"Available seats")
        print(2,"Book seat")
        choice = input("enter choice: ")
        if choice == 1:
            name = input("Enter name: ")
            if name != "" :
                Id = input("Enter ID number: ")
            if Id:
                phone = input("Enter phone number: ")
        else:
            print("please enter a valid choice")

    def write(self):
        with open('db.json', 'w') as write_file:
            json.dump(self.data, write_file)


if __name__ == "__main__":
    book_train = BookTrain(data)
