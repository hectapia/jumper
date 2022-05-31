# By Hector Olivares Tapia.
# What is encapsulation and why is it important?
# How did you apply encapsulation to your program's design?
# How did you use access control in the completed program?

class Encapsulation:
    def __init__(self):
        self.a = "Public variable (no encapsulated)"
        self._b = "Protected variable (encapsulated)" # protected member
        self.__c = "Private variable (encapsulated)"  # private member
 
    def public(self,d):
        self.a = self.a + d
        print(f"\nCalling Public method: {self.a}")


    def _protected(self,e):
        self._b = self._b + e
        print(f"Calling Protected method: {self._b}")

    # It is possible to use or change a private variable through a Public method into the same class.
    def __private(self,g):
        self.__c = self.__c + g
        print(f"\nCalling Private method through a Public method into the same class: {self.__c}")


    def use_public_member(self,g):
            self.__private(g)

obj = Encapsulation()

print(f"\nPrinting: ", end="")
print(obj.a)
obj.a = "Public variable (no encapsulated), changed outside of its class\n"
print(obj.a)

print(f"Printing: ", end="")
print(obj._b)
obj._b = "Protected variable (encapsulated) changed outside of its class\n"
print(obj._b)

obj = Encapsulation()
try:
    print(f"Printing: ", end="")
    print(obj.__c)
except BaseException as err:
    print(f"Expected {err=}, {type(err)=}")
    print("          It is not possible to directly use a private variable outside its class.")  

d = " changed inside of its class"
obj.public(d)
e = " changed inside of its class"
obj._protected(e)

# It is possible to use or change a private variable through a Public method into the same class.
g = " changed inside of its class"
obj.use_public_member(g)
print("        It is possible to use or change a private variable through a Public method into the same class.\n") 
