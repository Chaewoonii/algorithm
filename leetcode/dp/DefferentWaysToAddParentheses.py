def diffWaysToCompute(expression: str):
    result = []
    if len(expression) == 0: return []
    elif 0 < len(expression) <= 2: return [int(expression)]

    for i, curr in enumerate(expression):
        if curr.isdigit(): continue

        left_results = diffWaysToCompute(expression[:i])
        right_results = diffWaysToCompute(expression[i+1:])

        for l in left_results:
            for r in right_results:
                result.append(eval(f"{l}{curr}{r}"))

    return result

print(diffWaysToCompute("2-1-1"))
print(diffWaysToCompute("2*3-4*5"))
