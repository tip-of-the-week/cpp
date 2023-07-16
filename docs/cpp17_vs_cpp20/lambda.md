# Lambdas

```cpp
template<auto N> constexpr auto unroll = [](auto expr) {
  [expr]<auto ...Is>(std::index_sequence<Is...>) {
    ((expr(), void(Is)), ...);
  }(std::make_index_sequence<N>{});
};
```

```cpp
int main() {
  unroll<2>([]{ std::puts("!"); });
}
```

```asm
.LC0: .string "!"
main:
  sub     rsp, 8
  mov     edi, OFFSET FLAT:.LC0
  call    puts
  mov     edi, OFFSET FLAT:.LC0
  call    puts
  xor     eax, eax
  add     rsp, 8
  ret
```

Note: How to call templated lambda?

```cpp
auto l = []<auto...> {};
l.template operator()<42>()
```

> Lambda types

```cpp
static_assert(typeid([]{}) != typeid([]{}));
```

```cpp
static_assert(+[]{} != +[]{});
```

```cpp
auto expr = decltype([]{}){};
```
