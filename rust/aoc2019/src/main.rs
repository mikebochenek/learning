use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
    time::{SystemTime, UNIX_EPOCH},
};
use chrono::prelude::*;

// https://stackoverflow.com/questions/30801031/read-a-file-and-get-an-array-of-strings
fn lines_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    if cfg!(windows) { // https://stackoverflow.com/questions/43292357/how-can-one-detect-the-os-type-using-rust
        println!("this is windows"); 
        // can I try to rewrite filename?
    } else if cfg!(unix) {
        println!("this is unix alike");
    }

    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

fn fuel(mass: i32) -> i32 {
    return (mass / 3) - 2;
}

fn main() {
    println!("Hello, world!");
    //let lines = lines_from_file("/etc/hosts");
    let lines = lines_from_file("/home/mike/Documents/aoc/2019/day1.txt");

    let mut sum = 0;
    for line in lines {
        //println!("{:?}", line);
        let parsed: i32 = line.parse().unwrap(); // https://doc.rust-lang.org/rust-by-example/conversion/string.html
        sum += fuel(parsed)
    }

    println!("test1 {}", 654 == fuel(1969));
    println!("test2 {}", 33583 == fuel(100756));
    println!("sum {} equal expected value? {}", sum, 3320816 == sum);

    let e = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();
    let a = Utc::now().to_string();
    println!("{} - {}", a, e)
}
