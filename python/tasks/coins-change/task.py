#!/usr/bin/python3

# You are working at the cash counter at a fun-fair, and you have different types of coins available to you in infinite quantities. 
# The value of each coin is already given. Can you determine the number of ways of making change for a particular number of units using the given types of coins?

#For example, if you have 4 types of coins, and the value of each type is given as 8,3,1,2 respectively, 
# you can make change for 3 units in three ways: {1,1,1}, {1,2} and {3}


#Function Description
#
#getWays has the following parameter(s):

#    n: an integer, the amount to make change for
#    c: an array of integers representing available denominations


amount = 500
coins = [5, 20, 50]
answer = {5: 0, 20: 0, 50: 0}

calculated_result = {}
calculated = {}

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

# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
def getWays(amount, coins):
	if not len(coins):
		return 0

	if amount < 0:
		return 0

	if amount == 0:
		return 1

	coin = coins[:1][0]

	if calculated.get(coin) == None:
		calculated_result[coin] = {}
		calculated[coin] = {}

	if calculated[coin].get(amount) == None:
		calculated[coin][amount] = True
		calculated_result[coin][amount] = getWays(amount - coin, coins) +getWays(amount, coins[1:])

	return calculated_result[coin][amount]

if __name__=="__main__":
	result = make_change_variants(answer, amount, coins)

	print("result: {0}, answer: {1}".format(result, answer))