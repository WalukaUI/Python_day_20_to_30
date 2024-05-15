# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": 123456}
#     print(a_dictionary["wrongkey"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_msg:
#     print(f"The key {error_msg} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that i made")


height = float(input("heigh"))
wiight = float(input("weight"))

if height > 3:
   raise ValueError("Human height should be lover than 3 m")