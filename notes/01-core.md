# Clamp a number to bounds: implementation

## What the example does

Validate the lower bound before clamping. Inclusive bounds mean values already inside the interval are returned unchanged.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "number": 12,
  "low": 0,
  "high": 10
}
```

Expected result:

```json
10
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
