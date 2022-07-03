#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"


int main(){

printf("Mean of the data : %lf\n",mean("gau.dat"));
printf("Variance of the data : %lf",variance("gau.dat"));
return 0;
}
