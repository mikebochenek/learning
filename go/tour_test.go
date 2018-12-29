package main

import (
	"database/sql"
	"fmt"
	"log"
	"math/rand"
	"testing"

	_ "github.com/go-sql-driver/mysql"
)

func TestNothingInParticular(t *testing.T) { /** from https://tour.golang.org/basics/1 */
	fmt.Println("My favorite number is", rand.Intn(10))

	/* mostly from http://go-database-sql.org/accessing.html */
	db, err := sql.Open("mysql",
		"test2:test2@tcp(127.0.0.1:3306)/test2")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	var count int

	rows, err := db.Query("select count(*) from Users")
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()
	for rows.Next() {
		err := rows.Scan(&count)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println("user count is: ", count)
	}
	err = rows.Err()
	if err != nil {
		log.Fatal(err)
	}
}
