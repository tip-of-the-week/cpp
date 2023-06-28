# Testing

> No macros

  ```cpp
  import boost.ut;

  constexpr auto sum(auto... values) { return (values + ...); }

  int main() {
    using namespace boost::ut;

    "sum"_test = [] {
      expect(sum(0) == 0u);
      expect(sum(1, 2) == 3u);
      expect(sum(1, 2) > 0u and 41u == sum(40, 2));
    };
  }
  ```

  ```sh
  Running "sum"...
    sum.cpp:11:FAILED [(3 > 0 and 41 == 42)]

  FAILED
  ===============================================================================
  tests:   1 | 1 failed
  asserts: 3 | 2 passed | 1 failed
  ```

> Compile time tests
  * no undefined behaviors no leaks (almost)

  ```cpp20
    int main() {
        static_assert(
            0u ==
                [] {
                    list<int> list{};
                    list.push_back(42);
                    list.clean();
                    return list.size();
                }(),
            "clean");

        static_assert(
            0u ==
                [] {
                    list<int> list{};
                    return list.size();
                }(),
            "size");

        static_assert(
            2u ==
                [] {
                    list<int> list{};
                    list.push_back(42);
                    list.push_back(43);
                    return list.size();
                }(),
            "size many");

        static_assert(
            1u ==
                [] {
                    list<int> list{};
                    list.push_back(42);
                    return list.size();
                }(),
            "push_back");

        static_assert(
            42 ==
                [] {
                    list<int> list{};
                    list.push_back(42);
                    return list.front();
                }(),
            "front");

        static_assert(
            std::tuple{2u, 42} ==
                [] {
                    list<int> list{};
                    list.push_back(42);
                    list.push_back(43);
                    return std::tuple{list.size(), list.front()};
                }(),
            "front many");

        static_assert(
            0u ==
                [] {
                    list<int> list{};
                    list.pop();
                    return list.size();
                }(),
            "pop empty");

        static_assert(
            0u ==
                [] {
                    list<int> list{};
                    list.push_back(42);
                    list.pop();
                    return list.size();
                }(),
            "pop");
    }
  }
  ```

> compile time error tests

  ```cpp
  struct { int foo; } foo;
  struct { } bar;

  static_assert(requires { foo.foo; });
  static_assert(not requires { bar.foo; });
  ```
