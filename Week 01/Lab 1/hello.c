#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string user_name = get_string("Enter you name: ");
    // Saying hello
    printf("Hello, %s\n", user_name);
}