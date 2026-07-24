class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = [0] * 26
        window = [0] * 26
        window_size = len(s1)

        for char in s1:
            target[ord(char) - ord("a")] += 1

        for right, char in enumerate(s2):
            window[ord(char) - ord("a")] += 1

            # Keep the window size equal to len(s1).
            if right >= window_size:
                left_char = s2[right - window_size]
                window[ord(left_char) - ord("a")] -= 1

            if window == target:
                return True

        return False