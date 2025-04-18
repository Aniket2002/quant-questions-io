# Question: You have a pile of 100 coins. 1 of the coins is an unfair coin and has heads on both sides. The remaining 99 coins are fair coins. You randomly select a coin from the pile and flip it 10 times. The coin lands heads all 10 times. Calculate the probability that the coin you selected is the unfair coin.

unfair = 0.01  # Probability of selecting the unfair coin
fair = 0.99  # Probability of selecting a fair coin

prob_unfair_given_heads = 1  # Probability of getting heads 10 times with the unfair coin
prob_fair_given_heads = (0.5 ** 10)  # Probability of getting heads 10 times with a fair coin
prob_heads = (unfair * prob_unfair_given_heads) + (fair * prob_fair_given_heads)  # Total probability of getting heads 10 times
prob_unfair_coin = (unfair * prob_unfair_given_heads) / prob_heads  # Probability of selecting the unfair coin given heads 10 times

prob_unfair_coin = round(prob_unfair_coin, 4)  # Round to 4 decimal places
print(f"Probability that the selected coin is the unfair coin: {prob_unfair_coin:.4f}")
# The probability that the selected coin is the unfair coin is 0.9118.
# The total probability of getting heads 10 times is calculated using the law of total probability.
# The probability of selecting the unfair coin given heads 10 times is calculated using Bayes' theorem.
