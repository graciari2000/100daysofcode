package main

import (
	"fmt"
	"math"
)

func main() {
	// Prompt the user for height and weight
	var height, weight float64

	fmt.Print("Enter your height (in meters): ")
	_, err := fmt.Scan(&height)
	if err != nil {
		fmt.Println("Invalid input for height. Please enter a valid number.")
		return
	}

	fmt.Print("Enter your weight (in kilograms): ")
	_, err = fmt.Scan(&weight)
	if err != nil {
		fmt.Println("Invalid input for weight. Please enter a valid number.")
		return
	}

	// Calculate BMI
	bmi := calculateBMI(height, weight)

	// Display BMI and interpretation
	fmt.Printf("Your BMI is: %.2f\n", bmi)
	interpretation := interpretBMI(bmi)
	fmt.Println(interpretation)
}

func calculateBMI(height, weight float64) float64 {
	return weight / (height * height)
}

func interpretBMI(bmi float64) string {
	if bmi < 18.5 {
		return "You are underweight."
	} else if bmi >= 18.5 && bmi < 24.9 {
		return "You have a normal weight."
	} else if bmi >= 24.9 && bmi < 29.9 {
		return "You are overweight."
	} else {
		return "You are obese."
	}
}