tree = ['-', ['*', 13, ['+', ['/', 32, -4], 12]], ['*', ['+', ['-', 10, 1], 3], 4]]

def evaluate_tree(t):
    if isinstance(t, int):   # Check if it's an integer so it can return the answer.
        return t
    elif t[0]=="-":
        return evaluate_tree(t[1]) - evaluate_tree(t[2])
    elif t[0] == "+":
        return evaluate_tree(t[1]) + evaluate_tree(t[2])
    elif t[0] == "*":
        return evaluate_tree(t[1]) * evaluate_tree(t[2])
    elif t[0] == "/":
        return evaluate_tree(t[1]) // evaluate_tree(t[2])

result = evaluate_tree(tree)

print(result)
