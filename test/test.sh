#!/bin/bash
if [[ $1 =~ \.cpp$ ]]
then
    g++ --include leetcode.h --include $1 test.cpp -o test
    ./test
fi
if [[ $1 =~ \.py$ ]]
then
    python -c "import imp; print imp.load_source('', '$1').Solution().test()"
fi
