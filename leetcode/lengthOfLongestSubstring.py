def lengthOfLongestSubstring(s: str) -> int:
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
    :type s: str
    :rtype: int
    """
    temp_array: list[str] = []
    current_length: int = 0
    max_length: int = 0
    for i in s:
        if i not in temp_array:
            temp_array.append(i)
            current_length += 1
        else:
            if max_length < current_length:
                max_length = current_length
            temp_array = []
            current_length = 0
    return max_length


if __name__ == "__main__":
    case1: str = "abcabcbb"
    print(lengthOfLongestSubstring(case1))

    case2: str = "pwwkew"
    print(lengthOfLongestSubstring(case2))
