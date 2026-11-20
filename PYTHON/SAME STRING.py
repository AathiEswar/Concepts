def stringconv(tword):
        lst1 = tword.split()
        if lst1[0][0] == lst1[1][0]:
            return True
        else:
            return False



word = input("Enter two words:")


result = stringconv(word)

print(result)