#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Calculating the average of all colors
            float average = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0;
            image[i][j].rgbtBlue = round(average);
            image[i][j].rgbtGreen = round(average);
            image[i][j].rgbtRed = round(average);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Using the formula to calculate values
            float sepiaRed = 0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue;
            float sepiaGreen = 0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue;
            float sepiaBlue = 0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue;

            // Checking whether any color is fully present
            if (sepiaRed > 255)
            {
                sepiaRed = 255;

            }

            if (sepiaGreen  > 255)
            {
                sepiaGreen  = 255;

            }


            if (sepiaBlue  > 255)
            {
                sepiaBlue  = 255;

            }

            image[i][j].rgbtRed = round(sepiaRed);
            image[i][j].rgbtGreen = round(sepiaGreen);
            image[i][j].rgbtBlue = round(sepiaBlue);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int tmp[3];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Swapping the first and last elements
            tmp[0] = image[i][j].rgbtRed;
            image[i][j].rgbtRed = image[i][width - j - 1].rgbtRed;
            image[i][width - j - 1].rgbtRed = tmp[0];

            tmp[1] = image[i][j].rgbtGreen;
            image[i][j].rgbtGreen = image[i][width - j - 1].rgbtGreen;
            image[i][width - j - 1].rgbtGreen = tmp[1];

            tmp[2] = image[i][j].rgbtBlue;
            image[i][j].rgbtBlue = image[i][width - j - 1].rgbtBlue;
            image[i][width - j - 1].rgbtBlue = tmp[2];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Creating a copy image
    RGBTRIPLE copyImage[height][width];

    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            int red = 0;
            int green = 0;
            int blue = 0;
            float count = 0.00;

            // Taking the 3x3 box into consideration
            for (int a = -1; a <= 1; a++)
            {
                for (int b = -1; b <= 1; b++)
                {
                    if (x + a < 0 || x + a > height - 1 || y + b < 0 || y + b > width - 1)
                    {
                        continue;
                    }

                    red += image[x + a][y + b].rgbtRed;
                    green += image[x + a][y + b].rgbtGreen;
                    blue += image[x + a][y + b].rgbtBlue;
                    count++;
                }
            }

            // Assigning values
            copyImage[x][y].rgbtRed = round(red / count);
            copyImage[x][y].rgbtGreen = round(green / count);
            copyImage[x][y].rgbtBlue = round(blue / count);
        }
    }

    // Loading the changes into the original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = copyImage[i][j].rgbtRed;
            image[i][j].rgbtGreen = copyImage[i][j].rgbtGreen;
            image[i][j].rgbtBlue = copyImage[i][j].rgbtBlue;
        }
    }

    return;
}
