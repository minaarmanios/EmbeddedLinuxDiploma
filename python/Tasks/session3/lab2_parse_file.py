"""File Parsing Problems - Testing student capability with file parsing and text processing."""

import os
import re

def parse_config_file(file_path):
    r"""
    parse template data from a file. and return a dictionary with the data.
    Example :
    {
        "SUMMARY": "hello python",
        "LICENSE": CLOSED,"
        "SRC_URI": "file://sd-hello.py", "
        "RDEPENDS:${PN}": "python3",
    }
    if you intend to use regex you can use this pattern
    pattern = r'^([A-Z_][A-Z0-9_:${}]*)\s*=\s*"([^"]*(?:\\[\s\S]*?)*)"'

    """
    res = {}
    regex_pattern = r'^([A-Z_][A-Z0-9_:${}]*)\s*=\s*"([^"]*(?:\\[\s\S]*?)*)"'
    try:
        with open(file_path,"r",encoding="utf-8") as f:
            file_data = f.readlines()
            for file_line in file_data:
                found_list = re.findall(regex_pattern,file_line)
                if found_list and isinstance(found_list[0],tuple) and len(found_list[0]) == 2:
                    res[found_list[0][0]] = found_list[0][1]
    except IOError:
        print("couldn't opem file to tread")
    return res

if __name__ == "__main__":
    # Get the path to the template_data.txt file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_file = os.path.join(current_dir, "template_data.txt")
    print("Testing parse_config_file...")
    result = parse_config_file(template_file)
    # Test assertions
    print("Checking SUMMARY...")
    assert "SUMMARY" in result, "SUMMARY key not found in result"
    assert result["SUMMARY"] == " hello python", f"Expected ' hello python', got {result['SUMMARY']}"

    print("Checking LICENSE...")
    assert "LICENSE" in result, "LICENSE key not found in result"
    assert result["LICENSE"] == "CLOSED", f"Expected 'CLOSED', got '{result['LICENSE']}'"

    print("Checking SRC_URI...")
    assert "SRC_URI" in result, "SRC_URI key not found in result"
    EXPECTED_SRC_URI = "file://sd-hello.py"
    assert result["SRC_URI"] == EXPECTED_SRC_URI, f"Expected {EXPECTED_SRC_URI}, got {result['SRC_URI']}"

    print("Checking S variable...")
    assert "S" in result, "S key not found in result"
    assert result["S"] == "${WORKDIR}", f"Expected '${{WORKDIR}}', got '{result['S']}'"

    print("Checking RDEPENDS...")
    assert "RDEPENDS:${PN}" in result, "RDEPENDS:${PN} key not found in result"
    assert result["RDEPENDS:${PN}"] == "python3 ", f"Expected 'python3 ', got '{result['RDEPENDS:${PN}']}'"

    # Check that function definitions and inherit statements are not included
    print("Checking that function definitions are excluded...")
    for _key in result:
        assert not _key.startswith("do_install"), "Function definition should not be parsed as a _key"
        assert _key != "inherit", "inherit statement should not be parsed as a key"

    # Verify expected number of keys
    print("Checking total number of parsed keys...")
    expected_keys = {"SUMMARY", "LICENSE", "SRC_URI", "S", "RDEPENDS:${PN}"}
    assert len(result) == len(expected_keys), f"Expected {len(expected_keys)} keys, got {len(result)}"
    assert set(result.keys()) == expected_keys, f"Expected keys {expected_keys}, got {set(result.keys())}"

    print("All tests passed!")
