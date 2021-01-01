
money = [1, 5, 10, 20, 50, 100, 200, 500, 1_000]
amount = 1_475_879

# take the largest number that's less than or equal to amount
# take the floor div of amount to largest number that's less than it (that's how many of these are needed)
# take the mod of amount to largest number that's less than it (that is what's left)
# take the largest amount that's less than or equal to remainder
# take floor div and mod until 0

denominations = []
to_use = None
coins_copy = money.copy()

while amount > 0:
    while coins_copy:
        if max(coins_copy) <= amount:
            to_use = max(coins_copy)
            coins_copy.remove(to_use)
            break
        coins_copy.remove(max(coins_copy))
    else:
        raise Exception
    denominations.append((to_use, amount//to_use))
    amount = amount % to_use

print(denominations, f'\tHow many pieces: {sum(x[1] for x in denominations)}')





