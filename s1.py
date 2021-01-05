import sys
def get_max_min_sum(array, n):
    s = set(array)
    ln = len(s)
    sum =0
    if n > ln:
        return -1
    l = list(s)
    array = sorted(l)
    min_n = array[0: n]
    max_n = array[ln - n: ln]
    except_flag = bool(set(min_n) & set(max_n))
    if except_flag:
        return -1

    for item in min_n:
        sum += item
    for item in max_n:
        sum += item
    return sum


if __name__ == "__main__":
    flag = False
    li=[]
    sum =0
    try:
        m = int(sys.stdin.readline().strip())
        arry = str(sys.stdin.readline().strip()).split()
        if len(arry)!=m:
            raise ValueError("")
        for item in arry:
            li.append(int(item))
            if item>1000 or item <0:
                raise ValueError("")
        n= int(sys.stdin.readline().strip())
    except Exception:
        flag =True
    if flag :
        print(-1)
    else:
        sum =get_max_min_sum(li,n)
        print(sum)


