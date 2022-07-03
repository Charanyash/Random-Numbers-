#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int main(){
    //Generating chi-squared distribution for k = 2.
    chi_square("chi.dat","gau1.dat","gau2.dat",1000000);

    return 0;
}