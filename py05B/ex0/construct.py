"""Detect whether we run inside a virtual environment and report on it."""
import os
import sys


def in_venv() -> bool:
    """Return True when running inside a virtual environment.

    Two cases are checked:

    - Legacy virtualenv: ``sys.real_prefix`` exists and points to
      the original Python install.
    - Modern venv:       ``sys.base_prefix`` (original Python) and
      ``sys.prefix`` (current interpreter) differ, because the venv
      has re-rooted ``sys.prefix``.
    """
    return (
        hasattr(sys, "real_prefix")
        or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
    )


def venv_name() -> str | None:
    """Return the folder name of the active virtual environment. """
    if not in_venv():
        return None
    return os.path.basename(sys.prefix)


def site_packages_path() -> str:
    """Return the site-packages directory of the active interpreter. """
    import site

    paths = site.getsitepackages()
    if paths:
        return paths[0]
    return os.path.join(sys.prefix, "lib", "site-packages")


def show_sealed() -> None:
    """Output when running inside a virtual environment."""
    print()
    print(f"LABORATORY STATUS:{c}The laboratory is sealed{r}")
    print()
    print(f"Current Python: {c}{sys.executable}{r}")
    print(f"Virtual Environment: {c}{venv_name()}{r}")
    print(f"Environment Path: {c}{sys.prefix}{r}")
    print()
    print(f"SUCCESS:{c}You are working in an isolated environment!{r}")
    print("Safe to install reagents without affecting the global system.")
    print()
    print("Reagent installation path:")
    print(f"{c}{site_packages_path()}{r}")


def show_open() -> None:
    """Output when running in the global environment."""
    c = "\033[33m"
    print()
    print("LABORATORY STATUS: You are working in the open")
    print()
    print(f"Current Python: {c}{sys.executable}{r}")
    print(f"Virtual Environment: {c}None detected{r}")
    print()
    print(f"WARNING: {c}You are in the global environment!{r}")
    print("Every reagent you install here leaks into the whole system.")
    print()
    print(f"To seal the laboratory, run:{c}")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate   # On Unix")
    print("lab_env\\Scripts\\activate      # On Windows")
    print()
    print()
    print(f"Then run this program again.{r}")


def main() -> None:
    """Report the laboratory status."""
    if in_venv():
        show_sealed()
    else:
        show_open()


if __name__ == "__main__":
    c = "\033[32m"
    r = "\033[0m"
    main()
