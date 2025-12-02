use anyhow::{Context, Result};
use std::fs;

pub fn read_input(day: u8) -> Result<String> {
    let path = format!("inputs/day{:02}.txt", day);
    fs::read_to_string(&path).with_context(|| format!("Failed to read input file: {}", path))
}

pub fn parse_lines<T: std::str::FromStr>(input: &str) -> Vec<T>
where
    <T as std::str::FromStr>::Err: std::fmt::Debug,
{
    input
        .lines()
        .map(|line| line.parse::<T>().unwrap())
        .collect()
}
