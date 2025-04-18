# Question: You roll a fair 6-sided die twice. Calculate the probability that the value of the first roll is strictly less than the value of the second roll.

dice = [1, 2, 3, 4, 5, 6]
total_outcomes = 0
favorable_outcomes = 0
for i in dice:
    for j in dice:
        total_outcomes += 1
        if i < j:
            favorable_outcomes += 1
            
probability = favorable_outcomes / total_outcomes
print(f"Probability that the first roll is strictly less than the second roll: {probability:.2f}")
# The probability that the first roll is strictly less than the second roll is 0.5.
# The total number of outcomes is 6 * 6 = 36, and the number of favorable outcomes is 15.
# Therefore, the probability is 15/36 = 0.4166666666666667.
# This can be simplified to 5/12, which is approximately 0.4167.
# The probability is approximately 0.4167 or 41.67%.