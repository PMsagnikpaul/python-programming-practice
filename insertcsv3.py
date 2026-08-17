import csv
L=[["Name","Salary","Dept"],["Amit","54000","Finance"],
   ["Vikash","43550","IT"],["Rumi","49000","Sales"],["Sonal","61000","Finance"]]
file=open("Staff.csv","w")
with file:
    wrt=csv.writer(file)
    wrt.writerows(L)
