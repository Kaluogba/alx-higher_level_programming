def uppercase(s):
    for char in s:
        offset = 32 if 'a' <= char <= 'z' else 0
        print("{:c}".format(ord(char) - offset), end="")
    print()
