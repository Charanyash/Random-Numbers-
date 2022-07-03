#include <stdio.h>

int main()
{
    FILE *fp1;
    FILE *fp2;
    FILE *fp3;
    int i = 0;
    fp1 = fopen("gau.dat", "r");
    fp2 = fopen("bern.dat", "r");
    fp3 = fopen("Y.dat", "w");
    double x = 0.0;
    double n = 0.0;
    int A = 5;
    for (i = 0; i < 1000000; i++)
    {
        fscanf(fp1, "%lf", &x);
        fscanf(fp2, "%lf", &n);
        fprintf(fp3, "%lf\n", A * x + n);
    }
    fclose(fp1);
    fclose(fp2);
    fclose(fp3);

    return 0;
}