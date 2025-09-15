"""Dictionary Problems - Testing student capability with dictionary operations."""


def dictionary_operations(dict1:dict, dict2):
    """Perform basic operations on two dictionaries.

    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: Dictionary with merged, common_keys, and unique_keys
    """
    # Write your solution here
    res = {}
    if isinstance(dict1,dict) and isinstance(dict2,dict):
        res["merged"] = dict1 | dict2
        res["common_keys"] = set(dict1.keys() & dict2.keys())
        res["unique_keys"] =  set(res["merged"]).difference(res["common_keys"])
    elif isinstance(dict1,dict):
        res["merged"] = dict1
        res["common_keys"] = dict1
        res["unique_keys"] = dict1
    elif isinstance(dict2,dict):
        res["merged"] = dict2
        res["common_keys"] = dict2
        res["unique_keys"] = dict2
    return res

def count_word_frequency(text):
    """Count the frequency of each word in a text string.

    Args:
        text (str): Input text

    Returns:
        dict: Dictionary with word frequencies
    """
    # Write your solution here
    res = {}
    if isinstance(text,str):
        words = text.split(" ")
        for word in words:
            res.setdefault(word,0)
            res[word] += 1
    return res


def dictionary_filtering(students_grades):
    """Filter students based on their grades.

    Args:
        students_grades (dict): Dictionary with student names as keys and grades as values

    Returns:
        dict: Dictionary with students who have grades >= 70
    """
    # Write your solution here
    res = {}
    if isinstance(students_grades,dict):
        res = dict(filter(lambda x:x[1] >= 70, students_grades.items()))
    return res

def nested_dictionary_access(nested_dict, keys_path):
    """Access value in nested dictionary using a list of keys.

    Args:
        nested_dict (dict): Nested dictionary
        keys_path (list): List of keys to traverse

    Returns:
        any: Value at the specified path, or None if path doesn't exist
    """
    # Write your solution here
    selected_value = None
    if isinstance(nested_dict,dict) and len(keys_path) > 0:
        selected_value = nested_dict
        for key_path in keys_path:
            selected_value = selected_value.get(key_path,None)
            if not selected_value:
                break
    return selected_value

if __name__ == "__main__":
    # Test cases
    print("Testing dictionary_operations...")
    result = dictionary_operations({"a": 1, "b": 2}, {"b": 3, "c": 4})
    expected = {"merged": {"a": 1, "b": 3, "c": 4}, "common_keys": {"b"}, "unique_keys": {"a", "c"}}
    assert result == expected, f"Expected {expected}, got {result}"
    assert result["merged"] == {"a": 1, "b": 3, "c": 4}, "Merged dictionary incorrect"
    assert result["common_keys"] == {"b"}, "Common keys incorrect"
    assert result["unique_keys"] == {"a", "c"}, "Unique keys incorrect"

    print("Testing count_word_frequency...")
    result = count_word_frequency("hello world hello python world")
    expected = {"hello": 2, "world": 2, "python": 1}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Testing dictionary_filtering...")
    result = dictionary_filtering({"Alice": 85, "Bob": 65, "Charlie": 90, "Diana": 45})
    expected = {"Alice": 85, "Charlie": 90}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Testing nested_dictionary_access...")
    nested = {"level1": {"level2": {"level3": "found"}}}
    result = nested_dictionary_access(nested, ["level1", "level2", "level3"])
    assert result == "found", f"Expected 'found', got {result}"

    result = nested_dictionary_access(nested, ["level1", "nonexistent"])
    assert result is None, f"Expected None, got {result}"

    print("All tests passed!")
