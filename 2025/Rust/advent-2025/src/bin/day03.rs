use advent_2025::read_input;
use anyhow::Result;

fn highest_voltage(digits: &[u32]) -> u32 {
    let mut highest_voltage = 0;
    let mut best_first_digit = 0;
    for (i, &first) in digits.iter().enumerate() {
        if first <= best_first_digit {
            continue;
        }
        best_first_digit = first;

        for &second in &digits[i + 1..] {
            let voltage = first * 10 + second;
            if voltage > highest_voltage {
                highest_voltage = voltage;
            }
        }
    }
    highest_voltage
}

fn high_voltage2(digits: &[u32]) -> u64 {
    let mut result_digits = Vec::new();
    let needed = 12;
    let mut current_index = 0;
    let mut voltage = 0;

    for i in 0..needed {
        let remaining = needed - 1 - i;
        let end = digits.len() - remaining;
        let seach_slice: &[u32] = &digits[current_index..end];
        let max_number = seach_slice.iter().max().unwrap();
        let max_index = seach_slice.iter().position(|x| x == max_number).unwrap();
        current_index += max_index + 1;
        result_digits.push(*max_number);
    }

    for d in result_digits {
        voltage = voltage * 10 + (d as u64);
    }
    voltage
}
fn main() -> Result<()> {
    let input = read_input(3)?;

    let data = input.trim();

    println!("Part 1: {:#?}", part1(data));
    println!("Part 2: {:#?}", part2(data));

    Ok(())
}

fn part1(input: &str) -> Result<u32> {
    let mut total_voltage = 0;
    for line in input.lines() {
        let digits: Vec<u32> = line.chars().filter_map(|c| c.to_digit(10)).collect();
        total_voltage += highest_voltage(&digits);
    }

    Ok(total_voltage)
}

fn part2(input: &str) -> Result<u64> {
    let mut total_voltage: u64 = 0;
    for line in input.lines() {
        let digits: Vec<u32> = line.chars().filter_map(|c| c.to_digit(10)).collect();
        total_voltage += high_voltage2(&digits);
    }

    Ok(total_voltage)
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_INPUT: &str = "\
987654321111111
811111111111119
234234234234278
818181911112111";

    #[test]
    fn test_part1() {
        assert_eq!(part1(EXAMPLE_INPUT).unwrap(), 357);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2(EXAMPLE_INPUT).unwrap(), 3121910778619);
    }
}
