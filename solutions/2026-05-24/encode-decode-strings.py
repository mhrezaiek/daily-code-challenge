"""Encode and Decode Strings.

Serialize a list of arbitrary strings into a single string and recover it
losslessly. Each chunk is prefixed by its length and a delimiter so the decoder
can read exactly that many characters and skip ahead.
"""

from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        # Time: O(total length), Space: O(total length)
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        # Time: O(total length), Space: O(total length)
        out: List[str] = []
        i = 0
        n = len(s)
        while i < n:
            j = s.index("#", i)
            length = int(s[i:j])
            start = j + 1
            end = start + length
            out.append(s[start:end])
            i = end
        return out


def _tests() -> None:
    c = Codec()
    assert c.decode(c.encode([])) == []
    assert c.decode(c.encode([""])) == [""]
    assert c.decode(c.encode(["", "", ""])) == ["", "", ""]
    assert c.decode(c.encode(["hello", "world"])) == ["hello", "world"]
    assert c.decode(c.encode(["a#b", "c#d#e", ""])) == ["a#b", "c#d#e", ""]
    assert c.decode(c.encode(["12", "345", "6789"])) == ["12", "345", "6789"]
    unicode_inputs = ["café", "你好", ""]
    assert c.decode(c.encode(unicode_inputs)) == unicode_inputs


if __name__ == "__main__":
    _tests()
