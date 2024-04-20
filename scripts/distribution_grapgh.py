import matplotlib.pyplot as plt
import numpy as np

# Token allocation percentages
allocations = {
    "Koios Nodes Rewards": 20,
    "Koios Contributors": 10,
    "Provide to Subscribe Campaign": 30,
    "Treasury": 30,
    "Community Initiatives and Partnerships": 5,
    "Marketing and Future Development": 5
}

# Total number of tokens
total_tokens = 10_000_000

# Calculate the number of tokens for each stakeholder
tokens_per_stakeholder = {k: v * total_tokens / 100 for k, v in allocations.items()}

# Create a pie chart for token distribution
plt.figure(figsize=(10, 6))
plt.pie(tokens_per_stakeholder.values(), labels=tokens_per_stakeholder.keys(), autopct='%1.1f%%', startangle=140, colors=plt.cm.Greens_r(np.linspace(0.3, 0.7, len(tokens_per_stakeholder))))
plt.title('Koios Token Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
