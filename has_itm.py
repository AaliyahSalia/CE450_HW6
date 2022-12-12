def has_itm(t, e):
    if label(t) == e:
        return True
    for b in branches(t):
        if has_itm(b, e):
            return True
    return False

def tree(label, branches=[]):
    return [label, branches]
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1]

print(has_itm (tree(11, [tree(12), tree(13, [tree(14),tree(15)])] ),  11))
print(has_itm (tree(11, [tree(12), tree(13, [tree(14),tree(15)])] ),  16))


