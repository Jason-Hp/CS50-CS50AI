#include "helpers.h"
#include<math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i=0; i < height; i++)
    {
        for (int j=0; j < width; j++)
        {
            int x = 0;
            x = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed)/3.0);

            image[i][j].rgbtBlue = x;

            image[i][j].rgbtGreen = x;

            image[i][j].rgbtRed = x;
        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{

RGBTRIPLE temp[height][width];
for (int x =0; x<height; x++)
{
    for (int l =0; l<width;l++)
    {
        temp[x][l] = image[x][l];
    }
}
    for (int i = 0 ;i<height ; i++)
    {
        for (int j = 0; j<width; j++)
        {
            float red;
            float blue;
            float green;


            red = round(0.393 * temp[i][j].rgbtRed + 0.769 * temp[i][j].rgbtGreen + 0.189 * temp[i][j].rgbtBlue);
            green =round(0.349 * temp[i][j].rgbtRed + 0.686 * temp[i][j].rgbtGreen + 0.168 * temp[i][j].rgbtBlue);
            blue =  round(0.272 * temp[i][j].rgbtRed + 0.534 * temp[i][j].rgbtGreen + 0.131 * temp[i][j].rgbtBlue);

            if (red>255)
            {
                red = 255;
            }
            if (green>255)
            {
                green = 255;
            }
            if (blue>255)
            {
                blue = 255;
            }
            image[i][j].rgbtRed = red;
            image[i][j].rgbtGreen = green;
            image[i][j].rgbtBlue = blue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
   for (int i=0; i < height; i++)
    {
        for (int j=0; j < (width / 2) ; j++)
        {
         RGBTRIPLE HAHA;
           // Storing colours
            HAHA = image[i][j];

            // swapping colours

            image[i][j] = image[i][width-1-j];
            image[i][width-1-j] = HAHA;

        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    RGBTRIPLE temp[height][width];
for (int x =0; x<height; x++)
{
    for (int l =0; l<width;l++)
    {
        temp[x][l] = image[x][l];
    }
}

    for (int i = 0; i < height; i++)
    {

        for (int j = 0; j < width; j++)
        {

            float sred =0;
            float sblue =0;
            float sgreen =0;
            int counter = 0;


            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {

                    if (i + k >= 0 & i + k <= (height-1) & j + l >=0 & j + l <= (width-1))
                    {
                    sred = sred+temp[i + k][j + l].rgbtRed;
                    sblue = sblue+temp[i + k][j + l].rgbtBlue;
                    sgreen = sgreen+temp[i + k][j + l].rgbtGreen;
                    counter = counter + 1;
                    }
                }
            }

            image[i][j].rgbtRed = round(sred /counter);
            image[i][j].rgbtGreen = round(sgreen/ counter);
            image[i][j].rgbtBlue = round(sblue /counter);
        }
    }
    return;
}
