# Misc

> explicit(bool)

  C++17
  ```cpp
  explicit parser(t);

  template<class... Ts, std::enable_if<sizeof...(Ts) > 0, bool>=true>
  parser(Ts...);
  ```

  C++20
  ```cpp
  template<class... Ts>
  explicit(sizeof...(Ts) == 1) parse(Ts...)
  ```

---

> std::bit_cast - allows to safely reinterpret the representation of an object of one type as another type, without violating strict aliasing rules. The function ensures that the bitwise representation of the object is preserved during the conversion

  C++17
  ```cpp
  auto msg = reinterpret_cast<Msg*>(packet);
  ```

  C++20
  ```cpp
  auto msg = std::bit_cast<Msg*>(packet);
  ```

> namespace inline

  C++17
  ```cpp
  namespace foo::bar {
      namespace inline v1 {
      }
  }
  ```

  C++20
  ```cpp
  namespace foo::bar::inline v1 { }
  ```

> typeid is constexpr

  C++17
  ```cpp
  static_assert(std::is_same_v<decltype(42), int>);
  ```

  C++20
  ```cpp
  static_assert(typeid(42) == typeid(int));
  ```

> source_location

  ```cpp
  void log(const std::string& message, const std::source_location& location = std::source_location::current()) {
    std::cout << "Log Message: " << message << '\n';
    std::cout << "File: " << location.file_name() << '\n';
    std::cout << "Line: " << location.line() << '\n';
    std::cout << "Function: " << location.function_name() << '\n';
    std::cout << "Column: " << location.column() << '\n';
    std::cout << '\n';
  }
  ```

  ```cpp
  log("Hello, world!");
  ```

> spaceship operator

  ```cpp
  struct foo {
    int i;
    bool b;
    constexpr auto operator<=>(const foo&) const = default;
  };
  ```

  ```
  static_assert(foo{.i=1, .b=true} != foo{.i=2, .b=false});
  ```
