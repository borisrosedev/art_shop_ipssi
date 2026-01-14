#!/bin/bash
set -e

EMAIL="${EMAIL:?missing EMAIL}"
PASSWORD="${PASSWORD:?missing PASSWORD}"

COOKIE_JAR="cookies.txt"

echo "🔐 Logging in..."

curl -sS \
  -c "$COOKIE_JAR" \
  -H "Content-Type:application/json" \
  -d "{\"email\":\"$EMAIL\",\"password\":\"$PASSWORD\"}" \
  http://localhost:5000/api/v1/auth/login

echo "✅ Logged in, fetching protected resource..."

curl -b "$COOKIE_JAR" http://localhost:5000/api/v1/user/me

curl -sS \
     -c "$COOKIE_JAR" \
     http://localhost:5000/api/v1/auth/logout

curl -b "$COOKIE_JAR" http://localhost:5000/api/v1/user/me
