def lengthOfLongestSubstring(s: str) -> int:
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
    :type s: str
    :rtype: int
    """
    rtype: int = 0
    for i in range(0, len(s) - 1):
        temp_array: list[str] = []
        current_length: int = 0
        j: int = i
        while len(temp_array) == len(set(temp_array)):
            if j > len(s) - 1:
                break
            if len(temp_array) == 0:
                current_length -= 1
            print("index is ", j, ": ", s[j])
            temp_array.append(s[j])
            j += 1
            current_length += 1
        print(temp_array, set(temp_array), current_length)
        if rtype < current_length:
            rtype = current_length
            print("rtype is ", rtype)
    return rtype


if __name__ == "__main__":
    case1: str = "abcabcbb"
    print(lengthOfLongestSubstring(case1))

    case2: str = "pwwkew"
    print(lengthOfLongestSubstring(case2))

    case3: str = "bbbbb"
    print(lengthOfLongestSubstring(case3))
