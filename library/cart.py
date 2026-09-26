def total_price(prices):
    total = 0
    for i in range(1, len(prices)):
        total += prices[i]
    return total


def average_rating(ratings):
    return sum(ratings) / len(ratings)
