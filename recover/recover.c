#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
 if (argc != 2)
 {
    printf("Usage: ./recover IMAGE\n");
    return 1;
 }
   FILE *file = fopen(argv[1], "r");

   int i = -1;

   typedef uint8_t BYTE;

   BYTE buffer[512];

   char *s = malloc(8);

   sprintf(s , "%03i.jpg" , i);

   FILE *huh = fopen(s , "w");

   while (fread(&buffer, 512 , 1 ,file) == 1)

   {

      if (buffer[0] == 0xff & buffer[1] == 0xd8 & buffer[2] == 0xff & (buffer[3] & 0xf0) == 0xe0)
      {


         fclose(huh);
         i++;
         sprintf(s , "%03i.jpg" , i);
         huh = fopen(s , "w");
      }

      fwrite(&buffer,512,1,huh);
   }

   free(s);
   fclose(huh);
   fclose(file);
}