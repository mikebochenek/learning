package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

func saveWiki(filename string, body []byte) {
	/* mostly from http://go-database-sql.org/accessing.html */
	db, err := sql.Open("mysql",
		"test2:test2@tcp(127.0.0.1:3306)/test2")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	/* mostly from http://go-database-sql.org/modifying.html */
	stmt, err := db.Prepare("INSERT INTO wiki(filename, content) VALUES(?, ?)")
	if err != nil {
		log.Fatal(err)
	}

	res, err := stmt.Exec(filename, body)
	if err != nil {
		log.Fatal(err)
	}

	lastId, err := res.LastInsertId()
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("inserted record: ", lastId)
}
