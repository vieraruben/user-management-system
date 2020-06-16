
from .User import User
from data.helpers import *

class UserDB:
  def __init__(self):
    self.users = {}

  def is_empty(self):
    return len(self.users) == 0

  def valid_user(self, name):
    return self.users.get(name) # return None if user not valid

  def add_user(self, name, salary):
    user = User(name, salary)
    self.users[user.name] = user

  def remove_user(self, name):
    self.users.pop(name) # returns None if not found

  def update_user(self, name, salary):
    if not self.valid_user(name):
      return None
    self.users.get(name).setSalary(salary)
    return True

  def get_user_list(self):
    return [user for key, user in self.users.items()]

  def backup_user_data(self):
    user_data = {key: value.toJSON() for key, value in self.users.items()}
    sava_data('data/user_data.json', user_data)

  def load_user_data(self):
    user_data = load_data('data/user_data.json')
    for key, value in user_data.items():
      self.add_user(value["name"], value["salary"])