file_string = str(input("Enter Text here:"))

def write(text):
    file_object = open("testfile","w")
    file_object.write(text)
    file_object.close()

write(file_string)