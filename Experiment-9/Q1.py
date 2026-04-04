class Student:
    def get_data(self):
        self.name=input('Enter student namme : ')
        self.sap_id=input("Enter the student id : ")
        self.phy=float(input('Enter the physics marks: '))
        self.chem=float(input('Enter the chemistry marks: '))
        self.math=float(input('Enter the mathematics marks: '))
    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Sap ID:", self.sap_id)
        print("Name:", self.phy)
        print("Name:", self.chem)
        print("Name:", self.math)
s1= Student()
s1.get_data()
s1.display()
        
s2= Student()
s2.get_data()
s2.display()

s3= Student()
s3.get_data()
s3.display()