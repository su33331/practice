## 387. First Unique Character in a String
### 23問目
### [問題リンク](https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=ryq3bf2c)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        character_count = dict()
        for c in s:
            character_count[c] = character_count.get(c, 0) + 1

        for i in range(len(s)):
            if character_count[s[i]] == 1:
                return i
        return -1

###修正版
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        character_count = defaultdict(int)
        for letter in s:
            character_count[letter] += 1

        for i in range(len(s)):
            if character_count[s[i]] == 1:
                return i
        return -1

### 参考を見て書いた他方法
#26文字char配列を使う方法
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        count = [0] * 26
        for c in s:
            count[ord(c)-ord("a")] += 1
        for i in range(len(s)):
            if count[ord(s[i])] == 1:
                return i
        return -1

'''
参考にしたもの
* https://github.com/goto-untrapped/Arai60/pull/17/files
→ 26文字char配列を使う方法もある
* https://github.com/hayashi-ay/leetcode/pull/28/files
→ Counterを使った方法
→ ord()関数:文字をunicodeに変換してくれる。
#追加で知った情報
* defaultdict：初期値0で作れるdict.defaultlistもある.
'''
