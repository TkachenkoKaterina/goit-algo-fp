import random
import matplotlib.pyplot as plt


def monte_carlo_simulation(num_rolls):
    outcomes = [0] * 13

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        outcomes[total] += 1

    probabilities = [outcome / num_rolls for outcome in outcomes]
    return probabilities


num_rolls = 1000000

probabilities = monte_carlo_simulation(num_rolls)

analytical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

sums = list(range(2, 13))
monte_carlo_values = probabilities[2:13]
analytical_values = [analytical_probabilities[s] for s in sums]

plt.figure(figsize=(10, 6))
plt.plot(sums, monte_carlo_values, label='Monte Carlo', marker='o')
plt.plot(sums, analytical_values, label='Analytical', marker='x')
plt.title('Ймовірності сум при киданні двох кубиків')
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.xticks(sums)
plt.legend()
plt.grid(True)
plt.show()
