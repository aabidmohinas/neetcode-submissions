class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == []: return 'Empty[&*&][&*&]'
        elif strs == [""]: return 'Empty_String[&*&][&*&]'
        else: return '[&*&]'.join(strs)

    def decode(self, s: str) -> List[str]:
        if '[&*&][&*&]' in s and s == 'Empty[&*&][&*&]': return []
        elif '[&*&][&*&]' in s and s == 'Empty_String[&*&][&*&]': return [""]
        else: return s.split('[&*&]')