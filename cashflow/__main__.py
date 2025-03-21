from rich.console import Console

from cashflow.app import CashFlowApp

console = Console()


def main() -> None:
    app = CashFlowApp()
    app.run()


if __name__ == "__main__":
    main()
