def getData():
    filename="PDC1.csv"
    text_file=open(filename,"r")
    X=[]
    Y=[]
    for line in text_file:
        x,y=line[:-1].split(",")
        X.append(int (x))
        Y.append(int(y))
    text_file.close()
    return X,Y
