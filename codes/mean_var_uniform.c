#include <stdio.h>

int main(){

int count = 0;
  FILE *fp;
  double x, sum = 0.0;
  fp = fopen("uni.dat", "r");
  double square = 0;
  double mean;
  double variance;
  // get numbers from file
  while (fscanf(fp, "%lf", &x) != EOF)
  {
    // Count numbers in file
    count = count + 1;
    // Add all numbers in file
    sum = sum + x;

    // Adding the squares of numbers
    square =  square + x*x;
}
  fclose(fp);

  mean = sum /count;
  variance = square/count - mean*mean;
  
  printf("The mean is %lf, variance is %lf\n",mean,variance);

return 0;
}
