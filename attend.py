def repeat(xs, n):
    ans = []
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return ans
    for i in xs:
        for _ in range(n):
            ans.append(i)
    return ans


print(repeat(['a', 'b'], -1))
