from test import wikipedia_test

if __name__ == '__main__':
    number_list = [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9]
    for i_num in number_list:
        print(wikipedia_test(i_num)[0], '\n')


