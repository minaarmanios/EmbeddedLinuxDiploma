#include <cassert>
#include <iostream>
#include <stack>
#include <string>
#include <vector>

class FunctionBacktrace {
 private:
  static std::stack<std::string> callStack;
  std::string functionName;

 public:
  // Constructor - automatically enters function
  explicit FunctionBacktrace(const std::string &funcName) : functionName(funcName) {
    // write your solution here
    std::cout<< "Enter to [" <<funcName<< "]"<< std::endl;
    callStack.push(functionName);
  }

  // Destructor - automatically exits function
  ~FunctionBacktrace() {
    // write your solution here
     if (!callStack.empty() && callStack.top() == functionName) {
      std::cout<< "Exit from [" <<callStack.top()<< "]"<< std::endl;
      callStack.pop();
    }
  }

  // dont modify this function
  static void printBacktrace() {
    std::cout << "=== BACKTRACE ===" << std::endl;
    if (callStack.empty()) {
      std::cout << "No active functions" << std::endl;
      return;
    }

    std::vector<std::string> trace;
    std::stack<std::string> tempStack = callStack;

    // Extract all function names from stack
    while (!tempStack.empty()) {
      trace.push_back(tempStack.top());
      tempStack.pop();
    }

    // Print in reverse order (main first)
    for (int i = trace.size() - 1; i >= 0; i--) {
      std::cout << "-> " << trace[i] << std::endl;
    }
    std::cout << "=================" << std::endl;
  }

  // Get current stack depth
  static int getStackDepth() { return callStack.size(); }

  // Check if function is in stack
  static bool isFunctionInStack(const std::string &funcName) {
    // write your solution here
    std::stack<std::string> tempStack = callStack;
    while (!tempStack.empty()) {
      if (tempStack.top() == funcName) {
        return true;
      }
      tempStack.pop();
    }
    return false;
  }
};

// Static member definition
std::stack<std::string> FunctionBacktrace::callStack;

#define EnterFn FunctionBacktrace bt(__FUNCTION__)
#define ExitFn

#define PRINT_BT FunctionBacktrace::printBacktrace()

// dont modify these functions
void fun3() { EnterFn; }

void fun2() {
  EnterFn;
  fun3();
  PRINT_BT;
}

void fun1() {
  EnterFn;
  fun2();
}

void testBasicFunctionality() {
  EnterFn;
  // Test that we can detect function presence
  assert(FunctionBacktrace::isFunctionInStack("testBasicFunctionality") ==
         true);
  assert(FunctionBacktrace::getStackDepth() >= 1);
  ExitFn;
}

int main() {
  std::cout << "==============================================\n";
  std::cout << "        FUNCTION BACKTRACE VALIDATOR\n";
  std::cout << "==============================================\n\n";

  EnterFn;

  // Test 1: Basic functionality
  std::cout << "\n--- Test 1: Basic Function Calls ---\n";
  fun1();

  // Test 2: Stack depth verification
  std::cout << "\n--- Test 2: Stack Depth Tests ---\n";
  int initialDepth = FunctionBacktrace::getStackDepth();
  assert(initialDepth == 1);  // Only main should be active

  testBasicFunctionality();

  // Verify we're back to initial state
  assert(FunctionBacktrace::getStackDepth() == initialDepth);

  // Test 3: Function detection
  std::cout << "\n--- Test 4: Function Detection Test ---\n";
  assert(FunctionBacktrace::isFunctionInStack("main") == true);
  assert(FunctionBacktrace::isFunctionInStack("nonexistent") == false);

  // Test 4: Empty backtrace after cleanup
  std::cout << "\n--- Test 5: Final Backtrace ---\n";
  PRINT_BT;

  std::cout << "\n==============================================\n";
  std::cout << "         ALL TESTS PASSED! ✓\n";
  std::cout << "==============================================\n";

  return 0;
}
