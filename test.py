import tests as test
import functions as lib

if __name__ == '__main__':
    
    for i in test.cases:
        if lib.count_all(i[1], i[2]) == i[3]:
            print("Test #" + str(i[0]) + ': OK!')
        else:
            print("Test #" + str(i[0]) + ': KO!')