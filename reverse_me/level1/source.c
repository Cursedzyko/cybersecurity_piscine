#include <stdio.h>
#include <string.h>

int main()
{
    char str[20];
    char *exp = "__stack_check";
    printf("Please enter key: ");
    scanf("%s", str);

    if (strcmp( str, exp) == 0)
    {
        printf("Good job!\n");
    }
    else
    {
        printf("Nope.\n");
    }
    return 0;
}