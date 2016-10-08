package main

import "github.com/kataras/iris"

func main() {
	iris.Config.IsDevelopment = true // this will reload the templates on each request

	iris.Get("/", func(ctx *iris.Context) {
		ctx.Write("Hello, %s", "World!\n")
		ctx.Write(ctx.RequestHeader("User-Agent"))
		ctx.Write("\n")
		ctx.Write(ctx.RequestHeader("Forwarded"))
	})

	iris.Get("/myjson", func(ctx *iris.Context) {
		ctx.JSON(iris.StatusOK, iris.Map{
			"Name":     "Iris",
			"Released": "13 March 2016",
			"Stars":    5281,
		})
	})

	iris.Listen(":8080")
}
