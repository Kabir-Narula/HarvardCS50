#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// Creating a BYTE type to read files
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check for invalid usage
    if (argc < 1)
    {
        printf("Usage: recover [card...]\n");
        return 1;
    }

    // Reading the memory card
    FILE *file = fopen(argv[1], "r");

    // Checking for errors
    if (file == NULL)
    {
        printf("Could not open file..");
        return 1;
    }

    // Read 512 bytes into buffer
    BYTE bytes[512];
    fread(bytes, sizeof(BYTE), 512, file);

    int counter = 0; // Keeps track of images
    FILE *img = NULL; // Declaring file pointer
    while (fread(bytes, sizeof(BYTE), 512, file) > 0)
    {
        // Checking for jpeg
        if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff && (bytes[3] & 0xf0) == 0xe0)
        {
            if (!(counter == 0)) // If file is already opened
            {
                fclose(img);
            }

            // opening a file to write to it
            sprintf(argv[1], "%03i.jpg", counter);
            img = fopen(argv[1], "w");
            counter++;
        }

        if (!(counter == 0))
        {
            // Writing into an opened file
            fwrite(bytes, 512, 1, img);
        }
    }
    return 0;
}