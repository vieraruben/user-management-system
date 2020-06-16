import json

class User:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def getName(self):
    return self.name

  def getSalary(self):
    return self.salary

  def setSalary(self, new_salary):
    self.salary = new_salary

  def toJSON(self):
        return {
          "name": self.getName(),
          "salary": self.getSalary()
        }