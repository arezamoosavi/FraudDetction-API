#!/bin/bash
#!/bin/sh


set -o errexit
set -o nounset



n=10

while [ $n -gt 0 ]
do
	echo "Wait for cassandra $n more times."
	n=$(( n-1 ))
    sleep 5
done


echo ". . . . . Web Boot Up Is Done! . . . . ."

uvicorn run_app:app --host ${HOST} --port ${PORT} --reload --ws 'auto' --loop 'auto' --workers 8

exec "$@"