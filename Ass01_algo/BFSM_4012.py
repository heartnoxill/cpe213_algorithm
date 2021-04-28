def BFSM(string, pattern):
    for cnt_i in range(len(string)-len(pattern)):
        cnt_j = 0
        while cnt_j < len(pattern) and pattern[cnt_j] == string[cnt_i+cnt_j]:
            cnt_j = cnt_j + 1
        if cnt_j == len(pattern):
            print(cnt_i)
    return -1

BFSM("HelloWorld", "r")
BFSM("Lorem Ipsum", "Ip")
BFSM("    ilovealgo", "love")


