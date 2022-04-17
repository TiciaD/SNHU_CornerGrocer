#include <fstream>
#include <iostream>
#include <iomanip>
#include "Display.h"

void Display::displayMenu() {
    cout << "Choose an option" << endl;
    cout << "[1] Display all items purchased and number of times each was purchased " << endl;
    cout << "[2] Display number of times a specific item was purchased" << endl;
    cout << "[3] Display histogram based on the number of appearances of each item" << endl;
    cout << "[4] Quit" << endl;
}

void Display::displayHistogram() {
    string itemName;
    int itemQuantity{ 0 };
    // string that adds a green background behind the letter X
    string greenXBlock = "\033[3;42;30mX\033[0m";

    ifstream file;
    // Open data file
    file.open("frequency.dat");

    // assign item name from file
    file >> itemName;
    // assign item quanity from file
    file >> itemQuantity;
    // loop while file has information
    while (!file.fail()) {
        // print item name
        cout << setw(14) << left << itemName << setw(6);
        // loop until item quanity amount
        for (int i = 0; i < itemQuantity; i++) {
            // Print green X blocks in line with each other
            std::cout << std::right << greenXBlock;
        }
        // jump to newline
        cout << endl;
        // read and assign next item name
        file >> itemName;
        // read and assign next item quantity
        file >> itemQuantity;
    }
    // Close data file
    file.close();
}