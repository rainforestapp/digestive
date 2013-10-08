# Digestive

A simple email digest of what your team did today on GitHub, sent from the command line. Digestive started out as an Interview Hack Evening at [Rainforest](https://www.rainforestqa.com/).

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
