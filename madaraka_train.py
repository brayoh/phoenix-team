import json
from pprint import pprint

with open('db.json') as read_file:
  data = json.load(read_file)

class BookTrain(object):
  """docstring for BookTrain."""
  def __init__(self, data):
    super(BookTrain, self).__init__()
    self.data = data

  def choose_train_type(self):
    types = data['trains'][0]['classes']
    print ('We have two types of train:')
    for train_type in types:
      print(train_type['type'])
    self.choose_train_type = raw_input("Which train type do you want to take?:")
    return self.choose_train_type
  def train_chosen(self):
    if self.choose_train_type == 'VIP':
      return 'VIP'
    elif self.choose_train_type == 'Economy':
      return self.choose_train_type
  def seats_available(self):
    no_of_seats = data['trains'][0]['classes']
    print('kindly choose the seat you want, seats available iclude:')
    for seats in no_of_seats:
      print(no_of_seats['available_seats'])

    seat_chosen = raw_input('kindly input your desired seat number from the above:')
    return seat_chosen
  

if __name__ == "__main__":
  book_train = BookTrain(data)
book_train.choose_train_type()

print book_train.seats_available()
