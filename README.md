Pinner
---
This tool provides an easy way to manage microservices by freezing their
versions under a single platform.


#### Installing and deps
This project depends on python 3.7.2, install
[python virtualenv](https://virtualenv.pypa.io/en/latest/).  

Prerequisites:

> python 3.7   
libgit2,  libgit2-glib - macbook

```bash
$ virtualenv -p python3 .venv
....
# activate the virtualenv

source .venv/bin/activate
```

Now you can install the application

```bash
$: python3.7 setup.py install
```

##### Usage

The tool has three options: `describe`, `fetch` and `validate`. The `--version`
and the `--workspace' (or exporting PINNER_WORKSPACE) parameters are mandatory
for commands.  

You can find out the parameters needed and the description for each command by
passing `--help` at the end.
e.g.:
```bash
$: python3.7 pinner.py  describe --help
Usage: pinner.py describe [OPTIONS]

  This command will show you the pinned microservice versions together with
  some relevant metadata such as pinned refs and url. The data is tabulated.

Options:
  --version TEXT  The specific platform version
  --help          Show this message and exit.
```
