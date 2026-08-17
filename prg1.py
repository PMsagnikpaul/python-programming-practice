def arrange():
    f= open("E:\practcs\myfile.txt","r")
    s = f.read()
    l=s.split(" ")
    for i in l:
        print(i, end="#")

arrange()
