#!/bin/bash
set -e

jupyter notebook --ip=0.0.0.0 --no-browser "$@"
