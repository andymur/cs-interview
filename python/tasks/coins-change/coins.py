#!/usr/bin/python3

amount = 500
coins = [5, 20, 50]
answer = {5: 0, 20: 0, 50: 0}

def make_change_variants(answer, amount, coins):
	print("amount: {0}, coin: {1}, coins: {2}".format(amount, coins[:1][0] if len(coins) else [], coins))

	if not len(coins):
		return 0

	if amount < 0:
		return 0

	if amount == 0:
		print("ANSWER: {0}, number of coins: {1}".format(answer, sum(answer.values())))
		return 1

	coin = coins[:1][0]

	a1 = dict(answer)
	a2 = dict(answer)
	a1[coin] += 1

	return make_change_variants(a1, amount - coin, coins) + make_change_variants(a2, amount, coins[1:])

if __name__=="__main__":
	result = make_change_variants(answer, amount, coins)

	print("result: {0}, answer: {1}".format(result, answer))