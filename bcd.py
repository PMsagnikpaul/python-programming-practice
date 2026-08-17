def xyz(z):
    for i in range(len(z)):
        z[i]*=2
        
if __name__=="__main__":
    l=[25,63,69,7,23]
    xyz(l)
    print(l)
