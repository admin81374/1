def is_magic(g):
    lines = [
        g[0:3], g[3:6], g[6:9],
        g[0::3], g[1::3], g[2::3],
        g[0::4], g[2:7:2]
    ]

    for line in lines:
        if sum(line) != 15:
            return False
    return True


def print_sol(g):
    for i in range(0, 9, 3):
        print(g[i:i+3])
    print()


def solve(no_repeat=False, limit=20):
    count = 0
    grid = [0] * 9
    used = set()

    def backtrack(pos):
        nonlocal count

        if pos == 9:
            if is_magic(grid):
                count += 1
                print("Solution", count)
                print_sol(grid)
            return

        for num in range(1, 10):
            if no_repeat and num in used:
                continue

            grid[pos] = num
            used.add(num)
            backtrack(pos + 1)
            used.discard(num)

            if count >= limit:
                return

    backtrack(0)
    return count


print("Magic Square 3x3 | Sum = 15")
print("1. Repetition allowed")
print("2. No repetition allowed")

ch = input("Enter choice (1/2): ")

if ch == "1":
    n = int(input("Enter number of solutions: "))
    solve(limit=n)
elif ch == "2":
    n = int(input("Enter number of solutions: "))
    solve(no_repeat=True, limit=n)
else:
    print("Invalid choice")
