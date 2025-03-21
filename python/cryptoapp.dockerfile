# syntax=docker/dockerfile:1

FROM ALPINE:latest
RUN python -m pip install pynacl
WORKDIR ./
COPY createkeys.py
