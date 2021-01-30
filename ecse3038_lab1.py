def hello():
    print("ECSE3038 - Engineering IoT Systems")


def validatePassword(key):
    val = True

    # a password must contain at least 8 characters.
    if len(key) < 8:
        val = False

    # a password must consist of alphanumeric characters only.
    if not(key.isalnum()):
        val = False

    # a password must contain at least 2 numbers.
    num_digits = 0
    for i in key:
        if i.isdigit():
            num_digits += 1

    if (num_digits < 2):
        val = False

    if val:
        return val


def sumUpToN(num):
    sum = 0
    if num > 1:
        sum = (num * (num+1))/2
    else:
        sum = -1
    return sum

# Main method


def main():

    # Q1
    hello()

    # Q2
    password = "GreetingsFe11owKids"

    if (validatePassword(password)):
        print("Password is valid")
    else:
        print("Password is invalid!")

    # Q3
    sum_to_N = sumUpToN(200)
    print(sum_to_N)


# Driver Code
if __name__ == '__main__':
    main()
