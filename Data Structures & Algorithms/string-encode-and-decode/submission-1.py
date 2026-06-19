class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + r"#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1

            length = int(s[i:j])
            start_string = j + 1
            end_string = start_string + length
            
            decoded.append(s[start_string:end_string])
            
            i = end_string

        return decoded