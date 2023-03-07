#!/bin/bash
python3 ./mom/src/filesearching.py & 

python3 ./grpc/src/server.py & 

python3 ./gateway/api_gateway.py  