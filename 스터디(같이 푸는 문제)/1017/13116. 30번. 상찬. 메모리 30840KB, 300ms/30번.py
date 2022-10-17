import sys
sys.stdin = open('input.txt')

def find_par(n):
    li = []
    while n:
        li.append(n)
        n = par[n]
    return li

T = int(input())
par = [0] * 1024
for i in range(len(par)):
    par[i] = i // 2                         # 자식 노드를 2로 나눈 몫이 곧 부모 노드가 된다.
for test in range(T):
    A, B = map(int, input().split())
    A_par = set(find_par(A))                # 각각의 조상노드를 다 찾고 교집합을 통해서 결과를 도출
    B_par = set(find_par(B))
    print(max(A_par & B_par) * 10)
