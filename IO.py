out_file = open("test.txt", "w")
out_file.write("yo this is vishwa pratap singh ")
out_file.close()
in_file= open("test.txt", "rb+")
print(in_file.seek(1))
text =in_file.read()
in_file.close()
print(text)

with open("hello.txt", "w") as file:
    file.write("this is another way to create file handling in python")