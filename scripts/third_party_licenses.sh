#!/usr/bin/env zsh

if [[ ! -f "pyproject.toml" ]]; then
    echo "pyproject.toml not found. Exiting..."
    exit 1
fi

echo "# Third Party Licenses" > THIRD_PARTY_LICENSES.md
echo "This file contains the licenses of third-party dependencies used in this project." >> THIRD_PARTY_LICENSES.md
echo "Generated on $(date)" >> THIRD_PARTY_LICENSES.md
echo "" >> THIRD_PARTY_LICENSES.md

# Get direct dependencies from pyproject.toml using tomllib and output names without version constraints.
deps=$(uv run - <<'EOF'
import tomllib, re
with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)
deps = config["project"].get("dependencies", [])
# Remove version constraints by splitting on '<', '>', or '=' and stripping quotes
names = [re.split(r'[<>=]', dep)[0].strip().strip('"').strip("'") for dep in deps]
print(" ".join(names))
EOF
)

echo "## Direct Dependencies" >> THIRD_PARTY_LICENSES.md
echo "This section lists the direct dependencies of the project." >> THIRD_PARTY_LICENSES.md
echo "" >> THIRD_PARTY_LICENSES.md

# Split the deps string into an array using Zsh syntax
deps_array=("${(s: :)deps}")

# Use the array with proper quoting
uv run pip-licenses --packages "${deps_array[@]}" --from=mixed --format=markdown --with-urls >> THIRD_PARTY_LICENSES.md
echo "" >> THIRD_PARTY_LICENSES.md

# Get dev dependencies from pyproject.toml using tomllib and output names without version constraints.
dev_deps=$(uv run - <<'EOF'
import tomllib, re
with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)
deps = config["tool"]["uv"].get("dev-dependencies", [])
# Remove version constraints by splitting on '<', '>', or '=' and stripping quotes
names = [re.split(r'[<>=]', dep)[0].strip().strip('"').strip("'") for dep in deps]
print(" ".join(names))
EOF
)

echo "## Development Dependencies" >> THIRD_PARTY_LICENSES.md
echo "This section lists the development dependencies of the project." >> THIRD_PARTY_LICENSES.md
echo "" >> THIRD_PARTY_LICENSES.md

# Split the deps string into an array using Zsh syntax
dev_deps_array=("${(s: :)dev_deps}")

# Use the array with proper quoting
uv run pip-licenses --packages "${dev_deps_array[@]}" --from=mixed --format=markdown --with-system --with-urls >> THIRD_PARTY_LICENSES.md
