class Father:
    def show_father(self):
        print('Father class method')
class Mother:
    def show_mother(self):
        print('Mother class method')
class Child(Father,Mother):
    def show_child(self):
        print("Child class method")
obj = Child()
obj.show_father()
obj.show_mother()
obj.show_child()