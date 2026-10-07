# Python Arithmetic Tests

A minimal Python project with two intentionally failing unit tests.

## Run the tests

```sh
python -m unittest -v
```

## Intentional failures

- `add` correctly returns the sum, but its test expects `6` for `2 + 3`.
- `subtract` is intended to subtract, but currently adds its arguments; its test expects `7 - 3` to equal `4`.

The project uses Python's built-in `unittest` module and has no external dependencies.
