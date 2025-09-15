#include <algorithm>
#include <cassert>
#include <iostream>

bool allEven(int arr[], int size) {
  // Professional C++ solution using std::all_of with lambda
  // using std::all_of
  return std::all_of(arr, arr + size, [](int elm){ return elm % 2 == 0;});
}

int main() {
  std::cout << "==============================================\n";
  std::cout << "       ALL EVEN ARRAY CHECKER\n";
  std::cout << "==============================================\n\n";

  // Test the allEven function
  // Test all even arrays
  {
    int arr1[] = {2, 4, 6, 8, 10};
    assert(allEven(arr1, 5) == true);
  }

  {
    int arr2[] = {0, 2, 4};
    assert(allEven(arr2, 3) == true);
  }

  {
    int arr3[] = {-2, -4, -6};
    assert(allEven(arr3, 3) == true);
  }

  // Test single even element
  {
    int arr4[] = {8};
    assert(allEven(arr4, 1) == true);
  }

  // Test arrays with at least one odd number
  {
    int arr5[] = {1, 2, 3, 4, 5};
    assert(allEven(arr5, 5) == false);
  }

  {
    int arr6[] = {2, 4, 6, 7, 8};
    assert(allEven(arr6, 5) == false);
  }

  {
    int arr7[] = {1, 3, 5, 7, 9};
    assert(allEven(arr7, 5) == false);
  }

  // Test single odd element
  {
    int arr8[] = {7};
    assert(allEven(arr8, 1) == false);
  }

  // Test arrays with zero (zero is even)
  {
    int arr9[] = {0, 0, 0};
    assert(allEven(arr9, 3) == true);
  }

  {
    int arr10[] = {0, 2, 4, 6};
    assert(allEven(arr10, 4) == true);
  }

  {
    int arr11[] = {0, 1, 2};
    assert(allEven(arr11, 3) == false);
  }

  // Test mixed positive and negative even numbers
  {
    int arr12[] = {-4, -2, 0, 2, 4};
    assert(allEven(arr12, 5) == true);
  }

  {
    int arr13[] = {-4, -2, 0, 1, 4};
    assert(allEven(arr13, 5) == false);
  }

  // Test larger arrays
  {
    int arr14[] = {100, 200, 300, 400, 500, 600};
    assert(allEven(arr14, 6) == true);
  }

  {
    int arr15[] = {100, 200, 300, 401, 500, 600};
    assert(allEven(arr15, 6) == false);
  }

  // Test edge case: empty array (should return true)
  {
    int *arr16 = nullptr;
    assert(allEven(arr16, 0) == true);
  }

  std::cout << "\n\n[✓] All tests passed! All even checker works correctly.\n";
  std::cout << "Function correctly checks if all elements in array are even.\n";

  return 0;
}
