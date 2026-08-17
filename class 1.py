class Taximeter:
    taxino = 0
    name =""
    km = 0
    cost=0
    def input1(self):
        self.taxino = int(input("Kaka tmr taxi no kotoh? "))
        self.name = input("kaka pechone ke bose a6e ? ")
        self.km = int(input("Kotho dur nea gale km ? "))
    def calc(self):
        if self.km<= 1:
            self.cost=self.km*25
        elif self.km>1 and self.km<=6:
            self.cost = self.km*10
        elif self.km>6 and self.km<=12:
            self.cost = self.km*15
        elif self.km>12 and self.km<=18:
            self.cost = self.km*20
        elif self.km>18:
            self.cost = self.km*25
    def display(self):
        self.input1()
        self.calc()
        print("Taxino\t\tName\t\tKilometers travelled\t\tBill Amount")
        print(self.taxino,"\t\t",self.name,"\t\t",self.km,"\t\t\t",self.cost)
obj=Taximeter()
obj.display()
        
        
        
