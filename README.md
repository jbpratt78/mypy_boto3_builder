# mypy_boto3_builder

[![PyPI - mypy-boto3-builder](https://img.shields.io/pypi/v/mypy-boto3-builder.svg?color=blue&label=mypy-boto3-builder)](https://pypi.org/project/mypy-boto3-builder)
[![PyPI - boto3-stubs](https://img.shields.io/pypi/v/boto3-stubs.svg?color=blue&label=boto3-stubs)](https://pypi.org/project/boto3-stubs)
[![PyPI - boto3](https://img.shields.io/pypi/v/boto3.svg?color=blue&label=boto3)](https://pypi.org/project/boto3)

[![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue&label=Builder%20docs)](https://mypy-boto3-builder.readthedocs.io/)
[![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue&label=boto3-stubs%20docs)](https://pypi.org/project/boto3-stubs/)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/boto3-stubs.svg?color=blue)](https://pypi.org/project/boto3-stubs)
[![Coverage](https://img.shields.io/codecov/c/github/vemel/mypy_boto3_builder)](https://codecov.io/gh/vemel/mypy_boto3_builder)
[![PyPI - Downloads](https://img.shields.io/pypi/dw/boto3-stubs?color=blue)](https://pypistats.org/packages/boto3-stubs)


Type annotations builder for [boto3-stubs](https://pypi.org/project/boto3-stubs/) project. Compatible with [mypy](https://github.com/python/mypy), [VSCode](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/) and other tools.

- [mypy_boto3_builder](#mypyboto3builder)
  - [Using boto3-stubs](#using-boto3-stubs)
  - [How to build type annotations](#how-to-build-type-annotations)
    - [Locally](#locally)
    - [With Docker image](#with-docker-image)
  - [Versioning](#versioning)
  - [Latest changes](#latest-changes)
  - [Thank you](#thank-you)

## Using boto3-stubs

Check [boto3-stubs](https://pypi.org/project/boto3-stubs/) project for installation
and usage instructions.

If you use up-to-date `boto3` version, just install corresponding `boto3-stubs` and start
using code auto-complete and `mypy` validation. You can find instructions on
[boto3-stubs](https://pypi.org/project/boto3-stubs/) page.

This page is only for building type annotations manually. For example, if you want to
use the latest features for an older `boto3` version.

## How to build type annotations

### Locally

```bash
# Install preferred version of `boto3`
python -m pip install boto3==1.10.18 botocore==1.13.18

# Install `mypy-boto3-builder`
python -m pip install mypy-boto3-builder

# Build all packages
# You can specify required services explicitly like
# ./scripts/build.sh -s ec2 s3
./scripts/build.sh

# Install custom `boto3-stubs` packages
./scripts/install.sh
```

### With Docker image

- Install [Docker](https://docs.docker.com/install/)
- Pull latest `mypy_boto3_builder` version and tag it

```bash
docker pull docker.pkg.github.com/vemel/mypy_boto3_builder/mypy_boto3_builder_stable:latest
docker tag docker.pkg.github.com/vemel/mypy_boto3_builder/mypy_boto3_builder_stable:latest mypy_boto3_builder
```

- Generate stubs in `output` directory

```bash
mkdir output

# generate stubs for all services
docker run -v `pwd`/output:/output -ti mypy_boto3_builder

# generate stubs for s3 service
docker run -v `pwd`/output:/output -ti mypy_boto3_builder -s s3

# generate stubs for a specific boto3 version
docker run -e BOTO3_VERSION=1.10.18 BOTOCORE_VERSION=1.13.18 -v `pwd`/output:/output -ti mypy_boto3_builder
```

- Install packages from `output` directory as described above

## Versioning

`mypy_boto3_builder` version is not related to `boto3` version and follows
[Semantic Versioning](https://semver.org/).

## Latest changes

Full changelog can be found in [Releases](https://github.com/vemel/mypy_boto3_builder/releases).

## Thank you

- Guys behind [boto3-type-annotations](https://pypi.org/project/boto3-type-annotations/),
  this package is based on top of their work
- [black](https://github.com/psf/black) developers for awesome formatting tool
- [mypy](https://github.com/python/mypy) for doing all dirty work for us
