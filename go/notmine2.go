package main

import "fmt"

/**
 * []rune instead of []byte — Go strings are UTF-8, so you must iterate with range 
 * (which yields rune / Unicode codepoints) rather than byte indices. 
 * Appending to a []rune slice and converting back with string(result) 
 * handles the encoding automatically.
 * rune arithmetic — The offset math is identical to the Python version; 
 * Go's rune is just an alias for int32, so Unicode codepoint arithmetic works the same way.
 */ 
func toBoldSansSerif(text string) string {
	result := []rune{}
	for _, ch := range text {
		switch {
		case ch >= 'A' && ch <= 'Z':
			result = append(result, rune(0x1D5D4+(ch-'A')))
		case ch >= 'a' && ch <= 'z':
			result = append(result, rune(0x1D5EE+(ch-'a')))
		case ch >= '0' && ch <= '9':
			result = append(result, rune(0x1D7EC+(ch-'0')))
		default:
			result = append(result, ch)
		}
	}
	return string(result)
}

func main() {
	original := "Greater Zurich 2024"
	bold := toBoldSansSerif(original)
	restored := fromBoldSansSerif(bold)


	fmt.Println("Original: ", original)
	fmt.Println("Bold:     ", bold)
	fmt.Println("Restored: ", restored)
	fmt.Println("Roundtrip OK:", original == restored)

	fmt.Println(toBoldSansSerif("Greater Zurich"))
	fmt.Println(toUnicodeBold("Greater Zurich", "bold-italic-sans"))
}

var boldStyles = map[string][3]rune{
	"bold-serif":       {0x1D400, 0x1D41A, 0x1D7CE},
	"bold-sans-serif":  {0x1D5D4, 0x1D5EE, 0x1D7EC},
	"bold-italic-sans": {0x1D63C, 0x1D656, 0x1D7EC},
}

func toUnicodeBold(text, style string) string {
	offsets, ok := boldStyles[style]
	if !ok {
		return text
	}
	result := []rune{}
	for _, ch := range text {
		switch {
		case ch >= 'A' && ch <= 'Z':
			result = append(result, rune(offsets[0]+(ch-'A')))
		case ch >= 'a' && ch <= 'z':
			result = append(result, rune(offsets[1]+(ch-'a')))
		case ch >= '0' && ch <= '9':
			result = append(result, rune(offsets[2]+(ch-'0')))
		default:
			result = append(result, ch)
		}
	}
	return string(result)
}

func fromBoldSansSerif(text string) string {
	result := []rune{}
	for _, ch := range text {
		switch {
		case ch >= 0x1D5D4 && ch <= 0x1D5ED: // 𝗔–𝗭
			result = append(result, 'A'+(ch-0x1D5D4))
		case ch >= 0x1D5EE && ch <= 0x1D607: // 𝗮–𝘇
			result = append(result, 'a'+(ch-0x1D5EE))
		case ch >= 0x1D7EC && ch <= 0x1D7F5: // 𝟬–𝟵
			result = append(result, '0'+(ch-0x1D7EC))
		default:
			result = append(result, ch)
		}
	}
	return string(result)
}