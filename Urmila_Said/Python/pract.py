# def solve(g, y, r, last):
#     if g == 0 and y == 0 and r == 0:
#         return 1

#     ans = 0

#     if g > 0 and last != 'G':
#         ans += solve(g-1, y, r, 'G')

#     if y > 0 and last != 'Y':
#         ans += solve(g, y-1, r, 'Y')

#     if r > 0 and last != 'R':
#         ans += solve(g, y, r-1, 'R')

#     return ans


# g = int(input("Green: "))
# y = int(input("Yellow: "))
# r = int(input("Red: "))

# print("Output:", solve(g, y, r, ''))

def solve(g, y, r, last):
    if g == 0 and y == 0 and r == 0:
        return 1

    count = 0

    if g > 0 and last != 'G':
        count += solve(g-1, y, r, 'G')

    if y > 0 and last != 'Y':
        count += solve(g, y-1, r, 'Y')

    if r > 0 and last != 'R':
        count += solve(g, y, r-1, 'R')

    return count
