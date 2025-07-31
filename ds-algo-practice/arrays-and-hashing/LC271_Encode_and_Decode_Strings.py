class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encodedString = ""
        for w in strs:
            encodedString += w + "😂"
        return encodedString

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decodedStrings = []
        start = 0
        for i, c in enumerate(s):
            if c == '😂':
                decodedStrings.append(s[start:i])
                start = i+1
        return decodedStrings
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))