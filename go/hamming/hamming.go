package hamming

import (
	"errors"
)

func Distance(a, b string) (int, error) {

	if len(a) != len(b) {
		return 0, errors.New("DNA length does not match")
	}
	count := 0

	for i := range a {
		if a[i] != b[i] {
			count++
		}
	}
	
	return count, nil
}
