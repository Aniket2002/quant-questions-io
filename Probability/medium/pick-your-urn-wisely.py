# question : You have indistinguishable urns in front of you. The first urn has 4
# ($1 chips) and 6 ($10 chips), while the second urn has 3 ($1 chips) and 7 ($10 chips).
# You reach into one urn at random and select a ($1 chip). Then you have the opportunity 
# to pick another chip at random either from the same urn you picked the first chip from 
# or at random from the other urn. Your payout is the value of the second chip you select. 
# Under optimal gameplay, what is your expected payout?

# Define the probabilities and expected values for each urn
urn1 = {'$1': 4, '$10': 6}
urn2 = {'$1': 3, '$10': 7}

# Calculate the probabilities of drawing each chip from each urn
def calculate_probabilities(urn):
    total_chips = sum(urn.values())
    return {chip: count / total_chips for chip, count in urn.items()}

urn1_probs = calculate_probabilities(urn1)
urn2_probs = calculate_probabilities(urn2)

# Calculate the expected value of the second draw given the first draw is $1
def expected_value_same_urn(urn_probs):
    return sum(int(chip[1:]) * prob for chip, prob in urn_probs.items())

# Optimal strategy: switch urns if the second urn has a higher expected value
expected_urn1 = expected_value_same_urn(urn1_probs)
expected_urn2 = expected_value_same_urn(urn2_probs)

# Since the first draw is $1, we know which urn it came from
# Calculate the overall expected payout under optimal gameplay
optimal_expected_payout = 0.5 * max(expected_urn1, expected_urn2) + 0.5 * max(expected_urn2, expected_urn1)

print(f"Under optimal gameplay, the expected payout is: ${optimal_expected_payout:.2f}")


