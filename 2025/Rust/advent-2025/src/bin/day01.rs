use core::num;
use std::{any, result, str::FromStr};

use advent_2025::read_input;
use anyhow::{Context, Result};

enum Direction {
    Left,
    Right,
}

struct Instruction {
    direction: Direction,
    amount: i32,
}

impl FromStr for Instruction {
    type Err = anyhow::Error;

    fn from_str(s: &str) -> Result<Self> {
        let (dir_char, num_str) = s.split_at(1);
        let amount = num_str.parse().context("Failed to parse amount")?;
        let direction = match dir_char {
            "L" => Direction::Left,
            "R" => Direction::Right,
            _ => return Err(anyhow::anyhow!("Invalid direction: {}", dir_char)),
        };
        Ok(Instruction { direction, amount })
    }
}

struct Dial {
    position: i32,
}

impl Dial {
    fn new(start: i32) -> Self {
        Self { position: start }
    }

    fn rotate(&mut self, instr: &Instruction) -> i32 {
        let change = match instr.direction {
            Direction::Left => -instr.amount,
            Direction::Right => instr.amount,
        };

        self.position = (self.position + change).rem_euclid(100);

        if self.position == 0 { return 1 } else { 0 }
    }

    fn simulate_rotation(&mut self, instr: &Instruction) -> i32 {
        let mut hits = 0;
        for _ in 0..instr.amount {
            match instr.direction {
                Direction::Left => self.position -= 1,
                Direction::Right => self.position += 1,
            };

            self.position = self.position.rem_euclid(100);

            if self.position == 0 {
                hits += 1;
            }
        }
        hits
    }
}

fn main() -> Result<()> {
    let input = read_input(1)?;

    let data = input.trim();

    println!("Part 1: {:#?}", part1(data));
    println!("Part 2: {:#?}", part2(data));

    Ok(())
}

fn part1(input: &str) -> Result<i32> {
    let mut dial = Dial::new(50);
    let mut total = 0;

    for line in input.lines() {
        let instr: Instruction = line.parse()?;
        total += dial.rotate(&instr);
    }

    Ok(total)
}

fn part2(input: &str) -> Result<i32> {
    let mut dial = Dial::new(50);
    let mut total_hits = 0;

    for line in input.lines() {
        let instr: Instruction = line.parse()?;
        total_hits += dial.simulate_rotation(&instr);
    }

    Ok(total_hits)
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_INPUT: &str = "\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82";

    #[test]
    fn test_part1() {
        assert_eq!(part1(EXAMPLE_INPUT).unwrap(), 3);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2(EXAMPLE_INPUT).unwrap(), 6);
    }
}
