#include <cs50.h>
#include <stdio.h>


long bro(long z);


int main(void)
{
long x;


        x = get_long("number: ");

    if (x<4000000000000||x>4999999999999&x<340000000000000||x>379999999999999&x<4000000000000000||x>4999999999999999&x<5100000000000000||x>5599999999999999 )
    {
    printf("INVALID\n");
    
}
        //VISA13
        if (x>3999999999999&x<5000000000000)
        {
            int visa13 = bro(x);
            if (visa13%10==0)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }

        //AMEX
          if (x>339999999999999&x<350000000000000)
        {
            int amex = bro(x);
                if (amex%10 == 0)
                {
                    printf("AMEX\n");
                }
                    else
                {
            printf("INVALID\n");
                }
        }
        //AMEX 2
          if (x>369999999999999&x<380000000000000)
        {
            int amex2 = bro(x);
                if (amex2%10 == 0)
                {
                    printf("AMEX\n");
                }
                    else
                {
            printf("INVALID\n");
                }
        }
        //AMEX REJ
        if (x>349999999999999&x<370000000000000)
       {
        printf("INVALID\n");
       }
        // MASTERCARD
            if (x>5099999999999999&x<5600000000000000)
            {
                int mastercard = bro(x);
                    if (mastercard%10==0)
                    {
                        printf("MASTERCARD\n");
                    }
                       else
                    {
            printf("INVALID\n");
                    }
            }
        // VISA16
            if (x>3999999999999999&x<5000000000000000)
            {
                int visa16 = bro(x);
                    if (visa16%10==0)
                    {
                        printf("VISA\n");
                    }

            else
                   {
            printf("INVALID\n");
            }
            }
}

long bro(long z)
{
    long y;
    long a;
    long b;
    long c;
    long d;
    long e;
    long f;
    long g;
    long h;
    long s;




    y = (z/100000000000000%10+z/1000000000000%10+z/10000000000%10+z/100000000%10+z/1000000%10+z/10000%10+z/100%10+z%10);

        if (z/1000000000000000%10*2>=10)
            {
            a = (z/1000000000000000%10*2%10+1);
            }
            else
            {
                 a = (z/1000000000000000%10*2);
            }
        if (z/10000000000000%10*2>=10)
        {
            b = (z/10000000000000%10*2%10+1);
        }
        else
        {
             b = (z/10000000000000%10*2);
        }
        if (z/100000000000%10*2>=10)
        {
             c =(z/100000000000%10*2%10 + 1);
        }
        else
        {
            c=(z/100000000000%10*2);

          }  if (z/1000000000%10*2>=10)
           {
            d=(z/1000000000%10*2%10 + 1);
           }
           else
           {
            d= (z/1000000000%10*2);
           }
        if (z/10000000%10*2>=10)
        {
           e=(z/10000000%10*2%10 + 1);
        }
        else
        {
            e = (z/10000000%10*2);
        }
        if (z/100000%10*2>=10)
        {
            f = (z/100000%10*2%10 + 1);
        }
        else
        {
            f=(z/100000%10*2);
        }
        if (z/1000%10*2>=10)
        {
           g =  (z/1000%10*2%10 + 1 );
        }
        else
        {
            g =  (z/1000%10*2);
        }
        if (z/10%10*2>=10)
        {
            h = (z/10%10*2%10 + 1 );
        }
        else
        {
             h = (z/10%10*2);
        }
           s = y+a+b+c+d+e+f+h+g;

           return s;

}
