spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(my_list):
    for i in range(len(my_list)):
        if i < len(my_list) - 1:
            print(my_list[i], end = ", ")
        else:
            print("and " + my_list[i])

comma(spam)
