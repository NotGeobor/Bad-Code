class user:

    def __init__(self, username, password, key):
        self.username = username
        self.password = password


def encoder(var, key):
    letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    num_ls = []
    num_ls1 = []
    num1 = 0

    for el in str(key):
        num = el
        num1 += int(num)
    num1 = (num1 + (len(str(key)) - 1))

    for ch in var:
        ch = letters.index(ch)
        num_ls.append(ch)

    for el in num_ls:
        element = el
        num_ls1.append(str(int(element) + num1))

    return "".join(num_ls1[::-1])
