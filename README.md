# 📊 Domo Integration Scripts

This project automates the interaction between local Python scripts and the [Domo](https://www.domo.com/) data platform
using the official [`pydomo`](https://pypi.org/project/pydomo/) SDK. It
leverages [`uv`](https://github.com/astral-sh/uv) for fast, modern, and reproducible Python dependency management.

---

## 🚀 Project Purpose

The goal of this project is to:

- Seamlessly connect to Domo using `pydomo`
- Upload and fetch data programmatically
- Perform transformations with `pandas`
- Maintain a fast and secure Python environment using `uv`

This project is useful for automating ETL (Extract, Transform, Load) operations between local systems and Domo.

---

## ⚙️ Technologies Used

- **Python 3.11+**
- [`pydomo`](https://pypi.org/project/pydomo/) – SDK for Domo API access
- [`pandas`](https://pandas.pydata.org/) – Data manipulation library
- [`uv`](https://github.com/astral-sh/uv) – Rust-based dependency manager with lock file support

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Iamgovinda/pdf-to-csv.git
cd pdf-to-csv
```

### 2. Create and activate virtual environment using uv

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

Use --native-tls to resolve any TLS certificate issues:

```bash
uv pip install --native-tls
```

Happy Coding!!!