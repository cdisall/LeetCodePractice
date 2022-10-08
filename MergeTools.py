def merge_the_tools(string, k):
    for i in range(int(len(string)/k)):
        sub = string[i*k:(i+1)*k]
        out = ""
        for j in range(len(sub)):
            if sub[j] not in out:
                out += sub[j]
        print(out)
