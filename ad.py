#wpp to read a file and find the number of occurance of a word in that particular file.


def count():
    f=open("sp.txt", "r")
    s=f.read()
    count = 0
    x = input("Enter the word you want to search=")
    l=s.split(" ")
    for i in l:
        if i == x:
            count+=1
    print("The number of occurance of the word is=", count)
count()
            
