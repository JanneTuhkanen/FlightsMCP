#!/bin/sh

RELOAD=""

# Parse arguments in format --argument-name=value
for arg in "$@"; do
    case "$arg" in
    --reload)
        RELOAD="--reload"
        ;;
    esac
done

uv run uvicorn app.main:app --port 8000 $RELOAD