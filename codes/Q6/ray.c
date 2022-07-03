#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"


int main(){

    // Generating random numbers of Rayleigh distribution.
    Rayleigh("ray.dat","gau1.dat","gau2.dat",1000000);

    return 0;
}