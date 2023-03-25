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

func generateNPrimes(n int) []int {
    primes := []int{}
    num := 2
    for len(primes) < n {
        if isPrime(num) {
            primes = append(primes, num)
        }
        num++
    }
    return primes
}

func main() {
    for {
        var n int
        fmt.Print("Enter the number of prime numbers to generate: ")
        _, err := fmt.Scanln(&n)
        if err != nil {
            fmt.Printf("Invalid input: %v\n", err)
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
        primes := generateNPrimes(n)
        fmt.Printf("The first %d prime numbers are: %v\n", n, primes)
        var response string
        fmt.Print("Do you want to generate another set of prime numbers? (y/n) ")
        _, err = fmt.Scanln(&response)
        if err != nil {
            break
        }
        if response != "y" {
            break
        }
    }
}

