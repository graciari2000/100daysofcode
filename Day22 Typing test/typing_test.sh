sample_texts=("The lazy brown fox jumps over the whatevs."
"The quick red dog barks at the whatnot."
"The slow yellow cat meows at the woof."
)

# Function to select a random text
select_random_text() {
    local num_texts=${#sample_texts[@]}
    local random_index=$((RANDOM % num_texts))
    echo "${sample_texts[random_index]}"
}

# Function to calculate words per minute (WPM)
calculate_wpm() {
    local start_time=$1
    local end_time=$2
    local typed_text="$3"

    local elapsed_time=$((end_time - start_time))
    local num_words=$(echo "$typed_text" | wc -w)
    local wpm=$((num_words * 60 / elapsed_time))
    echo "$wpm"
}

# Main function
main() {
    clear
    echo "Welcome to the Typing Test!"
    echo "Press Enter to start..."
    read -r

    local text_to_type="$(select_random_text)"
    echo "Type the following text:"
    echo "$text_to_type"
    
    local start_time=$(date +%s)
    read -r typed_text
    local end_time=$(date +%s)

    local wpm=$(calculate_wpm "$start_time" "$end_time" "$typed_text")

    echo "Your typing speed: $wpm WPM"
}

main
