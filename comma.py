#Comma Code
#Practice problem from Chapter4

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(my_list):
    for i in range(len(my_list)):
        print(my_list[i], end = ", ")

comma(spam)
