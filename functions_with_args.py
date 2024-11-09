def longest_word(*args):
    print(args)
    print(type(args))
    leader = ""
    for word in args:
        if type(word) is str:
            if len(word) > len(leader):
                leader = word
    return leader

print(longest_word("Python", "Java", 3, [], "Programming"))

print()

def longest_list(*args):
    print(args)
    leader = []
    for list_ in args:
        if len(list_) > len(leader):
            leader = list_
    return leader

print(longest_list([1, 2], ['a', 'b', 'c'], [3]))

print()

def remove_from_string(string, *args):
    for symbol in args:
        string = string.replace(symbol, '')
    return string

print(remove_from_string("Смотри! Мы, можем удалить: все знаки препинания сразу. Или нет?", "?", ".", ",", "!", ":"))
