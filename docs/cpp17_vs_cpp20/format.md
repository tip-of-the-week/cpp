# std.format

  C++17
    fmt.format

  C++20
  ```cpp
  static_assert("42"sv         == fmt::format("{}", 42));
  static_assert("42.."sv       == fmt::format("{:.<4}", 42));
  static_assert("..42"sv       == fmt::format("{:.>4}", 42));
  static_assert("42 0x2a"sv    == fmt::format("{0} {0:#x}", 42)); // use 0 parameter
  static_assert("  QL  "sv     == fmt::format("{:^6}", "QL"));
  static_assert("  QL  "sv     == fmt::format("{:>4}  ", "QL"));
  static_assert("QL        "sv == fmt::format("{:<{}}", "QL", 10));
  ```
