st="Mississippi"
def most_frequent(stri):
    i=0
    s=0
    m=0
    p=0
    for j in stri:
        if j=="i" or j=="I":
            i+=1
        if j=="s" or j=="S":
            s+=1
        if j=="m" or j=="M":
            m+=1
        if j=="p" or j=="P":
            p+=1
    print("i=",i,"s=",s,"m=",m,"p=",p)

most_frequent(st)
