def validate(card):
    true = 1
    false = 0
    if (int(card[0])<4) or (int(card[0])>6) or ((len(card)!=16) and (len(card)!=19)):
        return false
    else:
        for j in range(len(card)):
            i = card[j]
            l = ['0','1','2','3','4','5','6','7','8','9','-']
            if i not in l:
                return false
            if i in card[j-3:j]:
                if (i==card[j-3]) and (i==card[j-2]) and (i==card[j-1]):
                    return false
            if i == '-':
                if (j!=4) and (j!=9) and (j!=14):
                    return false
        if '-' in card:
            if (card[4]!='-') or (card[9]!='-') or (card[14]!='-'):
                return false
            tmp = []
            for k in card:
                if k!='-':
                    tmp.append(k)
            for j in range(len(tmp)):
                i = card[j]
                if i in tmp[j-3:j]:
                    if (i==tmp[j-3]) and (i==tmp[j-2]) and (i==tmp[j-1]):
                        return false
    return true   

if __name__ == '__main__':
    for i in range(int(input())):
        card = input().strip()
        if validate(card):
            print("Valid")
        else:
            print("Invalid")
