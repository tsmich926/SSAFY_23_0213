# def ispair(ss):
#     stack = []
#     sp = -1
#     for i in range(len(ss)):
#         sp += 1
#         stack.append(ss[i])
#         if sp > 0:
#             if stack[sp] == stack[sp-1]:
#                 stack.pop(sp)
#                 stack.pop(sp-1)
#     print(stack)
#
#
#
#
#
#
# TC = int(input())
# for tc in range(1,TC+1):
#     ss = input()
#     ispair(ss)



# def ispair(ss):
#     N = len(ss)
#     stack = []
#     sp = -1
#     for i in range(N):
#         if i == 0 :
#             if ss[i] != ss[i+1]:
#                 sp += 1
#                 stack.append(ss[i])
#                 sp += 1
#                 stack.append(ss[i+1])
#         else:
#             idx = ss.index(stack[sp])+1
#             if stack[sp] != ss[idx] :
#                 sp += 1
#                 stack.append(ss[idx])
#             else:
#                 if stack != 0:
#                     stack.pop(sp)
#     return stack
#
#
# TC = int(input())
# for tc in range(1,TC+1):
#     ss = input()
#     print(ispair(ss))
#
#
#
# def ispair(ss):
#     N = len(ss)
#     tp = N - 1
#     stack = []
#     sp = -1
#     for s in ss:
#         stack.append(s)
#     for k in range(tp,0,-1):
#         if stack[k] == stack[k-1]:
#             del stack[k]
#             del stack[k-1]


#제출
T = int(input())
for tc in range(1, T+1):
    ss = input()
    stack=[]
    for s in ss:
        if len(stack) == 0:
            stack.append(s)
        else:
            if len(stack)>0:
                stack.pop()
            else:
                stack.append(s)

    lenth = len(stack)
    print(f'#{tc} {lenth}')