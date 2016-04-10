use std::io;
use std::io::prelude::*;

fn main() {
    // discard first line
    let stdin = io::stdin();
    let mut _s = String::new();
    stdin.read_line(&mut _s).unwrap();

    // read all of stdin
    for (caseno, line) in stdin.lock().lines().enumerate() {
        let mut runs = 1;
        let _line = line.unwrap();
        let mut iter = _line.chars();
        let mut plus = iter.next().unwrap() == '+';
        for ch in iter {
            if (ch == '-' && plus) || (ch == '+' && !plus) {
                plus = !plus;
                runs += 1;
            }
        }
        println!("Case #{}: {}", caseno + 1, if plus { runs - 1 } else { runs });
    }
}
