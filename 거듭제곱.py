
#######고치기
def gegop(N,M):
    if M == 0:
        return 1
    else:
        N * gegop(N, M - 1)

for tc in range(1,2):
    n = int(input())
    N,M = map(int,input().split())
    ans = gegop(N,M)
    print('f{tc} {ans}')