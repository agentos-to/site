"""agent-sdk CLI — guide, validate, new-app, shapes."""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(prog="agent-sdk", description="agentOS App Development Kit")
    sub = parser.add_subparsers(dest="command")

    # guide
    sub.add_parser("guide", help="Print the app development guide")

    # validate
    p_val = sub.add_parser("validate", help="Validate apps (AST-based static checks)")
    p_val.add_argument("target", nargs="?", default=None,
                       help="App id, app directory, or apps root (default: auto-discover)")
    p_val.add_argument("--all", action="store_true", help="Audit every app (default when no target)")
    p_val.add_argument("--sandbox", action="store_true", help="Only run the banned-import sandbox scan")
    p_val.add_argument("--fix-sources", action="store_true",
                       help="Review and clean up missing paths in settings.sources (interactive)")
    p_val.add_argument("--dry-run", action="store_true", help="(reserved — not yet implemented)")

    # new-app
    p_new = sub.add_parser("new-app", help="Scaffold a new app")
    p_new.add_argument("name", help="App name (e.g. my-meetup-app)")
    p_new.add_argument("--shape", default=None, help="Return shape (e.g. event, product)")

    # shapes
    p_shapes = sub.add_parser("shapes", help="List or inspect shapes")
    p_shapes.add_argument("name", nargs="?", help="Shape name to inspect")

    args = parser.parse_args()

    if args.command == "guide":
        from agentos.guide import print_guide
        print_guide()
    elif args.command == "validate":
        if args.fix_sources:
            from agentos.validate import _fix_sources_interactive
            sys.exit(_fix_sources_interactive())
        from agentos.validate import run_validate
        rc = run_validate(
            args.target,
            validate_all=args.all,
            sandbox_only=args.sandbox,
            dry_run=args.dry_run,
        )
        sys.exit(rc)
    elif args.command == "new-app":
        from agentos.scaffold import run_new_app
        run_new_app(args.name, args.shape)
    elif args.command == "shapes":
        from agentos.shape_cli import run_shapes
        run_shapes(args.name)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
