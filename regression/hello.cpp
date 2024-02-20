#include <iostream>

int main() {
    int x = 0;
    int counter;

    std::system("clear");
    std::cout << "Enter a number: ";

    std::cin >> counter;
    if (counter <= 0) { // Corrected the condition
        return 1;
    }
    counter--; // Decrements counter if it's greater than 1
    while (counter >= 0) {
        std::cout << "value of counter: " << counter << std::endl;
        counter--;
    }
    return 0;
}
