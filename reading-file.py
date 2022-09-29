


count = 0
with open('textfile.txt') as fp:
    for line in fp:
        if line.strip():
            count += 1

print('number of non-blank lines', count)

first_name= input("enter name: ")
second_name= input("enter name: ")
update_count = count+1
print(update_count)
name = f"{update_count}. my name is {first_name} {second_name} \n"
myfile= open("textfile.txt", "a") 

print(name)
myfile.write(name)
myfile.close()