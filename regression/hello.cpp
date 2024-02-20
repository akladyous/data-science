#include <iostream>

int main() {
  int x = 0;
  int counter;
  std::cin >> counter;

  while (counter >= 0) {
    std::cout << "value of counter: " << counter << std::endl;
    counter --;
  }

  return 0;
}
