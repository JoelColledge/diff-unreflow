# Diff unreflow tool

This script extracts the text changes from a diff where a "reflow" operation
has been applied. These changes are then applied without the "reflowing".

Usage:

```
./diff-unreflow.py <original_file> <patched_file>
```

The patched file without the "reflowing" is printed.
