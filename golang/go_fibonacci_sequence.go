package main

import (
	"fmt"
)

func fibonacciSequence(n int) []int {
	fib := []int{0, 1}
	for len(fib) < n {
		fib = append(fib, fib[len(fib)-1]+fib[len(fib)-2])
	}
	return fib
}

func main() {
	for {
		var n int
		fmt.Print("Enter the number of Fibonacci numbers to generate: ")
		_, err := fmt.Scan(&n)
		if err != nil {
			fmt.Println("Invalid input:", err)
			continue
		}
		if n < 1 {
			fmt.Println("Input must be positive.")
			continue
		}
		if n > 1000000 {
			fmt.Println("Input must be less than or equal to 1000000.")
			continue
		}
		fibonacciNumbers := fibonacciSequence(n)
		fmt.Printf("The first %d Fibonacci numbers are: %v\n", n, fibonacciNumbers)
		var response string
		fmt.Print("Do you want to generate another set of Fibonacci numbers? (y/n) ")
		_, err = fmt.Scan(&response)
		if err != nil {
			fmt.Println("Invalid input:", err)
			continue
		}
		if response != "y" {
			break
		}
	}
}

