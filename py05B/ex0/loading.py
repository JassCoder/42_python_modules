"""Report on external reagents."""
import importlib


def report(name: str) -> bool:
    """Import a reagent and report its version."""
    try:
        module = importlib.import_module(name)
    except ImportError:
        print(f"[MISSING] {name}")
        print(f" pip install {name}")
        print(f" poetry add {name}")
        return False
    print(f"[OK] {name} ({getattr(module, '__version__', 'unknown')})")
    return True


def main() -> None:
    """Load and report declared reagents."""
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")
    ok = all([report("pandas"), report("numpy")])

    print("pip vs Poetry:")
    print("requirements.txt declares what to install; pip resolves it at "
          "install time.")
    print("pyproject.toml declares the same constraints, and Poetry pins the "
          "resolved versions in poetry.lock so every install is identical.")

    if ok:
        print("All reagents present and accounted for.")
    else:
        print("Some reagents are missing - see the commands above.")


if __name__ == "__main__":
    main()
