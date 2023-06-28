# Concepts

> syntax

  C++17
  ```cpp
  template<class T> auto parse(T);
  ```

  C++20:
  ```cpp
  auto parse(auto);
  ```

> Note: auto = weakest concept // template<class T> Auto = true; // always satisfied

> constraints

  C++17 - SFINAE
  ```cpp
  template<class T, std::enable_if_t<Constrained, bool> = true> 
  auto parse(T);
  ```

  C++20
  ```cpp
  template<class T> concept = Constrained;
  template<Constrained T> auto parse(T);
  ```
  or
  ```cpp
  template<class T> requires Constrained<T> auto parse(T);
  ```

  Note: destructors can be constrained and there is not need for type

  ```cpp
  ~parser() requires std::abstract<T> = default;
  ```

  Note: tere syntax
  ```cpp
  auto parse(Constrained auto);
  ```

> Design by introspection (Andrei Alexandrescu)

  C++17
  ```cpp
  template<class T> using has_foo = decltype(std::declval<T&>().foo);

  if constexpr(std::is_detected<has_foo, T>) {
    // ...
  }
  ```

  C++20
  ```cpp
  if constexpr (requires(T t) { t.foo; }) {
    // ...
  }
  ```
