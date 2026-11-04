salary = [25000, 50000, 30000, 70000, 45000, 90000]

n = len(salary)

for i in range(n):
    for j in range(n - i - 1):

        if salary[j] > salary[j + 1]:
            salary[j], salary[j + 1] = salary[j + 1], salary[j]

print("Sorted Salaries:", salary)
print("Top Five Highest Salaries:", salary[-5:][::-1])