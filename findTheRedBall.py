import random as r
print('Can you find the RED BALL')
print('Give it a try')
def shuffle_list(lst):
    r.shuffle(lst)   
    return lst

def player_guess():
    guess  = ''
    while guess not in ['0','1','2']:
        guess = input('Pick a number 0, 1, or 2: ')
    return  int(guess)

def check_guess(result, index):
    if result[index]== 'red ball':
        print('Hurray you found the red Ball')
        print(result)
    else:
        print('Better luck next time')
        print(result)

def main():

    myList = ['','red ball', '']
    print(myList)
    result = shuffle_list(myList)
    index = player_guess()

    check_guess(result,index)
    choice = (input('Do you wanna try again: y or n --> ')).lower()
    print(choice)
    if choice == 'y':
        main()
    else:
        print('Bye')
main()

