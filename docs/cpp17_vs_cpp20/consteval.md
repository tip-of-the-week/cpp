# consteval - like constexpr but only at compile-time

```cpp
[[nodiscard]] consteval parse(auto t) {
  // ...
  return t;
}
```

```cpp
int main(int argc, char**) {
  constexpr auto = parse(42); // okay
  auto = parse(argc); // error, not a constant expression
}
```
