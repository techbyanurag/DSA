#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool is_vowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int maxVowels(char *s, int k) {
    int n = strlen(s);
    if (n < k) return 0;
    
    int current = 0;
    for (int i = 0; i < k; ++i) {
        if (is_vowel(s[i])) ++current;
    }
    int max_count = current;
    
    for (int i = k; i < n; ++i) {
        if (is_vowel(s[i])) ++current;
        if (is_vowel(s[i - k])) --current;
        if (current > max_count) max_count = current;
    }
    return max_count;
}
