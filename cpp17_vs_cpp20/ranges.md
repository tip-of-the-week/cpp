# Ranges

  ```cpp
  std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  ```

  C++17
  ```
  #include <algorithm>
    std::vector<int> first_five{};
    std::copy(numbers.begin(), numbers.begin() + 5, std::back_inserter(first_five));
    std::reverse(first_five.begin(), first_five.end());
  ```

  C++20
  ```
  #include <ranges>
  auto first_five_reversed = numbers
      | std::views::take(5)
      | std::views::reverse;
  ```

> Note: ranges are lazy by default
