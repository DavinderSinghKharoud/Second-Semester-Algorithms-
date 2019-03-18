class Tree:
    def __init__(tree, value):
        tree.value = value
        tree.children = []

    def __repr__(tree):
        return tree.value


root = Tree("Olivier")
mom = Tree("Mom")
dad = Tree("Dad")
grandma = Tree("Grandma")

root.children.append(mom)
root.children.append(dad)
mom.children.append(grandma)


# print(root.value)
# print(root.children)
# print(root.children[0].children)

def depthFirstTraversal(root):
    print(root.value)
    for child in root.children:
        depthFirstTraversal(child)


def size(root):
    if not root.children:
        return 1
    else:
        count = 1
        for child in root.children:
            value = size(child)
            count=count+value
        return count

def size1(root):
	total=1
	for child in root.children:
		total=total+size1(child)
	return total

print(size1(root))
print(size(root))

depthFirstTraversal(root)
# Olivier
# Mom
# Grandma
# Dad
