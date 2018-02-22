#!/bin/bash
echo "creating temp dir"
TMPDIR=$(mktemp -d)
trap "echo removing temp dir; rm -rf $TMPDIR" EXIT

echo "converting source to ascii"
iconv -f utf-8 -t ascii//TRANSLIT < $1 > $TMPDIR/tmp
cp $TMPDIR/tmp $1

if [[ $1 =~ \.cpp$ ]]
then
    echo "compiling $1"
    g++ --include leetcode.h --include $1 test.cpp -o $TMPDIR/_test
    TMPDIR/_test
fi
if [[ $1 =~ \.py$ ]]
then
    echo "interpreting $1"
    python -c "import imp; imp.load_source('', '$1').Solution().test()"
fi
