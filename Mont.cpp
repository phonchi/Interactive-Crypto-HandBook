#include <iostream>
#include "big.h"
#include "zzn.h"
#include <math.h>

using namespace std;

Miracl precision(400,10);

Big bitvar(Big a, int base, int inradix ){
   Big x, temp;
   int i;
   x = 0;
   temp = 1;
   for (i=0; i < inradix; i++){
        x = x + bit(a,base+i)*temp;
        temp = temp *2;     
    }
   return x;
}    
   

Big mont_setup (Big p, int radix)
{
  Big     x, temp;
  temp = pow((Big)2, radix);
  x = inverse(p, temp);//p^-1 mod 2
  x = (temp-x)%temp;
  return x;
}

Big mont_full (Big a, Big b, Big p, Big p_p)
{
    Big c, q, temp;
    temp = pow((Big)2, bits(p));
    c = a*b;
    q = ((c % temp) * p_p) % temp;
    c = (c+q*p)/temp;
    if(c>=p)  c = c -p;
    return c;
}


Big mont_mul (Big a, Big b, Big p, Big p_p, int inradix)
{
  Big  q, temp, c;
  int i, iter;
  temp = 0;
  c = 0;
  temp = pow((Big)2, inradix);
  if(bits(p)%2==0)  iter = bits(p)/inradix;
  else      iter = (bits(p)/inradix)+1;

  for (i=0; i< iter; i++){
    // method 1
        q = ((bitvar(c,0,inradix)+bitvar(a,i*inradix,inradix)*bitvar(b,0,inradix))*p_p) % temp;
 //       for(int j = inradix-1; j>=0; j--)
 //           cout<<bit(c,j);
 //       cout << endl;
         c = c+bitvar(a,i*inradix,inradix)*b+q*p;
  //      cout << "c=" << c << endl;
  //      for(int j =inradix-1; j>=0; j--)
  //          cout<<bit(c,j);
  //      cout << endl;
        c = c /temp;
        
        /*
       // method 2
         c = c + bit(a,i)*b;
         q = inverse(bit(p,0), 2);
         q = (bit(c,0)*q)%2;
         
         //cout << "q=" << q << endl;
         c = c+q*p;
         c = c/2;
      */ 
      /*
      // method 3
         c = c + bit(a,i)*b;
         if(bit(c,0)==1){
            c = c + p;
        }
         c=c/2;
        */
  }
 /* Back off if it's too big */
  if (c >= p) {
    c = c - p;
  }
  //cout << "c=" << c << endl;

  return c;
}
  

int  main()
{
    Big a, b, c, p, mu, ina, inb, outc, temp, test;
    ZZn na, nb, nc;
    int radix, inradix;
    a = 155;
    b = 174;
    p = 201;
    temp = pow((Big)2, 2*bits(p));
    temp = temp % 201;
        
    inradix = 0;
    radix = 16;// 2^4
    while (radix > 1){
        inradix = inradix+1;
        radix = radix/2;
    }
    /*  get  mu  value  */
    mu = mont_setup(bitvar(p,0,inradix), inradix);
    cout << "mu=" << mu <<endl;
        
    // using radix2
    ina = mont_mul(a, temp, p, mu, inradix);
    inb = mont_mul(b, temp, p, mu, inradix);
    cout << "ina=" << ina << endl;
    cout << "inb=" << inb << endl;
    outc =  mont_mul(ina, inb, p, mu, inradix);
    cout << "outc=" << outc << endl;
    /*  now  reduce a modulo b */
    c = mont_mul (outc,(Big)1, p, mu, inradix);
    cout << "number = " << c << endl;
    
    // using full word, no radix   
    temp = pow((Big)2, 16);
      
    mu = mont_setup(p, bits(p));
    cout << "mu2=" << mu <<endl;
       
    temp = temp % 201;
    ina = mont_full(a, temp, p, mu);
    inb = mont_full(b, temp, p, mu);
    outc = mont_full(ina, inb, p, mu);
    cout <<"ina=" << ina << endl;
    cout <<"inb=" << inb << endl;
    cout <<"outc=" << outc << endl;
    c = mont_full(outc, (Big)1, p, mu);
    cout << "number2 = " << c << endl;
      
    // Using built-in montgomery multiplication
    modulo(p);
    //prepare_monty((Big)201);
    na = a;
    nb = b;
    nc = a*b;
    c = nc;
    /*
    nres(a, ina);
    nres(b, inb);
    nres_modmult(ina, inb , outc);
    redc(outc,c);
    */
    temp= inverse(a, p);
    //temp((Big)na.getzzn());
    temp = 26*temp;
    cout << "ina=";
    otnum(na.getzzn(), stdout);
    cout << "inb=" ;
    otnum(nb.getzzn(), stdout);
    cout << "outc=";
    otnum(nc.getzzn(), stdout);
    cout << "number3=" <<  c << endl;    
    return  1;
}