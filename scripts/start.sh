#! /bin/bash
set -e

echo 'Starting app...'
uvicorn src.main:app --reload --host 0.0.0.0 --log-level debug