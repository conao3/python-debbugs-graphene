# debbugs-graphene

A GraphQL interface for the Debian Bug Tracking System (Debbugs) built with Python and Graphene.

## Overview

debbugs-graphene provides a modern GraphQL API layer on top of the Debbugs SOAP interface. It enables developers to query bug information from Debian-based bug tracking systems (such as bugs.debian.org and debbugs.gnu.org) using familiar GraphQL syntax.

## Features

- GraphQL schema for querying bugs and bug logs
- Type-safe data models powered by Pydantic
- Seamless integration between Pydantic models and GraphQL types via graphene-pydantic
- Command-line interface for quick access

## Requirements

- Python 3.11 or higher
- Poetry for dependency management

## Installation

```bash
git clone https://github.com/conao3/python-debbugs-graphene.git
cd python-debbugs-graphene
poetry install
```

## Usage

### Command Line

```bash
poetry run debbugs-graphene
```

### As a Library

```python
from debbugs_graphene.graphene.schema import schema

# Execute a GraphQL query
result = schema.execute('''
    query {
        bug {
            bugNum
            subject
            package
            severity
            tags
        }
    }
''')
```

## Data Models

The library provides comprehensive data models for bug tracking:

**Bug** - Complete bug report information including:
- Bug number, subject, and summary
- Originator, owner, and maintainer details
- Severity, tags, and package information
- Version tracking (found/fixed versions)
- Status flags (archived, pending, forwarded)
- Timestamps for creation and modifications

**BugLog** - Bug log entries containing:
- Message number
- Header and body content
- Attachments

## Project Structure

```
src/debbugs_graphene/
├── cli.py                  # Command-line interface
├── types.py                # Pydantic data models
├── client/                 # SOAP client implementation
│   └── method/             # API method handlers
│       ├── get_bugs.py
│       ├── get_bug_log.py
│       ├── get_newest_bugs.py
│       └── get_status.py
└── graphene/               # GraphQL layer
    ├── model.py            # GraphQL object types
    └── schema.py           # GraphQL schema definition
```

## License

See LICENSE file for details.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request on GitHub.
