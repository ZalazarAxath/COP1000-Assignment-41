"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 35.00
# Number of characters.
numChars = int(input("Enter the number of characters: "))
# Color of characters.
color = input("Enter the color of characters (black/white/gold): ").lower()
# Type of wood.
woodType = input("Enter the wood type (oak/pine): ").lower()

# Write assignment and if statements here as appropriate.

# Calculate charge based on number of characters.
if numChars > 5:
    charge += 4 * (numChars - 5)

# Additional charge for gold color.
if color == "gold":
    charge += 15.00

# Additional charge for oak wood type.
if woodType == "oak":
    charge += 20.00

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
