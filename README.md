# Lab 6: Calculator and GitHub Actions

A Python Calculator with add, subtract, multiply, and divide methods, and 12 unit tests (three per method).

## Run the tests

Requires Python 3.11. No external packages are needed.

```sh
python -m unittest discover -s tests -v
```

Tests cover positive and negative values, decimals, zero, and division by zero. Decimal results use assertAlmostEqual to allow for floating-point rounding.

## Automated testing

The workflow in `.github/workflows/tests.yml` runs on every push to `master`. GitHub checks out the code, sets up Python 3.11 on Ubuntu, and runs all tests. A failing test causes the job to fail.

Use the `master` branch for this exercise. Open the repository's Actions tab to inspect test results.

This implements continuous integration (CI), the automated testing part of a CI/CD pipeline. No deployment is configured.

## Practice

Temporarily change add to return a - b, run the tests, and observe the failures. Restore a + b and rerun to see the tests pass. If practicing on GitHub, commit and push each change to master to compare failed and successful Actions runs.
