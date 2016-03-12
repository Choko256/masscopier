# masscopier
Multi-file recursive file copier from source to target directories

## Prerequisities

- Python 3.x

## Usage

To copy every `jpg`, `jpeg`, `gif` files from `~/source/dir` and its sub-directories into `~/target/dir` directory.
```
$ python masscopier.py ~/source/dir ~/target/dir --filter jpg,jpeg,gif
```

Every filter is the extension name without the initial dot, separated by commas.
