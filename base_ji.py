fun = input("Введте 'проверка' или 'добавить': ")
fun = fun.replace(" ","")
if fun =="проверка":
    link=input("Введите ссылку для проверки: ")
    link = link.split()
    #print(type(link))
    with open ("base.txt","r") as base:
        base = (base.read())
        base = base.split(",")
       
        new_base= []

        for link_ in base:
            new_base.append(link_)
        new_base=list(set(new_base))
        print(link)
        print(new_base)
        if list[link]in new_base:
            print("Попався")
        
            
            
        #print(new_base)
        #print(type(new_base))


elif fun =="добавить" : 
    link = input("Введите ссылку или исполльзуйте пробелы для разделения ссылок: ")
    link += " "+link
    link =link.replace(" ",",")
    with open ("base.txt","a") as base:
        base.write((link))
    



   
