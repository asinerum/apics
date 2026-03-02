# APICS: Literp Compact Server

## Prerequisites

Python 3.10 with Pip 25.0.0 fresh installed and added to PATH

## Server Configuration and Fundamental Data

Contact your consultant to implement.  
Server directory tree should be something that looks like this:

```text
.
apics
├── access.yaml
├── app.yaml
├── dbase.yaml
├── io.yaml
├── lib
│   ├── db
│   │   └── query
│   │     ├── accounting
│   │     │   ├── README.txt
│   │     │   ├── insert.yaml
│   │     │   ├── select.yaml
│   │     │   ├── update.yaml
│   │     │   └── xaccount
│   │     │     ├── insert.yaml
│   │     │     └── select.yaml
│   │     └── admin
│   │       ├── README.txt
│   │       ├── insert.yaml
│   │       ├── select.yaml
│   │       └── update.yaml
│   ├── json
│   │   ├── accounting
│   │   │   ├── account.json
│   │   │   └── role.json
│   │   └── bank.json
│   └── yaml
│     └── accounting
│       ├── report.yaml
│       ├── rich.yaml
│       └── transaction.yaml
├── literp-key.pem
├── literp.pem
└── model.yaml
```

## Server Installation

```ts
cd apics
pip install apics
```

## Start Server with SQLite

```ts
apics
```

## Start Server with DuckDB

```ts
apics -d duckdb
```

(C)2026 ASINERUM CONLANG PROJECT
