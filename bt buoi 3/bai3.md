def dao_nguoc_chuoi(s):
   
    return s[::-1]

def dao_nguoc_doan_chuoi(s, a, b):

    return s[:a] + s[a:b][::-1] + s[b:]

def xoa_ki_tu_chan(s):

    return s[::2]

def doi_cho_ky_tu_dau(s1, s2):

    return s2[0] + s1[1:], s1[0] + s2[1:]

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    print(dao_nguoc_chuoi(s1))

    a, b = map(int,input().split())

    print( dao_nguoc_doan_chuoi(s2, a, b))

    print(xoa_ki_tu_chan(s1))

    s1, s2 = doi_cho_ky_tu_dau(s1, s2)

    print(s1, s2)
