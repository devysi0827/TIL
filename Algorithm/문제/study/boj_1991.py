# 전위순회
# 루트, 왼, 오
def pre_order(root):
    global tree, pre

    pre += root

    # 왼쪽 자식이 있으면?
    if tree[root][0] != '.':
        pre_order(tree[root][0])

    # 오른쪽 자식이 있으면
    if tree[root][1] != '.':
        pre_order(tree[root][1])

    return


# 중위순회
# 왼, 루트, 오
def mid_order(root):
    global tree, mid

    if tree[root][0] != '.':
        mid_order(tree[root][0])

    mid += root

    if tree[root][1] != '.':
        mid_order(tree[root][1])

    return


# 후위순회
# 왼, 오, 루트
def post_order(root):
    global tree, post

    if tree[root][0] != '.':
        post_order(tree[root][0])

    if tree[root][1] != '.':
        post_order(tree[root][1])

    post += root

    return


N = int(input())

tree = dict()
for _ in range(N):
    key, left, right = input().split()
    tree[key] = [left, right]

pre, mid, post = '', '', ''

pre_order('A')
mid_order('A')
post_order('A')


print(pre)
print(mid)
print(post)