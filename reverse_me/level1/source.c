#include <stdio.h>
#include <string.h>

int main()
{
    char str[100];
    printf("Please enter key: ");
    scanf("%s", str);

    if (strcmp( str, "__stack_check") == 0)
    {
        printf("Good job!\n");
    }
    else
    {
        printf("Nope.\n");
    }
    return 0;
}