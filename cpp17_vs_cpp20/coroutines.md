# State Machine

  C++17
  ```cpp
  constexpr auto establish = [] { std::puts("establish"); };
  constexpr auto close = [] { std::puts("close"); };
  constexpr auto is_valid = [] { return true; };
  constexpr auto reset = [] { std::puts("reset"); };

  sml::sm connection = [] {
    using namespace sml;
    return transition_table{
     * "Disconnected"_s + event<connect> / establish  = "Connecting"_s,
       "Connecting"_s   + event<established>          = "Connected"_s,
       "Connected"_s    + event<ping> [ is_valid ] / reset_timeout,
       "Connected"_s    + event<timeout> / establish  = "Connecting"_s,
       "Connected"_s    + event<disconnect> / close   = "Disconnected"_s
    };
  };
  ```

  ```
  int main() {
    connection.process_event(connect{});
    connection.process_event(established{});
    connection.process_event(ping{});
    connection.process_event(disconnect{});
  }
  ```

  C++20
  ```cpp
  constexpr auto establish = [] { std::puts("establish"); };
  constexpr auto close = [] { std::puts("close"); };
  constexpr auto is_valid = [] { return true; };
  constexpr auto reset = [] { std::puts("reset"); };

  class Connection {
      state connection() {
          for (;;) {
          disconnected:
              if (auto [event, data] = co_await sm; event == connect{}) {
                  establish();
              connecting:
                  if (auto [event, data] = co_await sm; event == established{}) {
                  connected:
                      switch (auto [event, data] = co_await sm; event) {
                          case ping{}:
                              if (is_valid(data)) reset();
                              goto connected;
                          case timeout{}:
                              establish();
                              goto connecting;
                          case disconnect{}:
                              close();
                              goto disconnected;
                      }
                  }
              }
          }
      }

     public:
      void process_event(const auto& event) { sm.process_event(event); }

     private:
      state_machine<int> sm{};
      state initial{connection()};
  };

  int main() {
      Connection connection{};
      connection.process_event(connect{});
      connection.process_event(established{});
      connection.process_event(ping{});
      connection.process_event(disconnect{});
  }
  ```
