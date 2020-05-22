#!/bin/bash
#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

n=9

while [ $n -gt 0 ]
do
	echo "Wait for kafka $n more times."
	n=$(( n-1 ))
    sleep 2
done


n=10

while [ $n -gt 0 ]
do
	echo "Wait for cassandra $n more times."
	n=$(( n-1 ))
    sleep 5
done


while python checkDbConnect.py; do echo 'connecting to database...'; sleep 2; done;

echo ". . . . . Database Connection Is Done! . . . . ."


exec "$@"