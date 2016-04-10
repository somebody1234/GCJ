// rust plz
#![feature(step_by)]

fn main() {
    // hah, hardcoding the input ¯\_(ツ)_/¯
    let (n, mut j) = (16, 50);
    // ... and output
    println!("Case #1:");

    // loop through all possible 1[...]1 coins
    for coin in (2u64.pow(n-1)+1..).step_by(2) {
        // the numbers in bases 2-10
        let mut nums = vec![0u64; 9];

        // loop through every bit and manually "base-convert" into nums
        for bit_idx in 0..n+1 {
            if ((coin >> bit_idx) & 1) == 1 {
                // add the proper number to everything inside nums
                for (idx, num) in nums.iter_mut().enumerate() {
                    *num += ((idx + 2) as u64).pow(bit_idx);
                }
            }
        }

        // get a list of the 9 divisors, or skip this number if any of the
        //   items in nums is prime
        let divisors = if let Some(divisors) = get_divisors(&nums) {
            divisors
        } else { continue; };

        // print the coin and count how many times we've printed
        println!("{:b} {}", coin, divisors.iter().map(|d| d.to_string())
                 .collect::<Vec<String>>().join(" "));
        j -= 1;
        if j == 0 { return; }
    }
}

// returns Some(Vec<u64>) if none of the numbers are prime, containing a list
//   of one divisor of each number, or None if any of the numbers are prime
fn get_divisors(nums: &Vec<u64>) -> Option<Vec<u64>> {
    let mut divisors = vec![];
    for &num in nums.iter() {
        divisors.push(
            if      num %  2 == 0 { 2 }
            else if num %  3 == 0 { 3 }
            else if num %  5 == 0 { 5 }
            else if num %  7 == 0 { 7 }
            else if num % 11 == 0 { 11 }
            else if num < (11*11 as u64) { return None }
            else {
                if let Some(divisor) = (13..((num as f64).sqrt() as u64))
                        .find(|d| num % d == 0 ) {
                    divisor
                } else {
                    return None;
                }
            }
        );
    }
    Some(divisors)
}
