#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int main(){
   // Generating two gaussian distributions.
    gaussian("gau1.dat",1000000);

    gaussian("gau2.dat",1000000);

    return 0;
}