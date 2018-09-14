package raindrops

import (
	"fmt"
)

func Convert(number int) string{
	rain_sound := ""
	if number % 3 == 0 {
		rain_sound  += "Pling"
	} 
	if number % 5 == 0 {
		rain_sound += "Plang"
	} 
	if number % 7 == 0 {
		rain_sound += "Plong"
	}
	if rain_sound == ""{
		return fmt.Sprintf("%d", number)
	}
	return rain_sound
}

