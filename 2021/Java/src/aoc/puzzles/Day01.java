package aoc.puzzles;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;
import aoc.utils.LoadInput;

public class Day01 {

  public static void main (String[] args) {
    List<Integer> input = LoadInput.load(1).stream().map(Integer::valueOf).collect(Collectors.toList());
    Day01 d1 = new Day01();
    System.out.println(d1.part1(input));
    System.out.println(d1.part2(input));
  }



  public Object part1(List<Integer> input) {
    int count = 0;

    for (int i = 1; i < input.size(); i++) {
      if (input.get(i - 1) < input.get(i)) {
        count++;
      }
    }
    return count;
  }


  public Object part2(List<Integer> input) {
    int count = 0;

    for (int i = 3; i < input.size(); i++) {
      if (input.get(i - 3) + input.get(i - 2) + input.get(i - 1)
          <  input.get(i - 2) + input.get(i - 1) + input.get(i)) {
        count++;
      }
    }
    return count;
  }
}


