package main

import (
	"fmt"
	"strings"
)

func findNemo(in string) {
	index := strings.Index(in, "Nemo")
	if index != -1 {
		fmt.Printf("I found Nemo at %d", index)
	} else {
		fmt.Printf("I can't find Nemo")
	}

}

func main() {
	findNemo("I am finding Nemo !")
}
