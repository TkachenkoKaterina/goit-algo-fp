items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    items_list = [(
        name, data["cost"], data["calories"], data["calories"] / data["cost"]
        ) for name, data in items.items()]

    items_list.sort(key=lambda x: x[3], reverse=True)

    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item in items_list:
        name, cost, calories, ratio = item
        if total_cost + cost <= budget:
            chosen_items.append(name)
            total_cost += cost
            total_calories += calories

    return chosen_items, total_calories


def dynamic_programming(items, budget):
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    item_names = list(items.keys())

    for i in range(1, len(items) + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    chosen_items = []
    b = budget
    for i in range(len(items), 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            chosen_items.append(item_names[i - 1])
            b -= items[item_names[i - 1]]["cost"]

    total_calories = dp[len(items)][budget]
    return chosen_items, total_calories


if __name__ == "__main__":
    budget = 100

    print("Жадібний алгоритм:")
    greedy_items, greedy_calories = greedy_algorithm(items, budget)
    print(f"Вибрані страви: {greedy_items}")
    print(f"Загальна калорійність: {greedy_calories}\n")

    print("Динамічне програмування:")
    dp_items, dp_calories = dynamic_programming(items, budget)
    print(f"Вибрані страви: {dp_items}")
    print(f"Загальна калорійність: {dp_calories}")
