#  The Product Rule!
t_shirts = 3
hats = 2
count = 0

for s in range(t_shirts):
    for h in range(hats):
        count += 1
        print(f"Combination {count}: Shirt {s+1} + Hat {h+1}")

print(f"\nFinal Count: {count}")