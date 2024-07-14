N, K = map(int, input().split())
S = input()
# A_list = list(map(int, input().split()))

MOD = 998244353
mp = {'C'*(K-1):1}

for i, s in enumerate(S):
    # dictの結合は | でできる
    tmp = ({key+'A':val for key, val in mp.items()} if s != 'B' else {}) | ({key+'B':val for key, val in mp.items()} if s != 'A' else {})
    # print('loop', i, ': tmp', tmp)
    mp = {}

    for key, val in tmp.items():
        if key != key[::-1]:
            if key[1:] in mp:
                mp[key[1:]] += val
            else:
                mp[key[1:]] = val

print(sum([val for val in mp.values()]) % MOD)