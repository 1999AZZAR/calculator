package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func fibonacciSequence(n int) []int {
	fib := []int{0, 1}
	for len(fib) < n {
		fib = append(fib, fib[len(fib)-1]+fib[len(fib)-2])
	}
	return fib
}

func primeAndFibonacci(n int) ([]int, []int) {
	if n > 10000 {
		return nil, nil
	}

	var primeNumbers []int
	for i := 2; len(primeNumbers) < n; i++ {
		if isPrime(i) {
			primeNumbers = append(primeNumbers, i)
		}
	}

	fibonacciNumbers := fibonacciSequence(n)

	return primeNumbers, fibonacciNumbers
}

func main() {
	for {
		fmt.Println("Please choose an option:")
		fmt.Println("1. Generate a list of prime numbers")
		fmt.Println("2. Generate a list of Fibonacci numbers")
		fmt.Println("3. Generate both lists")

		var choice string
		fmt.Print("Enter 1, 2, or 3: ")
		fmt.Scanln(&choice)

		if choice != "1" && choice != "2" && choice != "3" {
			fmt.Println("Invalid choice. Please enter 1, 2, or 3.")
			continue
		}

		var n int
		fmt.Print("Enter a positive integer: ")
		_, err := fmt.Scanln(&n)
		if err != nil || n < 1 || n > 10000 {
			fmt.Println("Invalid input. Please enter a positive integer less than or equal to 10000.")
			continue
		}

		switch choice {
		case "1":
			primeNumbers := make([]int, 0, n)
			for i := 2; len(primeNumbers) < n; i++ {
				if isPrime(i) {
					primeNumbers = append(primeNumbers, i)
				}
			}
			fmt.Printf("The first %d prime numbers are: %v\n", n, primeNumbers)
		case "2":
			fibonacciNumbers := fibonacciSequence(n)
			fmt.Printf("The first %d Fibonacci numbers are: %v\n", n, fibonacciNumbers)
		case "3":
			primeNumbers, fibonacciNumbers := primeAndFibonacci(n)
			if primeNumbers == nil || fibonacciNumbers == nil {
				fmt.Println("Invalid input. Please enter a positive integer less than or equal to 10000.")
				continue
			}
			fmt.Printf("The first %d prime numbers are: %v\n", n, primeNumbers)
			fmt.Printf("The first %d Fibonacci numbers are: %v\n", n, fibonacciNumbers)
		}

		var response string
		fmt.Print("Do you want to generate another set of numbers? (y/n) ")
		fmt.Scanln(&response)
		if response != "y" {
			break
		}
	}
}

