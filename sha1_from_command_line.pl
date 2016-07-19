#!/usr/bin/env perl

##  sha1_from_command_line.pl
##  by Avi Kak (kak@purdue.edu)
##  March 2, 2016

## Call syntax:
##
##     sha1_from_command_line.pl   your_message_string

##  This script takes its message on the standard input from
##  the command line and sends the hash to its standard
##  output.  NOTE: IT ADDS A NESWLINE AT THE END OF THE OUTPUT
##  TO SHOW THE HASHCODE IN A LINE BY ITSELF.

use strict;
use warnings;
use Algorithm::BitVector 1.25;

die "Usage: %s  <string to be hashed>\n" if @ARGV != 1;

my $message = shift;

# Initialize hashcode for the first block. Subsequetnly, the
# output for each 512-bit block of the input message becomes
# the hashcode for the next block of the message.
my $h0 = Algorithm::BitVector->new(hexstring => '67452301');
my $h1 = Algorithm::BitVector->new(hexstring => 'efcdab89');
my $h2 = Algorithm::BitVector->new(hexstring => '98badcfe');
my $h3 = Algorithm::BitVector->new(hexstring => '10325476');
my $h4 = Algorithm::BitVector->new(hexstring => 'c3d2e1f0');

my $bv = Algorithm::BitVector->new(textstring => $message);
my $length = $bv->length();
my $bv1 = $bv + Algorithm::BitVector->new(bitstring => "1");
my $length1 = $bv1->length();
my $howmanyzeros = (448 - $length1) % 512;
my @zerolist = (0) x $howmanyzeros;
my $bv2 = $bv1 + Algorithm::BitVector->new(bitlist => \@zerolist);
my $bv3 = Algorithm::BitVector->new(intVal => $length, size => 64);
my $bv4 = $bv2 + $bv3;

my @words = (undef) x 80;        
my @words_bv = (undef) x 80;   

for (my $n = 0; $n < $bv4->length(); $n += 512) {
    my @block = @{$bv4->get_bit( [$n .. $n + 511] )};
    @words = map {[@block[$_ * 32 .. ($_ * 32 + 31)]]}  0 .. 15;    
    @words_bv = map {Algorithm::BitVector->new( bitlist => $words[$_] )} 0 .. 15;

    my ($a,$b,$c,$d,$e) = ($h0,$h1,$h2,$h3,$h4);
    my ($f,$k);
    foreach my $i (16 .. 79) {
        $words_bv[$i] = $words_bv[$i-3] ^ $words_bv[$i-8] ^ $words_bv[$i-14] ^ $words_bv[$i-16];
        $words_bv[$i] = $words_bv[$i] << 1;
    }
    foreach my $i (0 .. 79) {
        if (($i >= 0) && ($i <= 19)) {
            $f = ($b & $c) ^ ((~$b) & $d);
            $k = 0x5a827999;
        } elsif (($i >= 20) && ($i <= 39)) {
            $f = $b ^ $c ^ $d;
            $k = 0x6ed9eba1;
        } elsif (($i >= 40) && ($i <= 59)) {
            $f = ($b & $c) ^ ($b & $d) ^ ($c & $d); 
            $k = 0x8f1bbcdc;
        } elsif (($i >= 60) && ($i <= 79)) {
            $f = $b ^ $c ^ $d;
            $k = 0xca62c1d6;
        }
        my $a_copy = $a->deep_copy();
        my $T = Algorithm::BitVector->new( intVal => (int($a_copy << 5) + int($f) 
                         + int($e) + int($k) + int($words_bv[$i])) & 0xFFFFFFFF, size => 32 );
        $e = $d;
        $d = $c;
        my $b_copy = $b->deep_copy();
        $b_copy = $b_copy << 30;
        $c = $b_copy;
        $b = $a;
        $a = $T;
    }
    $h0 = Algorithm::BitVector->new( intVal => (int($h0) + int($a)) & 0xFFFFFFFF, size => 32 );
    $h1 = Algorithm::BitVector->new( intVal => (int($h1) + int($b)) & 0xFFFFFFFF, size => 32 );
    $h2 = Algorithm::BitVector->new( intVal => (int($h2) + int($c)) & 0xFFFFFFFF, size => 32 );
    $h3 = Algorithm::BitVector->new( intVal => (int($h3) + int($d)) & 0xFFFFFFFF, size => 32 );
    $h4 = Algorithm::BitVector->new( intVal => (int($h4) + int($e)) & 0xFFFFFFFF, size => 32 );
}

my $message_hash = $h0 + $h1 + $h2 + $h3 + $h4;
my $hash_hex_string = $message_hash->get_hex_string_from_bitvector();
print "$hash_hex_string\n";
