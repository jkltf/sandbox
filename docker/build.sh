#!/bin/bash

set -e

for i in ubuntu-jaist ansible-node; do pushd $i; bash build.sh; popd; done
