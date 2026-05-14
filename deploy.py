"""
deploy.py — Build and deploy Mukesh Singh's portfolio to GitHub Pages
Run this script every time you want to publish changes to your live site.

Usage:
    python deploy.py
"""

import subprocess
import sys


def run(command, description):
    """Run a shell command and print what's happening."""
    print(f"\n⏳ {description}...")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"\n❌ Something went wrong during: {description}")
        print("   Check the error above and try again.")
        sys.exit(1)
    print(f"✅ Done: {description}")


def main():
    print("=" * 50)
    print("  🚀 Mukesh Singh — Portfolio Deployer")
    print("=" * 50)

    # Step 1: Install dependencies (safe to run every time)
    run(
        "pip install mkdocs mkdocs-material ghp-import --quiet",
        "Checking / installing dependencies"
    )

    # Step 2: Build the site (converts Markdown → HTML)
    run(
        "mkdocs build --clean",
        "Building your site (Markdown → HTML)"
    )

    # Step 3: Deploy to GitHub Pages
    run(
        "mkdocs gh-deploy --force",
        "Deploying to GitHub Pages"
    )

    print("\n" + "=" * 50)
    print("  🎉 Your portfolio is live!")
    print("  🌐 https://Mukesh29s.github.io/portfolio")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
