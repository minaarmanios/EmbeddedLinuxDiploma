#include <algorithm>
#include <cassert>
#include <iostream>

bool anyEven(int arr[], int size) {
  // Professional C++ solution using std::any_of with lambda
  // using std::any_of
  return std::any_of(arr, arr + size, [](int elm){ return elm % 2 == 0;});
}

int main() {
  std::cout << "==============================================\n";
  std::cout << "       ANY EVEN ARRAY CHECKER\n";
  std::cout << "==============================================\n\n";

  // Test the anyEven function
  // Test arrays with at least one even number
  {
    int arr1[] = {1, 2, 3, 4, 5};
    assert(anyEven(arr1, 5) == true);
  }

  {
    int arr2[] = {1, 3, 5, 8, 7};
    assert(anyEven(arr2, 5) == true);
  }

  {
    int arr3[] = {2, 1, 3, 5, 7};
    assert(anyEven(arr3, 5) == true);
  }

  // Test all even arrays
  {
    int arr4[] = {2, 4, 6, 8, 10};
    assert(anyEven(arr4, 5) == true);
  }

  {
    int arr5[] = {0, 2, 4};
    assert(anyEven(arr5, 3) == true);
  }

  // Test single even element
  {
    int arr6[] = {8};
    assert(anyEven(arr6, 1) == true);
  }

  // Test arrays with no even numbers (all odd)
  {
    int arr7[] = {1, 3, 5, 7, 9};
    assert(anyEven(arr7, 5) == false);
  }

  {
    int arr8[] = {-1, -3, -5};
    assert(anyEven(arr8, 3) == false);
  }

  {
    int arr9[] = {11, 13, 15, 17, 19};
    assert(anyEven(arr9, 5) == false);
  }

  // Test single odd element
  {
    int arr10[] = {7};
    assert(anyEven(arr10, 1) == false);
  }

  // Test arrays with zero (zero is even)
  {
    int arr11[] = {1, 3, 0, 5, 7};
    assert(anyEven(arr11, 5) == true);
  }

  {
    int arr12[] = {0};
    assert(anyEven(arr12, 1) == true);
  }

  // Test mixed positive and negative numbers
  {
    int arr13[] = {-1, -3, -2, -5, -7};
    assert(anyEven(arr13, 5) == true);
  }

  {
    int arr14[] = {-1, -3, -5, -7, -9};
    assert(anyEven(arr14, 5) == false);
  }

  // Test larger arrays
  {
    int arr15[] = {101, 103, 105, 107, 109, 111, 112};
    assert(anyEven(arr15, 7) == true);
  }

  {
    int arr16[] = {101, 103, 105, 107, 109, 111, 113};
    assert(anyEven(arr16, 7) == false);
  }

  // Test edge case: empty array (should return false)
  {
    int *arr17 = nullptr;
    assert(anyEven(arr17, 0) == false);
  }

  // Test with negative even numbers
  {
    int arr18[] = {-1, -3, -4, -5};
    assert(anyEven(arr18, 4) == true);
  }

  std::cout << "\n\n[✓] All tests passed! Any even checker works correctly.\n";
  std::cout << "Function correctly checks if any element in array is even.\n";

  return 0;
}
