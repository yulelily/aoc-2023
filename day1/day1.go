package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	// we are back to dealing with pointers !!!!! 🙃
	// create a os.File pointer
	f, err := os.Open("./input.txt")
	check(err)

	// create a file scanner using the bufio package and then split the input into lines
	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	res := 0
	// process each line one by one
	for scanner.Scan() {
		s := scanner.Text()

		// probably could combine these loops somehow...
		l, r := 0, len(s) - 1
		for l < len(s) && (s[l] > 57 || s[l] < 48) {
			l++
		}
		for r >= 0 && (s[r] > 57 || s[r] < 48) {
			r--
		}
		left := int(s[l]) - 48
		right := int(s[r]) - 48
		res += left * 10 + right
	}
	fmt.Println(res)

	f.Close()
}