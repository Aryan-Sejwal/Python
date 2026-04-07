class Parent:
    def show_parent(self):
        print("Parent class method")
class Child1 (Parent):
    def show_child1(self):
        print("Child1 class method")
class Child2(Parent):
    def show_child2(self):
        print("Child2 class method")
obj1=Child1()
obj1.show_parent()
obj1.show_child1()
obj2=Child2()
obj2.show_parent()
obj2.show_child2()