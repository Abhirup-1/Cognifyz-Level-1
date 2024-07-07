def pyramid():
    # for decreasing triange with spaces
    for i in range(5):
        for j in range(i,5):
            print(' ',end=' ')
        #for right triangle
        for j in range(i):
            print('2',end=' ')
        # for increasing triangle
        for j in range(i+1):
            print('2',end=' ')
        print()

def right_triangle():
    for i in range(5):
        for j in range(5-i):
            print(' ',end=' ')
        for j in range(i+1):
            print('1',end=' ')
        print()

def right_triangle_down():
    for i in range(5):
        for j in range(i+1):
            print(' ',end=' ')
        for j in range(5-i):
            print('1',end=' ')
        print()

def increasing_triangle():
    for i in range(5):
        for j in range(i+1):
            print('1',end='  ')
        print()

def decreasing_triangle():
    for i in range(5):
        for j in range(5-i):
            print('1',end='  ')
        print()

def square():
    for i in range(5):
        for j in range(5):
            print('1',end='  ')
        print()

while(True):
    print('Which pattern do you want to make ? ')
    print('------------------------------------')
    print('1. right_triangle ')
    print('2. increasing_triangle ')
    print('3. decreasing_triangle ')
    print('4. Square ')
    print('5. right_triangle_down')
    print('6. pyramid')
    print('7. exit')
    print('------------------------------------')

    choice = int(input('Enter your choice: '))

    match choice:
        case 1: 
            right_triangle()
        case 2:
            increasing_triangle()
        case 3:
            decreasing_triangle()
        case 4:
            square()
        case 5: 
            right_triangle_down()
        case 6: 
            pyramid()
        case 7:
            exit(1)
        case default:
            print('No shapes found !')

