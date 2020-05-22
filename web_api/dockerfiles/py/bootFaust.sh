#!/bin/bash
#!/bin/sh

set -o errexit
# set -o pipefail
set -o nounset



n=10

while [ $n -gt 0 ]
do
	echo "Wait for kafka $n more times."
	n=$(( n-1 ))
    sleep 8
done


echo ". . . . . Faust Is Done! . . . . ."

exec "$@"