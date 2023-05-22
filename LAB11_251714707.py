#QUESTION # 1

from math import pi


class Shape:
    def __init__(self, sides):
        self.sides = sides

    def Compute_area(self):
        pass

class Triangle(Shape):
    def __init__(self, sides, height, base):
        super().__init__(sides)
        self.height = height
        self.base = base

    def Compute_area(self):
        return (0.5*self.base*self.height)

class Circle(Shape):
    def __init__(self, sides, radius):
        super().__init__(sides)
        self.radius = radius

    def Compute_area(self):
        return pi*self.radius**2

def main():
    
    myShape = Shape(4)
    myShape.Compute_area()

    myTriangle = Triangle(3, 6, 5)
    print("The area of the triangle is: ", myTriangle.Compute_area())

    myCircle = Circle(0, 4)
    print("The area of the circle is: ", myCircle.Compute_area())

               
main()

#QUESTION # 2


class Employee:
    def __init__(self, EMPname, EMPid, salary):
        self.EMPname = EMPname
        self.EMPid = EMPid
        self.salary = salary

    def SalaryStatus(self):
        print (self.EMPname)
        print (self.EMPid)
        print (self.salary)

class BuildingManager(Employee):
    def __init__(self, EMPname, EMPid, salary):
        super().__init__(EMPname, EMPid, salary)
    
        self.EMPname = EMPname
        self.EMPid = EMPid
        self.salary = salary

    def SalaryStatus(self):
        print ("Name of Building manager is: ", self.EMPname)
        print ("ID of Building manager is: ", self.EMPid)
        print ("Salary of Building manager is: ", self.salary)
        print ("--------------------------------------------")
    
class ProcurementManager(Employee):
    def __init__(self, EMPname, EMPid, salary):
        super().__init__(EMPname, EMPid, salary)

        self.EMPname = EMPname
        self.EMPid = EMPid
        self.salary = salary

    def SalaryStatus(self):
        print ("Name of Procurement manager is: ", self.EMPname)
        print ("ID of Procurement manager is: ", self.EMPid)
        print ("Salary of Procurement manager is: ", self.salary)
        print ("--------------------------------------------")

class LogisticsManager(Employee):
    def __init__(self, EMPname, EMPid, salary):
        super().__init__(EMPname, EMPid, salary)

        self.EMPname = EMPname
        self.EMPid = EMPid
        self.salary = salary

    def SalaryStatus(self):
        print ("Name of Logistics manager is: ", self.EMPname)
        print ("ID of Logistics manager is: ", self.EMPid)
        print ("Salary of Logistics manager is: ", self.salary)
        print ("--------------------------------------------")

def main():

    EmpList = []

    myBuildingManager = BuildingManager("Ahmad", 101, 10000)
    myProcurementManager = ProcurementManager("Faraz", 102, 12000)
    myLogisticsManager = LogisticsManager("Saadiq", 103, 15000)

    EmpList.append(myBuildingManager)
    EmpList.append(myProcurementManager)
    EmpList.append(myLogisticsManager)

    for i in EmpList:
        i.SalaryStatus()

main()

    
    
    

    
        

