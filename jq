jq '.ports_ip.values | map_values(strings) | map(select(test("^[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+$")))[]' file.json
