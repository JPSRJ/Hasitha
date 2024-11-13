import sys


def final_out(words, words_exsist_counter):
    vertical_print = 0
    horizontal_print = 0
    max_len = 0
    for i in words:
        if len(i) > max_len:
            max_len = len(i)

    print('-'*(max_len+31))
    print('|  words'+' '*(max_len-3)+'|  Repetition frequency  |')
    print('-'*(max_len+31))
    for j in words:
        print('|  '+j+' '*(max_len+2-len(j))+'|', end='')
        print('  '+str(words_exsist_counter[words.index(j)])+' '*21+'|')
    print('-'*(max_len+31))


def get_letter_and_count(sentense):
    global words
    global words_exsist_counter
    words = []
    words_exsist_counter = []
    para = ''

    temp_letter = ''

    for l in sentense:
        if l in '.()!':
            continue
        else:
            para += l.lower()

    for i in para:
        if i == ' ':
            if temp_letter.isalpha():
                if len(words) == 0:
                    words.append(temp_letter)
                    words_exsist_counter.append(1)
                    temp_letter = ''
                else:
                    for j in words:
                        if j == temp_letter:
                            words_exsist_counter[words.index(j)] += 1
                            temp_letter = ''
                            break
                    for k in words:
                        if temp_letter == '':
                            break
                        else:
                            words.append(temp_letter)
                            words_exsist_counter.append(1)
                            temp_letter = ''
            else:
                temp_letter = ''
        else:
            if i == para[-1]:
                temp_letter += i
                words.append(temp_letter)
                words_exsist_counter.append(1)
                temp_letter = ' '
            else:
                temp_letter += i

def main():
    z = 1
    print('1. Input One Line Sentense: ')
    print('2. Input Paragraph')
    print('3. Exit')
    print()

    user = input("Enter No. of option do you want: ")
    if user == '1':
        parag = input("Enter yout sentense: ")
        get_letter_and_count(parag)
        final_out(words, words_exsist_counter)
    elif user == '2':
        ready = input("Please past your paragraph into input.txt file & press Enter [file location: root folder]:\n")
        file = open('input.txt', 'r')
        parag = file.read()
        while z == 1:
            if parag == '':
                error = input('No any characters inside the txt file. Please past your paragraph and press enter:\n')
            else:
                get_letter_and_count(parag)
                final_out(words, words_exsist_counter)
                file.close()
                z = 0
    elif user == '3':
        sys.exit(0)

if __name__ == '__main__':
    main()