package main

import (
	"database/sql"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	max := int64(10000)
	for i := int64(1); i <= max; i += 1 {
		//n := i*i + i + 41
		//isPrime := prime(n)
		isPrime := prime(i)

		if isPrime {
			//fmt.Println(i)
			savePrime(i)
		}
	}
}

func savePrime(p int64) int64 {
	/* mostly from http://go-database-sql.org/accessing.html */
	db, err := sql.Open("mysql",
		"test2:test2@tcp(127.0.0.1:3306)/test2")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	/* mostly from http://go-database-sql.org/modifying.html */
	stmt, err := db.Prepare("INSERT INTO primes(prime) VALUES(?)")
	if err != nil {
		log.Fatal(err)
	}

	res, err := stmt.Exec(p)
	if err != nil {
		log.Fatal(err)
	}

	lastId, err := res.LastInsertId()
	if err != nil {
		log.Fatal(err)
	}

	//fmt.Println("inserted record: ", lastId)
	return lastId
}

func prime(x int64) bool {
	for i := int64(2); i < x; i += 2 {
		if x%i == 0 {
			return false
		}
	}
	return true
}
