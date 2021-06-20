#!/bin/bash
# Remember to set environment variables before running this script
# DATABASE_URI
# SECRET_KEY
# MYSQL_ROOT_PASSWORD
# MYSQL_DATABASE

if [ -z $DATABASE_URI] || [ -z $SECRET_KEY ] || [ -z $MYSQL_DATABASE ] || [ -z $MYSQL_ROOT_PASSWORD ]
then
    echo "One or more of youre secrests has not been set"
    exit 1
fi

sad \
    -e 's,{{DATABASE_URI}},'$DATABASE_URI',g;' \
    -e 's,{{SECRET_KEY}},'$SECRET_KEY',g;' \
    -e 's,{{MYSQL_ROOT_PASSWORD}},'$MYSQL_ROOT_PASSWORD',g;' \
    -e 's,{{MYSQL_DATABASE}},'MYSQL_DATABASE',g;' secrets.yaml | kubectl apply -f -