class sequence:
    def __init__(self, s):
        self.data = v
    def f_target(self, target):
        arr = self.data.copy()
        arr.sort()
        x = 0
        y = len(arr) - 1
        while x < y:
            if arr[x] + arr[y] == target:
                return f'The indexes for target sum {target} is {(x+1, y+1)}'
            if arr[x] + arr[y] > target:
                y -= 1
            if arr[x] + arr[y] < target:
                x += 1
        return "No pair found."
v = [10, 20, 10, 40, 50, 60, 70]
q = sequence(v)
print(q.f_target(int(input('Enter the target number: '))))