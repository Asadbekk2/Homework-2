#Task 1

#Я первое не смог понять, как это нужно сделать и что именно нужно, вопроса не понял.

#Task 2
# try:
#     file_text = (input("Write something"))
#     if file_text :
#         with open('example.txt', 'w') as file:
#             content = file.write(file_text)
#             if (content):
#                 print("Your file is created")
#             else:
#                 print("Something isn't working")
#     else:
#         print("Write one more time")
#         file = (input("Write something own"))
# except FileNotFoundError:
#     print("Sorry man your file is not readable")
# except Exception as e:
#     print(f"ur except.. error ocus: {e}")
# except ValueError:
#     print("Error Sorry man something doesn't working")
# except IOError:
#      print("Error: bialbalba")                                

#Task 3
# def main():
#     while True:
#         try:
#             user_input = input("write your number")
#             number = int (user_input)
#             result = 100 / number
#         except ValueError:
#             print("Something is not working number")
#         except ZeroDivisionError:
#             print("Error zero impossible divede with. Please check again")   
#         else:
#             print("Результат деление на 100: {number} равен: {result}")
#             break
#         finally:
#             print("Please try again") 

# if __name__ == "__main__":
#     main()    

#Task 4
# def write_to_filename(filename, data):
#     try:
#         with open(filename, 'w') as file:
#             file.write(data)
#             print("Succesful{file}")
#     except IOError as e:
#          print(f"Something with open file {e}")

# file_name = 'example.txt'
# data_to_write = 'Hello.'

# write_to_filename(file_name, data_to_write)

# try:
#     file_text = (input("Write your essay"))
#     if file_text:
#         with open('example.txt', 'w') as file:
#             content = file.write(file_text)
#             if (content):
#                 print("You file is created")
#             else:
#                 print("Something is gonna wrong")
#     else:
#         print("Write one more time")
#         file = str(input("Write your own essay"))
# except FileNotFoundError:
#     print("Sorry man your file is not readable")
# except IOError:
#     print("Error: bialbalba")                           
# finally:
#     print('This is finally tags')     

#Task 5
# try:
#     file_text = (input("Write about yourself"))
#     if file_text:
#         with open ('example.txt', 'w') as file:
#             content = file.write(file_text)
#             if (content):
#                 print("Succesfull created your file")
#             else:
#                 print("Something is gonna wrong")
# except ValueError:
#     print("Ошибка: введенная строка не является целым числом")
# finally:
#     print("Completion of data processing")#