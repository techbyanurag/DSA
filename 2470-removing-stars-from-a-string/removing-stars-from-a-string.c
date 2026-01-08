char* removeStars(char* s) {
    int j = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] != '*') {
            s[j++] = s[i];
        } else {
            j--;
        }
    }
    s[j] = '\0';
    return s;
}
