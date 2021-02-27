// This program impliments matrix tiling to compute the product of two randomly populated N X N matrices, A and B.
// The tile size is H X H
// N and H are hardcoded
// The order of the for-loops is also hardcoded

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>


float A[2050][2050];
float B[2050][2050];
float C[2050][2050];

int main(){
  struct timeval start;
  struct timeval end;


  unsigned long long int total_time = 0; // formatter is %llu
  long double FLOPS = 0; // formatter is %Lf

  long double MFLOPS = 0;

  float N = 2050.0 ; // size of matrix, hardcoded
  int n = (int)N;

  float H =  41.0; // size of tile, hardcoded
  float h = (int)(H);

  // randomly populate arrays
  for (int i = 0; i < n; i ++){
      for (int j = 0; j < n; j ++){

        A[i][j] = (float)rand() ;
        B[i][j] =  (float)rand() ;

      }
  }



 // Cache warm up


 for (int ii = 0; ii < n/h ; ii++){
   for (int kk = 0; kk < n/h ; kk++){
     for (int jj = 0; jj < n/h ; jj++){

       for (int i = ii*h; i < (ii+1)*h ; i++){
         for (int k = kk*h; k < (kk+1)*h ; k++){
           for (int j = jj*h; j < (jj+1)*h ; j++){

             C[i][j] += A[i][k] * B[k][j];

           }
         }
       }
     }
   }
 }


  // Second run. Measure time taken.

  gettimeofday(&start, NULL);



 for (int ii = 0; ii < n/h ; ii++){
   for (int kk = 0; kk < n/h ; kk++){
     for (int jj = 0; jj < n/h ; jj++){

       for (int i = ii*h; i < (ii+1)*h ; i++){
         for (int k = kk*h; k < (kk+1)*h ; k++){
           for (int j = jj*h; j < (jj+1)*h ; j++){

             C[i][j] += A[i][k] * B[k][j];

           }
         }
       }
     }
   }
 }

  gettimeofday(&end, NULL);

  total_time = (end.tv_sec * 1000000 + end.tv_usec)
      - (start.tv_sec * 1000000 + start.tv_usec); // time in microseconds,  1 microsecond = 10^(-6) seconds

  double total_time_as_double = (double)total_time;

  FLOPS = ( 2*N*N*N / total_time_as_double ) * 1000000 ;    //  (2*N^3) / t,  converting back to seconds.

  MFLOPS = FLOPS / 1000000;

  printf("Array size: %f \n", N );
  printf("Subarray size: %f \n", H);
  printf("time taken (in microseconds): %lf \n", total_time_as_double );
  printf("MFLOPS = %Lf \n", MFLOPS );



} // ends main
