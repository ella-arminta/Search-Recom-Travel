#!/bin/bash

# Check if rabbit is up and running before starting the service.

until nc -z ${RABBIT_HOST} ${RABBIT_PORT}; do
    echo "$(date) - waiting for rabbitmq..."
    sleep 20
done

# Run the service
export PYTHONPATH=$(pwd)

nameko run --config config.yml searchrecom.agent searchrecom.airlines searchrecom.atraksi searchrecom.carrental searchrecom.hotel searchrecom.insurance searchrecom.servicelist --backdoor 3000