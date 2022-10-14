##!/bin/bash


ENV_FILE=".env"

POSTGRES_DB=
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432
POSTGRES_HOST=localhost
TOKEN=
KEYWORD=
MAX=10
ITERATION=1


usage() { 
echo "Usage: $0 
  -U <POSTGRES_USER> default 'postgres'
  -W <POSTGRES_PASSWORD> default 'postgres'
  -H <POSTGRES_HOST> default 'localhost'
  -p <POSTGRES_PORT> default '5432'
  -D <POSTGRES_DB> required
  -t <BEARER_TOKEN> required
  -k <KEYWORD> required
  -m <MAX_RESULTS> default '10'
  -i <ITERATION>] default '1'"
  1>&2;
  exit 1; 
}

while getopts ":U:W:H:p:D:t:k:m:i:" o; do
    case "${o}" in
        i)
            ITERATION=${OPTARG}
            ;;
        m)
            MAX=${OPTARG}
            ;;
        k)
            KEYWORD=${OPTARG}
            ;;
        t)
            TOKEN=${OPTARG}
            ;;
        D)
            POSTGRES_DB=${OPTARG}
            ;;
        U)
            POSTGRES_USER=${OPTARG}
            ;;
        W)
            POSTGRES_PASSWORD=${OPTARG}
            ;;
        H)
            POSTGRES_HOST=${OPTARG}
            ;;
        p)
            POSTGRES_PORT=${OPTARG}
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))

if [ -z "${POSTGRES_DB}" ] || [ -z "${TOKEN}" ] || [ -z "${KEYWORD}" ]; then
    usage
fi

echo "\
POSTGRES_DB=$POSTGRES_DB
POSTGRES_USER=$POSTGRES_USER
POSTGRES_PASSWORD=$POSTGRES_PASSWORD
POSTGRES_PORT=$POSTGRES_PORT
POSTGRES_HOST=$POSTGRES_HOST
TOKEN=$TOKEN
ITERATION=$ITERATION
KEYWORD=$KEYWORD
MAX_RESULTS=$MAX
" > $ENV_FILE

source $ENV_FILE

echo "images is being created"
docker-compose up
rm -f $ENV_FILE
