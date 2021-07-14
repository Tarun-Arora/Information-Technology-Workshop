class s_zero:
 def __init__(self, s):
    self.data = v
 def zero_triplets(self):
    arr = self.data.copy()
    arr.sort()
    out = []
    while len(arr) >= 3:
        val = arr.pop()
        x = 0
        y = len(arr) - 1
        while x < y:
            if arr[x] + arr[y] + val == 0:
                a = [arr[x], arr[y], val]
                out.append(a)
                arr.pop(y)
                arr.pop(x)
                break
            elif arr[x] + arr[y] + val > 0:
                y -= 1
            elif arr[x] + arr[y] + val < 0:
                x += 1
    return out
v = [-25, -10, -7, -3, 2, 4, 8, 10]
q = s_zero(v)
print('The suitable triplets found are:',q.zero_triplets())