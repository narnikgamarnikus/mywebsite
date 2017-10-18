#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A website.taskapp worker -l INFO
