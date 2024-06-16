#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(int argc, string argv[])
{
int z = 0;
int lol = 0;
string s = argv[1];
if (argc == 2)
{
    for (int i=0; s[i]!='\0';i++)
{
    if (s[i]<48 || s[i]>57)
{
    z = z+1;
}
}
if (z>0)
{
    printf("Usage: ./caesar key\n");
    return 1;
}
else
        {
char c=0;
int n = strlen(s);
            for (int i=0; s[i]!=0;i++)
            {
                lol = lol + (s[i]-48)*pow(10,(n-1-i));
            }
         string plain = get_string("plaintext: ");
           printf("ciphertext: ");
            for (int i=0; plain[i] !=0 ;i++)
            {
                if (plain[i]>=65 & plain[i]<=90)
                {plain[i] = plain[i]-65 + lol;
                while (plain[i]>25)
                {
                    plain[i] = plain[i]-26;
                }
                    plain[i] = plain[i] + 65;
                }
                else if (plain[i]>=97 & plain[i]<=122)
                {plain[i] = plain[i]-97 + lol;
                while (plain[i]>25)
                {
                    plain[i] = plain[i]-26;
                }
                    plain [i]= plain[i]+97;
                }
                 printf("%c",plain[i]);
            }
       printf("\n");
        }
}
else
{
    printf("Usage: ./caesar key\n");
    return 1;
}

}