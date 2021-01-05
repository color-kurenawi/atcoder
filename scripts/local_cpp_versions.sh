
#!/usr/bin/env bash

echo "Abailable C++ Version:"
gcc -v --help 2>/dev/null | grep -E "^\s+\-std=.*$"

