# Fundamentals in Programming

You can use this the navigate your way around and through fundamental programming concepts.

## Current Resources

![Harvard Programming Courses - CS50](https://www.youtube.com/channel/UCcabW7890RKJzL968QWEykA)


## Main Topics you will find here

### Abstraction

Abstraction is the representation of data, a dry way of saying how can we solve and think about problems

### functions

side effects, return values

```c
//prototype of a function
void PrintName(string name);

int main(void)
{
    printf("Your name: ");
    string s = GetString();
    PrintName(s);
}

void PrintName(string name)
{
    printf("hello, %s\n", name);
}
```

Also notice by initally declaring the function at the top of our program, your giving the compiler a litte 'breadcrumb' promising that you're going to make this function, _PrintName_, do something eventually.

### representation of information

* integer overflow and floats

## ASCII

Lets convert ASCII character witha C program:

```c
#include <stdio.h>
// Typecast an int to a char
int main(void){
for (int i = 65; i < 65 + 26; i++){
        printf("%c: %i\n", (char) i, i);
}
printf("\n");
for (int i = 97; i < 97 + 26; i++){
        printf("%c: %i\n", (char) i, i);
}}
```

```c
#include <stdio.h>
// Typecast a char to an int
int main(void){
for (int c = 'A'; c <= 'Z'; c++)
        printf("%c: %i\n", c , (int) c);
printf("\n");
for (int c = 'a'; c <= 'z'; c++)
        printf("%c: %i\n", c , (int) c);
}
```

### command-line arguments

> int main(int argc, string argv[])
