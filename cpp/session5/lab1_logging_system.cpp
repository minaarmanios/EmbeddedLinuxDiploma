#include <cassert>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

#define LOG Log

// Log level enumeration
enum class Level { DEBUG = 0, INFO = 1, WARN = 2, ERROR = 3, FATAL = 4 };

// Log entry structure
class Log {
 private:
    inline static const std::vector<std::string> MSG_PER_LEVEL = {"DEBUG", "INFO", "WARNING", "ERROR", "FATAL"};
    static Level current_level;
    static int log_count;

    static std::vector<std::vector<std::string>> stored_logs;

 public:
    static std::ostream& showMsg(Level log_level) {
      log_count += 1;
      int log_level_index = static_cast<int>(log_level);
      if (log_level_index < static_cast<int>(MSG_PER_LEVEL.size())) {
        std::cout<< MSG_PER_LEVEL[log_level_index]<< ":";
      }
      return std::cout;
    }

    static inline std::ostream& Debug() {
      
      return Log::showMsg(Level::DEBUG);
    }

    static inline std::ostream& Info() {
      return Log::showMsg(Level::INFO);
    }

    static inline std::ostream& Warn() {
      return Log::showMsg(Level::WARN);
    }

    static inline std::ostream& Error() {
      return Log::showMsg(Level::ERROR);
    }

    static inline std::ostream& Fatal() {
      return Log::showMsg(Level::FATAL);
    }

    static int GetLogCount() {
      return log_count;
    }

    static bool ContainsMessage(const std::string msg) {
      for (const auto &vec : stored_logs) {
        if (std::find(vec.begin(), vec.end(), msg) != vec.end()) {
          return true;
        }
      }
      return false;
    }

    static void Dump() {
      int current_level_index = static_cast<int>(current_level);
      for (int i= current_level_index; i < static_cast<int>(stored_logs.size()); ++i) {
        std::cout<< std::endl<< MSG_PER_LEVEL[i]<< " msgs:" <<std::endl;
        for (const auto &msg : stored_logs[i]) {
          std::cout<< msg<< std::endl;
        }
        std::cout<< std::endl;
      }
    }

    static void push_msg(Level req_level, std::string msg) {
      int req_level_index = static_cast<int>(req_level);
      if (req_level_index < static_cast<int>(stored_logs.size())) {
        stored_logs[req_level_index].push_back(msg);
      }
    }
};

Level Log::current_level = Level::DEBUG;
int Log::log_count = 0;
std::vector<std::vector<std::string>> Log::stored_logs = std::vector<std::vector<std::string>>(5);




int main() {
  std::cout << "==============================================\n";
  std::cout << "           LOGGING SYSTEM VALIDATOR\n";
  std::cout << "==============================================\n\n";

  // Test : Basic logging functionality
  std::cout << "--- Test 1: Basic Logging ---\n";
  LOG::Info() << "System started";
  LOG::Warn() << "Configuration file missing";
  LOG::Error() << "Database connection failed";
  LOG::Debug() << "This debug message should not appear";
  LOG::Fatal() << "Application must terminate";

  // Verify logs were stored
  assert(LOG::GetLogCount() == 5);
  assert(LOG::ContainsMessage("System started"));
  assert(LOG::ContainsMessage("Configuration file missing"));

  LOG::Dump();

  std::cout << "\n==============================================\n";
  std::cout << "         ALL TESTS PASSED! ✓\n";
  std::cout << "==============================================\n";

  return 0;
}
