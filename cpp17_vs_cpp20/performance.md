# Performance

> Attributes: [[likely]], [[unlikely]]
  *  reorders instructions

  ```cpp
    if (msg.type == TRADE) [[likely]] {
      // ...
    }
  ```

  ```cpp
    if (msg.type == UNKNOWN) [[unlikely]] {
      // ...
    }
  ```

> Attribute: [[no_unique_address]]

  ```cpp
  template <class T, fixed_string Str, auto Offset = 0>
  struct field {
    constexpr const auto& get() const {
      return *reinterpret_cast<const T*>(reinterpret_cast<const char*>(this) + Offset);
    }
    constexpr operator const T&() const { return get(); }
  };

  enum class side : std::uint8_t { buy, sell };
  struct trade {
      [[no_unique_address]] field<std::int32_t, "price"> price;
      [[no_unique_address]] field<std::uint32_t, "size", sizeof(std::int32_t)> quantity;
      [[no_unique_address]] field<side, "side", sizeof(std::int32_t) + sizeof(std::uint32_t)> side;
  };
  static_assert(1 == sizeof(trade));

  auto parse(const void* msg) {
    const auto& trade = *std::bit_cast<const ::trade*>(msg);
    assert(42 == trade.price);
    assert(100 == trade.quantity);
    assert(side::sell == trade.side);
  }

  int main() {
    struct [[gnu::packed]] {
      std::int32_t price{42};
      std::uint32_t quantity{100};
      side side{side::sell};
    } trade{};

    parse(std::addressof(trade));
  }
  ```
