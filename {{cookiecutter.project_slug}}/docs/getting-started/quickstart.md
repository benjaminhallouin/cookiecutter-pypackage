# Quick Start

This guide will help you get started with {{ cookiecutter.project_name }}.

## Basic Usage

```python
import {{ cookiecutter.project_slug }}

# Check version
print({{ cookiecutter.project_slug }}.__version__)
```

{% if cookiecutter.include_cli == "yes" -%}
## Command-Line Interface

{{ cookiecutter.project_name }} provides a command-line interface:

```bash
# Display help
{{ cookiecutter.project_slug }} --help

# Example command
{{ cookiecutter.project_slug }} hello World
```
{% endif -%}

## Examples

### Example 1: Basic Usage

```python
from {{ cookiecutter.project_slug }} import exceptions

try:
    # Your code here
    pass
except exceptions.{{ cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '') }}Error as e:
    print(f"Error: {e}")
```

## Next Steps

- Read the [API Reference](../reference/index.md) for detailed documentation
- Check out the [Contributing Guidelines](../development/contributing.md) to contribute
- Report issues on [GitHub](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues)
