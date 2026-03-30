class Solution:
        def checkStrings(self, s1: str, s2: str) -> bool:
                # Separate characters by index parity
                        # s1[::2] gets all characters at indices 0, 2, 4...
                                # s1[1::2] gets all characters at indices 1, 3, 5...
                                        
                                                # We sort them to compare the character frequencies easily
                                                        return (sorted(s1[::2]) == sorted(s2[::2]) and 
                                                                        sorted(s1[1::2]) == sorted(s2[1::2]))