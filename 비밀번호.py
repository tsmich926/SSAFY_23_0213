import sys
sys.stdin = open('i.txt', 'r')

# for tc in range(1,3):
#     N, S = input().split()
#     stack = []
#     sp = -1
#     for i in range(len(S)):
#         if len(stack) == 0:
#             sp += 1
#             stack.append(S[i])
#         else:
#             if stack[sp] == S[i]:
#                 sp -= 1
#                 stack.pop(sp)
#             else:
#                 sp += 1
#                 stack.append(S[i])
#     print(f'{tc} {stack}')




# for tc in range(1,2):
#     N, S = input().split()
#     stack = []
#     for i in range(len(S)):
#         if len(stack) == 0:
#             stack.append(S[i])
#         else:
#             if stack[-1] == S[i]:
#                 stack.pop()
#             else:
#                 stack.append(S[i])
#     print(f'{tc} {stack}')

#
for tc in range(1, 11):
    N, S = input().split()
    stack=[]
    for s in S:
        if len(stack) == 0:
            stack.append(s)
        else:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
    print(f"#{tc} ", end="")
    for s in stack:
        print(s, end="")
    print()

    # for tc in range(1, 11):
    #     lenS, S = input().split()
    #
    #     stack = []
    #     for s in S:
    #         if not stack or stack[-1] != s:
    #             stack.append(s)
    #         else:
    #             stack.pop(-1)
    #
    #     print(f"#{tc} ", end="")
    #     for s in stack:
    #         print(s, end="")
    #     print()