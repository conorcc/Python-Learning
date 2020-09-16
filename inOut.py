def write():
    f = open('testing.txt', mode='wt', encoding='utf-')
    f.write('this is the first piece of text \n'
            'this is the next piece \n')
    f.close()


def read():
    f = open('testing.txt', mode='rt', encoding='utf-')
    print(f.read())
    f.close()


def append():
    f = open('testing.txt', mode='at', encoding='utf-8')
    f.write('This is another line I added')
    f.close()


if __name__ == '__main__':
    f = open('testing.txt', mode='rt',  encoding='utf-8')
    for line in f:
        print(line)
