class Father:
    def show_father(self):
        print('This is the father class')
class Son(Father):
    def show_son(self):
        print('This the son class')
obj = Son()
obj.show_father()
obj.show_son()
