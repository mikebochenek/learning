use std::{
    fs::File,
    io::{prelude::*, BufReader},
    time::{SystemTime, UNIX_EPOCH},
};
use chrono::prelude::*;

// https://stackoverflow.com/questions/30801031/read-a-file-and-get-an-array-of-strings
fn lines_from_file(filename: &str) -> Vec<String> {
    let mut path: String = "".to_string();
    if cfg!(windows) { // https://stackoverflow.com/questions/43292357/how-can-one-detect-the-os-type-using-rust
        let p: &str = "C:/dev/data/aoc/2019/"; 
        path = format!("{p}{filename}"); 
        println!("windows trying to read {}", path); // can I try to rewrite filename?
    } else if cfg!(unix) {
        let p: &str = "/home/mike/Documents/aoc/2019/";
        path = format!("{p}{filename}"); 
        println!("unix trying to read {}", path);
    }

    let file = File::open(path).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

fn fuel(mass: i32) -> i32 {
    return (mass / 3) - 2;
}

fn day1() {
    let filename: &str = "day1.txt";
    let lines = lines_from_file(filename); // ("/etc/hosts");

    let mut sum = 0;
    for line in lines {
        //println!("{:?}", line);
        let parsed: i32 = line.parse().unwrap(); // https://doc.rust-lang.org/rust-by-example/conversion/string.html
        sum += fuel(parsed)
    }

    assert!(654 == fuel(1969));
    assert!(33583 == fuel(100756));
    println!("sum {} equal expected value? {}", sum, 3320816 == sum);
}

fn main() {
    day1();

    let utc = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();
    let now = Utc::now().to_string();
    println!("\t{} ({} since unix epoch)", now, utc)
}
