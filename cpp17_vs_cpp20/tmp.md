# Template-Meta-Programming

  C++17
  ```cpp
  boost.mp11
  ```

  C++20
  ```cpp
  #include <ranges>

  auto hello_world = [](auto list, auto add_const, auto has_value){
   return list                          // int, foo, val, bar
    | std::views::drop(1_c)             // foo, val, bar
    | std::views::reverse               // bar, val, foo
    | std::views::take(2_c)             // bar, val
    | std::views::transform(add_const)  // bar const, val const
    | std::views::filter(has_value)     // val const
    ;
  };
  ```

  ```cpp
  auto add_const = []<class T> -> T const {};
  auto has_value = []<class T> { return requires(T t) { t.value; }; };
  ```

> Note: can be used with types/values

  ```cpp
  auto slice = [](auto list, auto begin, auto end) {
    return list
      | std::views::drop(begin)      // STL/ranges!
      | std::views::take(end - 1_c); // filter/reverse/sort/...
  };
  ```

  ```cpp
  // type_list
  static_assert(slice(mp::list<int, double, float, short>, 1_c, 3_c) == mp::list<double, float>);
  ```

  ```cpp
  // value_list
  static_assert(slice(mp::list<1, 2, 3, 4>, 1_c, 3_c) == mp::list<2, 3>);
  ```

  ```cpp
  // fixed_string
  static_assert(slice(mp::list<"foobar">, 1_c, 3_c) == mp::list<"oo">);
  ```

  ```cpp
  // tuple of values
  static_assert(slice(std::tuple{1, 2, 3, 4}, 1_c, 3_c) == std::tuple{2, 3});
  ```

  ```cpp
  int main(int argc, const char**) {
    // run-time tuple of values
    assert((slice(std::tuple{1, argc, 3, 4}, 1_c, 3_c) ==
                  std::tuple{argc, 3}));
  }
  ```
