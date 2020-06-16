class Switch:
  
  def __init__(self, user_db):
    self.users_db = user_db

  def check(self, choice):
    default = "" 
    return getattr(self, 'case_' + str(choice), lambda: default)() 

  def case_0(self):
      print("Show user: ")
      name = input("Name: ")
      user = self.users_db.valid_user(name)

      if not user:
        print("User not found")
        return
      
      print(f"User Name: {user.getName()}  User Salary: {user.getSalary()}")


  def case_1(self):
      print("Provide information: ")
      name = input("Name: ")
      salary = int(input("Salary: "))
      self.users_db.add_user(name, salary)

  def case_2(self):
    print("Enter user name to remove")
    name = input("Name: ")
    if not self.users_db.valid_user(name):
      print("User not found!")
      return

    self.users_db.remove_user(name)
    print(f"User {name} has been remove.")

  def case_3(self):
      print("Enter user name to update")
      name = input("Name: ")
      if not self.users_db.valid_user(name):
          print(f"User {name} is not in our DB")
          return

      print("Please, provide new salary")
      salary = int(input("Salary: "))
      self.users_db.update_user(name, salary)

  def case_4(self):
    print("User Database")
    if self.users_db.is_empty():
        print("User db is empty.")
        return
    for user in self.users_db.get_user_list():
        print(f"{user.getName()} - {user.getSalary()}") 

  def case_5(self):
    print("Backup user data")
    self.users_db.backup_user_data() 
    print("Data has been backup")
        
  def case_q(self): # default case
      return "Good Bye!"



      

  


