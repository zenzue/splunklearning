#!/bin/bash
umask 0077

exec /sbin/entrypoint.sh "$@"