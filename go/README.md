Go
========

This is my experiments playground with Go (aka golang)

The best part of golang is that it's so fast and so simple.  Doing CONTROL+S reformats, saves, compiles, and runs all the test cases in 0.050 seconds!

Definition: Go is an open source programming environment that makes it easy to build simple, reliable, and efficient software.

# Note module requirement in 1.16

Golang evolves just like everything these days: so we need to either [turn-off](https://stackoverflow.com/questions/66894200/error-message-go-go-mod-file-not-found-in-current-directory-or-any-parent-dire
) or follow the new requirement to run some of the older code.
~~~
go env -w GO111MODULE=off
~~~

## version
On Ubuntu
~~~
go version go1.10.4 linux/amd64
~~~
