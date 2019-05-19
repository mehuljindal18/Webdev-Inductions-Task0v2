print('Welcome to Bubble Sorting Algoritm Developed For Spider WebDev Induction')
inputted_list = input('Enter a set of numbers seperated by commas: ')
list = inputted_list.split(',')
number_of_items = int(len(list))

print(list)

position = 0
Pass = 0
counter = 1
while counter == 1:
    number_of_swaps = 1
    counter2 = 0
    permanent_numbers = []
    while number_of_swaps > 0:
        counter2 = counter2 + 1
        number_of_swaps = 0
        while position < number_of_items - 1:
            if int(list[position]) > int(list[position + 1]):
                number_of_swaps = number_of_swaps + 1
                item1 = int(list[position])
                item2 = int(list[position + 1])
                list[position] = item2
                list[position + 1] = item1
            position = position + 1
        Pass =  Pass + 1
        print('pass',Pass,':',list)
        position = 0
        if Pass == number_of_items - 1:
            number_of_swaps = 0
        permanent_numbers.append(list[number_of_items - counter2])
    if number_of_swaps == 0:
        counter = 0


print('total number of passes:', Pass)
