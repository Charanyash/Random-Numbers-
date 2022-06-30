#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"
// void gaussian(char *str, int len)
// {
//     int i, j;
//     FILE *fp;
//     fp = fopen(str, "w");
//     double x;
//     for (i = 0; i < len; i++)
//     {
//         x = 0.0;
//         for (j = 0; j < 12; j++)
//         {
//             x = x + (double)rand()/RAND_MAX
//         }
//         x-=6;
//         fprintf(fp,"%lf\n",x);
//     }
// }

int main(void) // main function begins
{

    // Gaussian random numbers
    gaussian("gau.dat", 1000000);

    return 0;
}
