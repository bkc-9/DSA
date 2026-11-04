from collections import Counter
members = []
borrows = []
n = int(input("Enter number of members: "))
for i in range(n):
    name = input("Enter member name: ")
    count = int(input("Enter books borrowed: "))
    members.append(name)
    borrows.append(count)

if n > 0:
    print("Average:", sum(borrows)/n)
    print("Highest:", members[borrows.index(max(borrows))])
    print("Lowest:", members[borrows.index(min(borrows))])
    print("Memebers with zero borrowing: ", borrows.count(0))
    c = Counter(borrows)
    mode = c.most_common(1)[0][0]
    print("Most found: ", mode)
else:
    print("No members available")