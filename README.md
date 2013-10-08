# Digestive

Email templateable daily digests of Github activity from the command line.

## Development Setup

```bash
virutalenv .
source bin/activate
pip install -r requirements.txt
```

## Usage

```bash
pip install -r requirements.txt
python digestive.py user/repo email@domain.com
```

## TODO

- Support for pull requests
- Support for commits
- Autheticate with the github API to have a low api limit
- Support custom SMTP server
