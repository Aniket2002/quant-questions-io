# Question: On average, how many cards in a normal deck of 52 playing cards do you need to flip over to observe your first ace.

# Calculate the expected number of cards to flip over to observe the first ace
total_non_ace_cards = 48  # Total non-ace cards in the deck
num_sections = 5  # Sections created by the 4 aces

# Expected number of cards in the first section
expected_cards_in_first_section = total_non_ace_cards / num_sections

# Add 1 for the first ace
expected_cards_to_first_ace = expected_cards_in_first_section + 1
expected_cards_to_first_ace = round(expected_cards_to_first_ace, 2)  # Round to 2 decimal places

print(f"On average, you need to flip over {expected_cards_to_first_ace} cards to observe your first ace.")