# reflection

> to_tuple (possible in C++17 with any)

```cpp
  template <class T>
  [[nodiscard]] constexpr auto to_tuple(T&& obj) {
    // ...
    if constexpr (requires { [&obj] { auto&& [p1, p2] = obj; }; }) {
      auto&& [p1, p2] = std::forward<T>(obj);
      return std::tuple{p1, p2};
    } else if constexpr (requires { [&obj] { auto&& [p1] = obj; }; }) {
      auto&& [p1] = std::forward<T>(obj);
      return std::tuple{p1};
    } else {
      return std::tuple{};
    }
  };
```

```cpp
struct foo { int i{}; bool b{}; };

static_assert(std::tuple{42, true} ==
            to_tuple(foo{.i = 42, .b = true})
)
```

> C++23 #embed

  ```cpp
  template <fixed_string Name>
  constexpr auto meta_contains = [] {
      static constexpr char self[] = {
        #embed __FILE__
      };
      const auto code = std::string_view(std::data(self), std::size(self));
      const auto find = code.find(Name);
      return find != std::string_view::npos and code[find - 1] != '\"';
  }();
  ```

  ```cpp
  struct foo {};
  struct bar {};

  auto fn() -> void;

  static_assert(not meta_contains<"struct x">);
  static_assert(not meta_contains<"STD::string_view">);
  static_assert(meta_contains<"std::string_view">);
  static_assert(meta_contains<"struct foo">);
  static_assert(meta_contains<"struct bar">);
  static_assert(meta_contains<"auto fn()">);
  ```
