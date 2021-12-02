package aoc.utils;

import static java.util.stream.Collectors.toList;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.List;
import java.util.Objects;

public class LoadInput {
  public static List<String> load(int day) {

      String paddedDay = String.valueOf(day);
      if(day < 10) {
        paddedDay = "0" + day;
      }
      String fileName = "./aoc/inputs/day" + paddedDay + ".txt";

      BufferedReader r = new BufferedReader(new InputStreamReader(
          Objects.requireNonNull(ClassLoader.getSystemResourceAsStream(fileName))));
      return r.lines().collect(toList());
  }
}
