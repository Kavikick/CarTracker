/*
    Main thread of program execution

    Loops through to see if there is user input and if there is it handles it

    Also if the test flag is set it will run the test suite instead of the
   program
*/

#include "UI.h"

#include <iostream>
using namespace std;

bool runAllTests();

int main() {
  // Execute tests before every launch
  runAllTests();

  // main thread of execution
  UI userInterface;
  userInterface.run();
}