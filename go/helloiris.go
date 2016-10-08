package main

import (
	"database/sql"
	"log"
	"os"

	_ "github.com/go-sql-driver/mysql"
	"github.com/kataras/iris"
)

func main() {
	iris.Config.IsDevelopment = true // this will reload the templates on each request

	dbtest()

	iris.Get("/", func(ctx *iris.Context) {
		logger := log.New(os.Stdout, "logger: ", log.Lshortfile) //TODO seems inefficient to create a new one each time
		logger.Print("get request for /")

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

func dbtest() {
	db, err := sql.Open("mysql", "test:@/presto")
	if err != nil {
		panic(err.Error()) // Just for example purpose. You should use proper error handling instead of panic
	}
	defer db.Close()

	//var id int
	stmtOut, err := db.Prepare("SELECT id,email FROM user")
	//err = stmtOut.Query().Scan(&id)
	if err != nil {
		panic(err.Error()) // proper error handling instead of panic in your app
	}
	defer stmtOut.Close()

}
