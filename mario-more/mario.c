#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n <= 0 || n >= 9);

    for (int i = 0; i < n; i++)
    {
        for (int a = 0; a < (n-(1+i)); a++)
        {
            printf(" ");
        }
        for (int s = 0; s < i+1 ; s++)
        {
            printf("#");
        }
            printf("  ");
        for (int d = 0; d < i+1; d++)
            {
            printf("#");
            }
    printf("\n");



}
}