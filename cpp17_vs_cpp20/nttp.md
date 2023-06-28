# Non-template type parameters

  ```cpp
  struct msg {
    int type;
  };
  ```

  ```cpp
  template<msg m>
  auto parse() {
    // ...
  }
  ```

  ```
  parse<msg{.type = 42}>();
  ```

> Useful for templated configurations

  ```cpp
  int main() {
    unordered_map<{.key = std::string_view(), .value = std::size_t()}> map{};
    map["NTTP"] = 0x20;
    assert(0x20 == map["NTTP"]);
  }
```
