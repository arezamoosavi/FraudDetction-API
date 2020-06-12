#!/bin/sh

n=10

while [ $n -gt 0 ]
do
	echo "Wait for $n more times."
	n=$(( n-1 ))
    sleep 5
done

spark-submit app.py

exec "$@"