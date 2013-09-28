// +build notmine1

// http://play.golang.org/p/eGRSgZqJyQ
package main

type I interface {
	Set(int)
}

type T struct {
	Value int
}

func (t *T) Set(v int) {
	t.Value = v
}

func main() {
	t := &T{}
	var i I = t
	i.Set(23)
	println(t.Value)
}
