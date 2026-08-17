import csv
L=[["Name","Company","Price"],["Pen Drive","I-Ball","850"],["CD-Writer","LG","1250"],
   ["Hard-Disk","Seagate","4200"],["Monitor","LG","6500"],["Wireless-Speaker","LG","1900"]]
file=open("Product.csv","w")
with file:
    wrt=csv.writer(file)
    wrt.writerows(L)
