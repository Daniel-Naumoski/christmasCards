with open("employees.txt", mode="r", encoding="utf8") as my_file1:
    content=my_file1.readline() #Alice

    with open("template.txt", mode="r", encoding="utf8") as my_file2:
        content2=my_file2.read()
        with open('christmasCards/"Alice.txt"', mode="w", encoding="utf8") as my_file3:
            content3=content2.replace("NAME",content)
    
    content=my_file1.readline() #John
    with open("template.txt", mode="r", encoding="utf8") as my_file2:
        content2=my_file2.read()
        with open('christmasCards/"John.txt"', mode="w", encoding="utf8") as my_file3:
            content3=content2.replace("NAME",content)


    content=my_file1.readline() #Emily
    with open("template.txt", mode="r", encoding="utf8") as my_file2:
        content2=my_file2.read()
        with open('christmasCards/"Emily.txt"', mode="w", encoding="utf8") as my_file3:
            content3=content2.replace("NAME",content)
    
    content=my_file1.readline() #Michael
    with open("template.txt", mode="r", encoding="utf8") as my_file2:
        content2=my_file2.read()
        with open('christmasCards/"Michael.txt"', mode="w", encoding="utf8") as my_file3:
            content3=content2.replace("NAME",content)
    
    content=my_file1.readline() #Sofia
    with open("template.txt", mode="r", encoding="utf8") as my_file2:
        content2=my_file2.read()
        with open('christmasCards/"Sofia.txt"', mode="w", encoding="utf8") as my_file3:
            content3=content2.replace("NAME",content)
    
