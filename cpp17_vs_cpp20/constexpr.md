# constexpr

- virtual
- std::unique_ptr
- std::string
- std::vector
- ...

> Example - constexpr std::function

  ```cpp
  template <class>
  class function;

  template <class R, class... TArgs>
  class function<R(TArgs...)> {
      struct interface {
          constexpr virtual auto operator()(TArgs...) -> R = 0;
          constexpr virtual ~interface() = default;
      };

      template <class Fn>
      struct implementation final : interface {
          constexpr explicit(true) implementation(Fn fn) : fn{fn} {}
          constexpr auto operator()(TArgs... args) -> R { return fn(args...); }

         private:
          Fn fn{};
      };

     public:
      template <class Fn>
      constexpr function(Fn fn) : fn{std::make_unique<implementation<Fn>>(fn)} {}

      constexpr auto operator()(TArgs... args) const -> R {
          return (*fn)(args...);
      }

     private:
      std::unique_ptr<interface> fn{};
  };

  template <class>
  struct function_traits {};

  template <class R, class B, class... TArgs>
  struct function_traits<R (B::*)(TArgs...) const> {
      using type = R(TArgs...);
  };

  template <class F>
  function(F) -> function<typename function_traits<decltype(&F::operator())>::type>;
  ```

  ```cpp
  consteval auto test_empty() {
      function f = [] { return 42; };
      return f();
  }

  consteval auto test_arg() {
      function f = [](int i) { return i; };
      return f(42);
  }

  consteval auto test_capture() {
      int i = 42;
      function f = [&] { return i; };
      return f();
  }

  static_assert(42 == test_empty());
  static_assert(42 == test_arg());
  static_assert(42 == test_capture());
  ```
