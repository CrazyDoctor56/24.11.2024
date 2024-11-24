with open("quotes.txt", "r", encoding = "utf-8") as file:
    data = file.read()

print(data)

question = input("Бажаєте додати автора? 1 - так, 2 - ні")

if question == "1":
    avtor = input("Введіть ім'я автора:")

    with open("quotes.txt", "a", encoding = "utf - 8") as file:
        file.write(f"\n({avtor})\n")
        

else:
    print("Bye, Bye!")