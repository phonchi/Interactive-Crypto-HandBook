
#include <iostream>
#include "big.h"
using namespace std;
Miracl precision(400,10);


const int _CUTOFF = 1536;

Big karatsuba_mul (Big x, Big y)
{
  Big  mask, xlow, ylow, xhigh, yhigh, a, b, c, d;
  int n, half;
  // Base case
  if ( bits(x) <= _CUTOFF || bits(y) <= _CUTOFF)  return x * y ;
  else {
        n = max(bits(x), bits(y));
        half = (n + 32) / 64 * 32 ;
        mask = Big((1 << half) - 1);
        xlow = land(x, mask);
        ylow = land(y, mask);
        xhigh = x >> half;
        yhigh = y >> half;

        a = karatsuba_mul(xhigh, yhigh);
        b = karatsuba_mul(xlow + xhigh, ylow + yhigh);
        c = karatsuba_mul(xlow, ylow);
        d = b - a - c;
        return (((a << half) + d) << half) + c;
  }
  
}
int  main()
{
    Big a,b,c;
    miracl *mip=&precision;
    char aa[100]="87609798870979228866001198790ACDFFFFEEEE756868ABAABB564312345678";
    char bb[100]="AAAA1122907567841367868987091789876582228769815290789878AAA7DCAC";
    mip->IOBASE=16;
    a = aa;
    b = bb;
    c = karatsuba_mul (a, b);
    cout << "number = " << c << endl;  
    return  1;
}