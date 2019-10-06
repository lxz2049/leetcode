#!/bin/bash
TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT
trap "rm -f *pyc" EXIT

iconv -c -f ascii -t ascii < $1 > $TMPDIR/$1

if [[ $TMPDIR/$1 =~ \.cpp$ ]]
then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        clang++ -std=c++11 -stdlib=libc++ --include leetcode.h --include $TMPDIR/$1 test.cpp -o $TMPDIR/_test
    else
        g++ --include leetcode.h --include $TMPDIR/$1 test.cpp -o $TMPDIR/_test
    fi
    $TMPDIR/_test
fi
if [[ $TMPDIR/$1 =~ \.py$ ]]
then
    echo "from typing import *
    $(cat $TMPDIR/$1)" > $TMPDIR/$1.old
    echo "$(cat $TMPDIR/$1.old)
Solution().test()" > $TMPDIR/$1
    python3 $TMPDIR/$1
fi
