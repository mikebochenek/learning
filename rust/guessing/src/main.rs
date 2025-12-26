use std::io;
use rand::Rng;

/* https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html 
   (base) PS C:\dev\code\learning\rust\guessing> dir .\target\debug\ 
   cargo run 
   cargo build 
   cargo test */
fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("The secret number is: {secret_number}");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {guess}");
}