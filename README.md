# Authmoderne

<p align="center">
    <em>Streamlined authentication for modern Python applications.</em>
</p>

[![build](https://github.com/frankie567/authmoderne/workflows/Build/badge.svg)](https://github.com/frankie567/authmoderne/actions)
[![codecov](https://codecov.io/gh/frankie567/authmoderne/branch/master/graph/badge.svg)](https://codecov.io/gh/frankie567/authmoderne)
[![PyPI version](https://badge.fury.io/py/authmoderne.svg)](https://badge.fury.io/py/authmoderne)

---

**Documentation**: <a href="https://frankie567.github.io/authmoderne/" target="_blank">https://frankie567.github.io/authmoderne/</a>

**Source Code**: <a href="https://github.com/frankie567/authmoderne" target="_blank">https://github.com/frankie567/authmoderne</a>

---

## Development

### Setup environment

We use [uv](https://docs.astral.sh/uv/) to manage the development environment and production build, and [just](https://github.com/casey/just) to manage command shortcuts. Ensure they are installed on your system.

### Run unit tests

You can run all the tests with:

```bash
just test
```

### Format the code

Execute the following command to apply linting and check typing:

```bash
just lint
```

### Publish a new version

You can bump the version, create a commit and associated tag with one command:

```bash
just version patch
```

```bash
just version minor
```

```bash
just version major
```

Your default Git text editor will open so you can add information about the release.

When you push the tag on GitHub, the workflow will automatically publish it on PyPi and a GitHub release will be created as draft.

## Serve the documentation

You can serve the Mkdocs documentation with:

```bash
just docs-serve
```

It'll automatically watch for changes in your code.

## License

This project is licensed under the terms of the MIT license.
