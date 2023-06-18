/ Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;
typedef uint8_t BYTE1;
typedef int16_t BYTE2;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file
    BYTE1 header[HEADER_SIZE];
    fread(&header, sizeof(header), 1, input);  // no loops used as there is only one header
    fwrite(&header, sizeof(header), 1, output);

    // TODO: Read samples from input file and write updated data to output file
    BYTE2 buffer;
    while (fread(&buffer, sizeof(BYTE2), 1, input))
    {
        buffer *= factor;
        fwrite(&buffer, sizeof(BYTE2), 1, output);
    }

    // Close files
    fclose(input);
    fclose(output);
}