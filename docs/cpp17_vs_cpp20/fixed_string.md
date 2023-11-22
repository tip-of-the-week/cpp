# fixed_string (compile-time string)

  ```cpp
  template<char....> struct ct_string{};
  ```

  C++17 via gnu-extension
  
  ```cpp
  template<class T, T... Cs>
  constexpr auto operator""_cs() { return ct_string<Cs...>{}; }
  
  template<class> struct foo {};
  foo<decltype("bar"_cs)>;
  ```

  C++20 via fixed_string

  ```cpp
  template <std::size_t N>
  struct fixed_string final {
      constexpr explicit(true) fixed_string(const auto... cs) : data{cs...} {}

      constexpr explicit(false) fixed_string(const char (&str)[N + 1]) {
          std::copy_n(str, N + 1, std::data(data));
      }

      [[nodiscard]] constexpr auto operator<=>(const fixed_string&) const = default;

      [[nodiscard]] constexpr explicit(false) operator std::string_view() const {
          return {std::data(data), N};
      }

      [[nodiscard]] constexpr auto size() const -> std::size_t { return N; }

      std::array<char, N + 1> data{};
  };
  ```

  ```cpp
  template<fixed_string> struct foo {};
  foo<"bar"> f{};
  ```

> Note: fixed_string doesn't have external linkage

  ```cpp
  template <stdext::fixed_string Str>
  static auto to_string = []<auto... Ns>(std::index_sequence<Ns...>) {
    return ct_string<Str.data[Ns]...>{};
  }(std::make_index_sequence<Str.size()>{});
  ```

  ```cpp
  static_assert(ct_string<'f', 'o', 'o'> == to_string<"foo">)
  ```
