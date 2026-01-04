use std::io;
use rand::Rng;
use regex::Regex;

/* https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html 
   (base) PS C:\dev\code\learning\rust\guessing> dir .\target\debug\ 
   cargo run 
   cargo build 
   cargo test */
/*
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
*/

fn regex_fun() { // https://medium.com/coderhack-com/an-in-depth-guide-to-regex-in-rust-2158220607f2
    println!("regex fun! why is this even here? LOL...");

    let re = Regex::new(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$").unwrap();
    assert!(re.is_match("hello@example.com"));
    assert!(!re.is_match("hello@example")); // Missing .com

    let re = Regex::new(r"^https?://[a-z0-9-.]{2,}\.[a-z]{2,4}(:[0-9]{2,5})?/?.*$").unwrap(); 
    assert!(re.is_match("https://example.com")); 
    assert!(!re.is_match("example.com")); // Missing https
}


// can you generate a short program in rust that demonstrates what make is different from java or go?  
// add comments to explain the strange parts to a newbie
// https://claude.ai/chat/6a18b2df-2597-45cf-8db0-817b3a3d462f

// Rust's biggest difference from Java/Go: OWNERSHIP
// Rust has no garbage collector. Instead, it uses a system where each value has ONE owner.
// When the owner goes out of scope, the value is automatically cleaned up.

fn main() {
    regex_fun();

    // === OWNERSHIP BASICS ===
    
    let s1 = String::from("hello");
    // s1 owns this String. Rust tracks this automatically.
    
    let s2 = s1;
    // MOVE: s1's value moves to s2. s1 is now invalid!
    // In Java/Go, this would copy a reference. In Rust, it's a move.
    // Uncomment the next line to see a compile error:
    // println!("{}", s1);  // ERROR: s1 is no longer valid
    
    println!("{}", s2);  // OK: s2 owns the value
    
    // === BORROWING ===
    
    let s3 = String::from("world");
    print_string(&s3);  // &s3 is a BORROW - s3 still owns it
    println!("{}", s3);  // s3 still works! It was borrowed, not moved
    
    // === MUTABLE BORROWING ===
    
    let mut s4 = String::from("rust");
    modify_string(&mut s4);  // Borrow mutably to modify
    println!("{}", s4);  // Prints "rust!" - modified inside the function
    
    // === NO GARBAGE COLLECTOR ===
    
    // Memory is freed automatically when ownership ends:
    {
        let temp = String::from("temporary");
        println!("{}", temp);
    } // temp is dropped here automatically - no GC needed!
    
    // === MULTIPLE OWNERSHIP (if you really need it) ===
    
    // Rc<T> allows multiple owners, but only in single-threaded code.
    // This is something Java/Go do by default; Rust makes you opt-in.
    let data = std::rc::Rc::new(String::from("shared"));
    let data2 = std::rc::Rc::clone(&data);
    println!("data: {}, data2: {}", data, data2);  // Both can use it
}

// This function BORROWS the string (doesn't take ownership)
fn print_string(s: &String) {
    // &String is an IMMUTABLE BORROW
    // We can read it, but not modify it
    println!("Borrowed: {}", s);
    // s goes out of scope here, but it's borrowed so the original owner still has it
}

// This function BORROWS the string mutably
fn modify_string(s: &mut String) {
    // &mut String is a MUTABLE BORROW
    // We can read AND modify it
    s.push_str("!");
    // The original owner can still see the changes
}

/* KEY DIFFERENCES FROM JAVA/GO:

JAVA:
  - Everything is (mostly) garbage collected
  - Ownership is implicit; you don't think about it
  - Memory leaks are rare but possible
  - No explicit control over when memory is freed

GO:
  - Garbage collected like Java
  - Simple, pragmatic approach
  - Less thinking about memory, but slower for performance-critical code

RUST:
  - NO garbage collector (performance!)
  - Ownership is explicit and enforced by the compiler
  - Memory is freed immediately when no longer needed (predictable)
  - The compiler catches mistakes at compile time, not runtime
  - Borrowing lets you temporarily use values without moving them
  - Forces you to think about resource management, but pays off in safety & speed
*/