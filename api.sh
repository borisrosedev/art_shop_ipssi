# shellcheck shell=bash
test_get_all() {
    curl -sSi X GET http://localhost:8080/api/v1/users
}

test_get_all
