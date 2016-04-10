use std::io;
use std::io::prelude::*;
use std::collections::HashSet;

fn main() {
    // discard first line
    let stdin = io::stdin();
    let mut _s = String::new();
    stdin.read_line(&mut _s).unwrap();

    // read all of stdin
    for (caseno, line) in stdin.lock().lines().enumerate() {
        let n = line.unwrap().parse::<u64>().unwrap();
        if n == 0 {
            println!("Case #{}: INSOMNIA", caseno + 1);
            continue;
        }
        let mut a = n;
        let mut hs = HashSet::new();
        loop {
            for ch in a.to_string().chars() { hs.insert(ch); }
            if hs.len() == 10 { break; }
            a += n;
        }
        println!("Case #{}: {}", caseno + 1, a);
    }
}
