# import codecademylib3
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms

# Display two plots at once
plt.figure(1)
plt.subplot(211)

# Create the flights histogram
plt.hist(
  flights,
  range = (0, 365),
  bins = 365,
  edgecolor = 'black'
)

# Add x-label to the histogram
plt.xlabel('Day of the Year')

# Add y-label to the histogram
plt.ylabel('Flight Count')

# Add title to the histogram
plt.title('Flight by Day')

# A grid of subplot
plt.subplot(212)

# Create the in_bloom histogram
plt.hist(
  in_bloom,
  range = (0, 365),
  bins = 365
)

# Add x-label to the histogram
plt.xlabel('Day of the Year')

# Add y-label to the histogram
plt.ylabel('Bloom Count')

# Add title to the histogram
plt.title('Flower Blooms and Flights by Day')

# Prevent labels from overlapping
plt.tight_layout()

# Display the histogram
plt.show()