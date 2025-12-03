use std::str::FromStr;

use advent_2025::read_input;
use anyhow::{Context, Ok, Result};

fn main() -> Result<()> {
    let input = read_input(2)?;

    let data = input.trim();

    println!("Part 1: {:#?}", part1(data));
    println!("Part 2: {:#?}", part2(data));

    Ok(())
}

#[derive(Debug)]
struct Range {
    start: i64,
    end: i64,
}

impl FromStr for Range {
    type Err = anyhow::Error;

    fn from_str(s: &str) -> Result<Self> {
        let (start_str, end_str) = s
            .split_once('-')
            .ok_or_else(|| anyhow::anyhow!("Invalid format"))?;

        Ok(Range {
            start: start_str.parse().context("Invalid start")?,
            end: end_str.parse().context("Invalid end")?,
        })
    }
}

impl Range {
    fn iter(&self) -> std::ops::RangeInclusive<i64> {
        self.start..=self.end
    }
}

fn valid_pattern(num: i64) -> bool {
    let num_str = num.to_string();
    if num_str.len() % 2 == 0 {
        let size = num_str.len().div_ceil(2);
        let pattern: String = num_str[0..size].to_string();

        return num_str == pattern.repeat(2);
    }
    false
}

fn part1(input: &str) -> Result<i64> {
    let ranges: Vec<Range> = input
        .split(',')
        .map(|s| s.parse())
        .collect::<Result<Vec<_>>>()?;
    let mut total: i64 = 0;

    for range in ranges {
        println!("Proccessing range: {}-{}, ", range.start, range.end);

        for num in range.iter() {
            if valid_pattern(num) {
                total += num
            }
        }
    }
    Ok(total)
}

fn part2(input: &str) -> Result<i32> {
    Ok(0)
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_INPUT: &str = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124";

    #[test]
    fn test_part1() {
        assert_eq!(part1(EXAMPLE_INPUT).unwrap(), 1227775554);
    }

    // #[test]
    // fn test_part2() {
    //     assert_eq!(part2(EXAMPLE_INPUT).unwrap(), 6);
    // }
}
