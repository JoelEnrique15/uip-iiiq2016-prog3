x = input(" ")
lista=[]
agua=0
fuego=0
while x !="salir":
    if x.find("agua")>=0:
        agua= agua+1
        lista.append(x)

        if x.find("fuego") >=0:
            fuego= fuego+1

    elif x.find("fuego")>=0:
        fuego= fuego+1
        lista.append(x)

    x= input(" ")

print(lista)
print("agua=" +str(agua),"fuego=" +str(fuego))
