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
    print("LABORATORY STATUS: The laboratory is sealed")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name()}")
    print(f"Environment Path: {sys.prefix}")
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting the global system.")
    print("Reagent installation path:")
    print(site_packages_path())


def show_open() -> None:
    """Output when running in the global environment."""
    print("LABORATORY STATUS: You are working in the open")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.")
    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate   # On Unix")
    print("lab_env\\Scripts\\activate      # On Windows")
    print("Then run this program again.")


def main() -> None:
    """Report the laboratory status."""
    if in_venv():
        show_sealed()
    else:
        show_open()


if __name__ == "__main__":
    main()
