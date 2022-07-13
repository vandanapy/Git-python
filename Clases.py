#1) what is class and object and write an example
Class:- is a userdefined blueprint from which object is if created:
    EX:-
class Car:
      carname="breza"
      carmodel=2022
      price="15lakh"
      def display(self):
          # self.carname=carname
          print("carname=:" ,self.carname)
          print("carmodel=:", self.carmodel)
          print("carprice=:", self.price)
obj=Car()
obj.display()


#2) what is constructor and use with example
The __init__ method is called constructor
Constructors are used to initializing the object’s state. Like methods, a constructor also contains a collection of statements that are executed at the time of Object creation.
It runs as soon as an object of a class is instantiated.
class Animal:
    def __init__(self):
        self.name="dog"
        self.color="black"
        self.gen="male"
        print(self.name)
        print(self.color)
        print(self.gen)
obj=Animal()



#4) how to access one class data into another class
   using class name

#5) what is inner class and how to access inner class data write two methods
class inside th class is called inner class
class Vehicals:
     def __init__(self):
         self.name="car"
         self.color="white"
     def display_car(self):
         print("car details",self.name)
         print("car details", self.color)
     class Bus:
        def display_busdetails(self):
            print("busdetails")

obj=Vehicals()
obj.display_car()
obj.Bus().display_busdetails()

Method #2
class Vehicals:
     def __init__(self):
         self.obj1=self.Bus()
         self.obj1.display_busdetails()
         self.name="car"
         self.color="white"
     def display_car(self):
         print("car details",self.name)
         print("car details", self.color)
     class Bus:
        def display_busdetails(self):
            print("busdetails")

obj=Vehicals()
obj.display_car()



6) what is refernce variable how to acess data using that ?
self is the reference varaible we can acess data by using self.