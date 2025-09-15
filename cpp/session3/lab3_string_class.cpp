#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <memory>

class MyString {
 private:
  char *string_data;
  size_t length;

 public:
  // Default constructor
  // write your solution here...
  MyString() {
    string_data = new char[1];
    string_data[0] = '\0';
    length = 0;
  }

  MyString(const char *str) {
    length = (str != nullptr)? strlen(str):0;
    string_data = new char[length + 1];
    if (length > 0) {
      strcpy(string_data, str);
    }
    string_data[length] = '\0';
  }
  MyString(const MyString& other) {
    string_data = new char[other.length];
    length = other.length;
    strcpy(string_data,other.string_data);
  }


  // Destructor
  ~MyString() {
    delete [] string_data;
    string_data = nullptr;
  }

  // Getters
  size_t getLength() const { return length; }
  const char *getString() const { return string_data; }

  // Indexing operator (const version)
  // uncomment and write your solution
  const char &operator[](size_t index) const {
      return string_data[index];
  }

  // Indexing operator (non-const version)
  // uncomment and write your solution
  char &operator[](size_t index) {
    return string_data[index];
  }

  // Equality operator
  bool operator==(const MyString &other) const {
    int res = strcmp(other.string_data, string_data);
    return (res == 0)? true: false;
  }

  // Inequality operator
  bool operator!=(const MyString &other) const {
    int res = strcmp(other.string_data, string_data);
    return (res != 0)? true: false;
  }
};

int main() {
  std::cout << "==============================================\n";
  std::cout << "       CUSTOM STRING CLASS TESTER\n";
  std::cout << "==============================================\n\n";

  // Test default constructor
  {
    MyString str1;
    assert(str1.getLength() == 0);
    assert(std::strcmp(str1.getString(), "") == 0);
    std::cout << "Default constructor test passed\n";
  }

  // Test constructor with C-string
  {
    MyString str2("Hello");
    assert(str2.getLength() == 5);
    assert(std::strcmp(str2.getString(), "Hello") == 0);
    std::cout << "C-string constructor test passed\n";
  }

  // Test length functionality
  {
    MyString str3("World!");
    assert(str3.getLength() == 6);
    std::cout << "Length: " << str3.getLength() << " characters\n";
  }

  // Test indexing operator (const)
  {
    const MyString str4("Testing");
    assert(str4[0] == 'T');
    assert(str4[1] == 'e');
    assert(str4[6] == 'g');
    std::cout << "Const indexing test passed\n";
  }

  // Test indexing operator (non-const)
  {
    MyString str5("Modify");
    str5[0] = 'X';
    str5[5] = 'Z';
    assert(str5[0] == 'X');
    assert(str5[5] == 'Z');
    std::cout << "Non-const indexing test passed\n";
    std::cout << "Modified string: " << str5.getString() << "\n";
  }

  // Test empty string
  {
    MyString str6("");
    assert(str6.getLength() == 0);
    std::cout << "Empty string test passed\n";
  }

  // Test equality operators
  {
    MyString str7("First");
    MyString str8("First");
    MyString str10("Different");

    assert(str7.getLength() == 5);
    assert(std::strcmp(str7.getString(), "First") == 0);
    assert(str7 == str8);
    assert(str7 != str10);
    std::cout << "Equality operators test passed\n";
  }

  // Test single character
  {
    MyString str7("A");
    assert(str7.getLength() == 1);
    assert(str7[0] == 'A');
    std::cout << "Single character test passed\n";
  }

  // Test null pointer handling
  {
    MyString str8(nullptr);
    assert(str8.getLength() == 0);
    assert(std::strcmp(str8.getString(), "") == 0);
    std::cout << "Null pointer handling test passed\n";
  }

  // Test character access and modification
  {
    MyString str9("12345");
    std::cout << "Original: " << str9.getString() << "\n";

    for (size_t i = 0; i < str9.getLength(); ++i) {
      std::cout << "str9[" << i << "] = " << str9[i] << "\n";
    }

    // Modify characters
    str9[0] = 'A';
    str9[4] = 'E';
    std::cout << "Modified: " << str9.getString() << "\n";
  }

  // Test special characters
  {
    MyString str11("Special!@#$%^&*()");
    assert(str11.getLength() == 17);
    std::cout << "Special characters test passed\n";
  }

  std::cout << "\n[✓] All tests passed! String class works correctly.\n";
  std::cout << "Class supports construction, length queries, and indexing.\n";

  return 0;
}
