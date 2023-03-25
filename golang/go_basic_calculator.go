package main

import (
	"fmt"
)

// Define function for addition operation
func add(x, y float64) float64 {
	return x + y
}

// Define function for subtraction operation
func subtract(x, y float64) float64 {
	return x - y
}

// Define function for multiplication operation
func multiply(x, y float64) float64 {
	return x * y
}

// Define function for division operation
func divide(x, y float64) float64 {
	return x / y
}

func main() {
	for {
		// Get the user's choice of operation
		fmt.Println("Please select an operation:")
		fmt.Println("1. Add")
		fmt.Println("2. Subtract")
		fmt.Println("3. Multiply")
		fmt.Println("4. Divide")

		var choice int
		for {
			_, err := fmt.Scanln(&choice)
			if err != nil || choice < 1 || choice > 4 {
				fmt.Println("Error: Invalid input. Please enter a valid choice (1-4).")
				continue
			}
			break
		}

		// Get the user's input for operands
		var num1, num2 float64
		for {
			fmt.Println("Enter first number:")
			_, err := fmt.Scanln(&num1)
			if err != nil {
				fmt.Println("Error: Invalid input. Please enter a number.")
				continue
			}
			break
		}

		for {
			fmt.Println("Enter second number:")
			_, err := fmt.Scanln(&num2)
			if err != nil {
				fmt.Println("Error: Invalid input. Please enter a number.")
				continue
			}
			break
		}

		// Perform the chosen operation and display the result
		switch choice {
		case 1:
			fmt.Printf("%v + %v = %v\n", num1, num2, add(num1, num2))
		case 2:
			fmt.Printf("%v - %v = %v\n", num1, num2, subtract(num1, num2))
		case 3:
			fmt.Printf("%v * %v = %v\n", num1, num2, multiply(num1, num2))
		default:
			fmt.Printf("%v / %v = %v\n", num1, num2, divide(num1, num2))
		}

		// Ask if user wants to perform another operation
		var response string
		for {
			fmt.Println("Do you want to perform another operation? (y/n)")
			_, err := fmt.Scanln(&response)
			if err != nil || (response != "y" && response != "n") {
				fmt.Println("Error: Invalid input. Please enter 'y' or 'n'.")
				continue
			}
			break
		}

		if response == "n" {
			break
		}
	}
}

