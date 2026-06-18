# Python Virtual Environment (venv)

## What is a Virtual Environment?

A virtual environment is a separate Python workspace that keeps a project's libraries isolated from the system Python and other projects.

## Why Use venv?

- Avoid package conflicts
- Keep projects independent
- Maintain clean system installations
- Easily recreate project environments
- Manage different package versions

## Creating a Virtual Environment

```bash
python3 -m venv .venv
```

This creates a folder named `.venv` containing a dedicated Python environment.

## Activating the Environment

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows CMD

```cmd
.venv\Scripts\activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

After activation, you'll see:

```text
(.venv)
```

in the terminal.

## Installing Packages

```bash
pip install requests
```

Install multiple packages:

```bash
pip install numpy pandas matplotlib
```

View installed packages:

```bash
pip list
```

## Saving Dependencies

```bash
pip freeze > requirements.txt
```

Example:

```text
requests==2.32.3
numpy==2.3.0
```

## Reinstalling Dependencies

```bash
pip install -r requirements.txt
```

Useful when sharing a project with others.

## Deactivating venv

```bash
deactivate
```

This returns you to the system Python environment.

## Removing a Virtual Environment

Linux/macOS:

```bash
rm -rf .venv
```

Windows:

```cmd
rmdir /s .venv
```

## Quick Workflow

```bash
mkdir demo_project
cd demo_project

python3 -m venv .venv
source .venv/bin/activate

pip install requests

pip freeze > requirements.txt

deactivate
```

## Best Practices

- Create a new venv for every project.
- Do not upload `.venv` to GitHub.
- Keep dependencies in `requirements.txt`.
- Activate the environment before running your project.

Example `.gitignore`:

```gitignore
.venv/
__pycache__/
*.pyc
```

## Conclusion

A virtual environment helps manage project dependencies efficiently by creating an isolated Python workspace. It is a recommended practice for all Python projects.