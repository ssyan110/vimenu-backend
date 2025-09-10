#!/usr/bin/env bash
set -euo pipefail
URL="${1:?Usage: smoke_test.sh https://your-url}"
echo "Hitting $URL/health ..."
for i in {1..20}; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "$URL/health" || true)
  if [ "$code" = "200" ]; then
    echo "Smoke test passed."
    exit 0
  fi
  echo "Attempt $i failed (code=$code). Retrying in 10s..."
  sleep 10
done
echo "Smoke test FAILED."
exit 1
