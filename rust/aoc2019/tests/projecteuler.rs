// https://projecteuler.net/problem=7
fn is_prime(n: u32) -> bool { // https://stackoverflow.com/questions/55790537/calculating-prime-numbers-in-rust
    let limit = (n as f64).sqrt() as u32;
    for i in 2..=limit {
        if n % i == 0 {
            return false;
        }
    }
    true
}


#[cfg(test)]
mod testpe {
    use super::*;

    #[test]
    fn test_prime() {
        assert_eq!(is_prime(17), true);
    }
}