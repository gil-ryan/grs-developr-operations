# Dealing with Memory in RAM

## Examples of Overflow

In using differing types, it is important to acknowledge its memory properties, for examples:

```c
#include <stdio.h>
#include <unistd.h>
int main(void)
{
    for(int i = 1; i < 1000000000000  ;i *= 2){
        printf("%i\n", i*2 );
        sleep(1);}
}
```

## Important

There is a vast difference in the length of a string, versuse the amount of memory that it takes up. A string will be _n_ length, however, it will take up _n + 1_ bytes in memory.

### Null Character \0
