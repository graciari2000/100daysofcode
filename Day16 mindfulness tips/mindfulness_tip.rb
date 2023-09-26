# List of mindfulness tips
mindfulness_tips = [
    "Take a few deep breaths to center yourself.",
    "Practice gratitude for the little things in life.",
    "Pay full attention to the taste and texture of your food.",
    "Spend a few minutes meditating or focusing on your breath.",
    "Disconnect from electronic devices for a while.",
    "Notice the beauty in nature around you.",
    "Express kindness to someone, even in a small way.",
    "Take a mindful walk and notice your surroundings.",
    "Listen actively when someone is talking to you.",
    "Pause and appreciate a moment of silence."
]

# Function to select a random mindfulness tip
def select_random_tip(tips)
    tips.sample
end

# Display a daily mindfulness tip
def display_daily_tip(tips)
    puts "Today's Mindfulness Tip:"
    puts select_random_tip(tips)
end

# Main program
display_daily_tip(mindfulness_tips)
