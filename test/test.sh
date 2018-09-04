#!/bin/bash
TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT
trap "rm -f *pyc" EXIT

iconv -f utf-8 -t ascii//TRANSLIT < $1 > $TMPDIR/$1

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
    python2.7 -c "import imp; imp.load_source('', '$TMPDIR/$1').Solution().test()"
fi
