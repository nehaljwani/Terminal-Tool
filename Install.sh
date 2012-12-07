#!/bin/bash
#+----------------------------------------------------
# Commands for compiling modified bash
#+----------------------------------------------------
INSTALLDIR=$PWD/Terminal
cd Source
tar -xf myBash.tar.gz
cd myBash
./configure --prefix=$INSTALLDIR 
make clean all install
cd ../../
