# Designated initliazers

  ```cpp
  struct msg {
    int type;
    int value;
  }
  ```

  C++17
  ```cpp
  auto m = msg{42, 42}; // error prone
  ```

> for safety strong types would be preferred


  C++20
  ```cpp
  auto m = msg{.type = 42, .value = 42};
  ```
  
