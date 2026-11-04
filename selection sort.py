salary = [25000, 50000, 30000, 70000, 45000, 90000]

n = len(salary)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if salary[j] < salary[min_index]:
            min_index = j

    salary[i], salary[min_index] = salary[min_index], salary[i]

print("Sorted Salaries:", salary)
print("Top Five Highest Salaries:", salary[-5:][::-1])