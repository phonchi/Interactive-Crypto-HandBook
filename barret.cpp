

#include <iostream>
#include "big.h"
using namespace std;
Miracl precision(400,10);

Big barret_setup (Big b)
{
  Big     x;
  x = pow((Big)2, 2*bits(b));
  x = x/b;
  return x;
}

Big barret_reduction (Big x, Big m, Big mu)
{
  Big  q, b, temp, zero;
  int ix, iq;
  temp = 1;
  /* q = x */
  q = x;
  q = q >> (bits(m)-1);
  q = mu * q;
  q = q >> (bits(m)+1);
  temp = pow((Big)2, bits(m)+1);
  x = x % temp;
  cout << "x="<< x << endl;

  q =q * m;
  temp = pow((Big)2, bits(m)+1);
  q = q % temp;
  cout << "q=" << q << endl <<"m=" << m << endl;
  x = x - q;
  if (x < 0) {
    b = pow((Big)2, bits(m)+1);
    x = x + b;
    cout << "b=" << b << endl;
  }
  while (x > m)  x = x - m; 
  cout << "x=" << x << endl;

  return x;
}
int  main()
{
    Big a,b,c,mu;
   /*  initialize  a,b  to  desired  values,  mp_init  mu, c  and  set  c  to  1...we  want  to  compute  a^3  mod  b   */
    a = 1601613;
    b = 201;
    /*  get  mu  value  */
    mu = barret_setup(b);
    /*  now  reduce a modulo b */
    c = barret_reduction (a, b, mu);
    cout << "number = " << c << endl;
    
    return  1;
}