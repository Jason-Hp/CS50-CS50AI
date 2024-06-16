#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string s);
int count_sentences(string s);

int main(void)
{
string text = get_string("Text: ");
float L = ((float)count_letters(text)/(float)count_words(text)*100.0);
float S = ((float)count_sentences(text)/(float)count_words(text)*100.0);

int index = round(0.0588 * L - 0.296 * S - 15.8);

if (index < 1)
{
    printf("Before Grade 1\n");
}
else if (index >= 16)
{
    printf("Grade 16+\n");
}
else
{
    printf("Grade %i\n",index);
}
}

int count_letters(string text)
{
int x = 0;
for (int i=0;text[i] != 0;i++)
{
    if (text[i]>=65 & text[i]<=90 || text[i]>=97 & text[i]<=122)
    {
        x++;
    }
}
return x;
}

int count_words(string s)
{
int c = 0;
for (int i = 0;s[i] !=0;i++)
{
    if (s[i] == 32)
    c++;
}
c = c + 1;
return c;
}

int count_sentences(string s)
{
int z = 0;
for (int i=0;s[i] != 0;i++)
{
    if (s[i] == 33 || s[i] == 46 || s[i] == 63)
    {
        z++;
    }
}
return z;
}