package main

import (
	"fmt"
	"strings"
)

// Morse code dictionary
var morseCodeMap = map[string]string{
	"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
	"G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
	"M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
	"S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
	"Y": "-.--", "Z": "--..",
	"1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
	"6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
	" ": " ", // Space
}

func textToMorse(text string) string {
	text = strings.ToUpper(text)
	var result string

	for _, char := range text {
		if morseChar, ok := morseCodeMap[string(char)]; ok {
			result += morseChar + " "
		} else {
			result += " " // Add space for characters not in the dictionary
		}
	}

	return result
}

func morseToText(morse string) string {
	var result string
	morseArray := strings.Fields(morse) // Split Morse code by spaces

	for _, code := range morseArray {
		for key, value := range morseCodeMap {
			if code == value {
				result += key
				break
			}
		}
	}

	return result
}

func main() {
	fmt.Println("1. Text to Morse")
	fmt.Println("2. Morse to Text")
	fmt.Print("Enter your choice (1/2): ")
	var choice int
	fmt.Scanln(&choice)

	switch choice {
	case 1:
		fmt.Print("Enter text to convert to Morse code: ")
		var text string
		fmt.Scanln(&text)
		morse := textToMorse(text)
		fmt.Println("Morse Code:", morse)
	case 2:
		fmt.Print("Enter Morse code to convert to text (separate letters/numbers with spaces): ")
		var morse string
		fmt.Scanln(&morse)
		text := morseToText(morse)
		fmt.Println("Text:", text)
	default:
		fmt.Println("Invalid choice.")
	}
}