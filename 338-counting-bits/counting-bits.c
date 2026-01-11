#include <stdlib.h>

int* countBits(int n, int* returnSize) {
    *returnSize = n + 1;
    int* dp = (int*)malloc((n + 1) * sizeof(int));
    dp[0] = 0;
    
    for (int i = 1; i <= n; i++) {
        dp[i] = dp[i >> 1] + (i & 1);  // Right shift + LSB check
    }
    
    return dp;
}
