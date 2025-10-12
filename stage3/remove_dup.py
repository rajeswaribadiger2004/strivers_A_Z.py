from typing import List

class Solution:
    def remove_dup(self,arr:List[int])->int:
        i=0
        for j in range(1,len(arr)):
            if arr[i]!=arr[j]:
                i+=1
                arr[i]=arr[j]
        return i+1
        
        
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = sol.remove_dup(arr)
    print("The array after removing duplicate elements is:")
    for i in range(k):
        print(arr[i], end=" ")

// fibonacci_iterative.c
#include <stdio.h>



int main(void) {
    int n;
    if (scanf("%d", &n) != 1) return 0;

    if (n <= 0) {
        printf("0\n");
        return 0;
    }
    if (n == 1) {
        printf("0\n");
        return 0;
    }

    long long a = 0, b = 1, c;
    // prints nth Fibonacci number where F0 = 0, F1 = 1
    for (int i = 2; i <= n; ++i) {
        c = a + b;
        a = b;
        b = c;
    }
    printf("%lld\n", (n == 0) ? a : b);
    return 0;
}

