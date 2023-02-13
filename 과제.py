
def ispair(ss):
    stack = []
    for s in ss:
        if s == '(':
            stack.append(s)
        elif s == '{' :
            stack.append(s)
        elif s == ')':
            if len(stack) == 0:
                return 0
            else:
                p1 =stack.pop(-1)
                if p1 != '(':
                    return 0
        elif s == '}':
            if len(stack) == 0:
                return 0
            else:
                p2 = stack.pop(-1)
                if p2 != '{':
                    return 0
    if stack :
        return 0
    return 1



TC = int(input())
for tc in range(1,TC+1):
    ss = input()
    ans = ispair(ss)
    print(f'#{tc} {ans}')





#딕셔너리 이용해서 하기
def ispair(ss):
    match = {'(':')','{':'}'}
    for i in (ss):
        if i == '(':
-----------------------------
def ispair(ss):
    for i in (ss):
        if i