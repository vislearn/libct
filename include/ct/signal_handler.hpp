#ifndef LIBCT_SIGNAL_HANDLER_HPP
#define LIBCT_SIGNAL_HANDLER_HPP

extern "C" {
  static volatile sig_atomic_t ct_signaled;

  void ct_signal_handler(int sig)
  {
    ct_signaled = 1;
  }
}

namespace ct {

class signal_handler {
public:
  signal_handler()
  {
    ct_signaled = 0;
    old_handler_ = std::signal(SIGINT, ct_signal_handler);
  }

  ~signal_handler()
  {
    std::signal(SIGINT, old_handler_);
    if (signaled())
      std::raise(SIGINT);
  }

  bool signaled() const { return ct_signaled != 0; };

protected:
  void(*old_handler_)(int);
};

}

#endif

/* vim: set ts=8 sts=2 sw=2 et ft=cpp: */
