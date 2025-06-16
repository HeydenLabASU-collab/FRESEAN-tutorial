#!/bin/bash

CC=gcc

SCRIPT_DIR=$(dirname "$0")
cd $SCRIPT_DIR

$CC -O3 -fopenmp -fpic -c unwrap.c
$CC -shared -lgomp unwrap.o -o libunwrap.so

$CC -O3 -fopenmp -fpic -c align.c
$CC -shared -lgomp align.o -o libalign.so
