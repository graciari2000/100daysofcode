#!/bin/bash

# Define the file containing health tips
TIPS_FILE="./health_tips.txt"

# Get the current date
CURRENT_DATE=$(date "+%Y-%m-%d")

# Calculate a random seed based on the current date
RANDOM_SEED=$(date -d "$CURRENT_DATE" +%j)

# Use the random seed to get a random line number from the tips file
# Use modulo to ensure the line number is within the file's line count
NUM_TIPS=$(wc -l < "$TIPS_FILE")
RANDOM_LINE=$((RANDOM_SEED % NUM_TIPS + 1))

# Get the health tip for the day
HEALTH_TIP=$(sed -n "${RANDOM_LINE}p" "$TIPS_FILE")

# Display the health tip
echo "Daily Health Tip for $CURRENT_DATE:"
echo "$HEALTH_TIP"