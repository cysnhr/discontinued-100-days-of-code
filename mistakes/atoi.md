#### 20230409
dunno what's wrong.

```c
#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input, int len);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    // Checks if everything are integers
    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input, strlen(input)));
}

int convert(string input, int len)
{
    // Base case
    if (len == 0)
        return 0; // Stops program

    // Recursive case
    int digit = input[len] - '0';
    return convert(input, len - 1) * 10 + digit;

}
```
