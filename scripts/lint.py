import subprocess
import sys


def run():
    subprocess.call(
        ["ruff", "check", "note_app", "--fix"],
        stdin=sys.stdin,
        stderr=sys.stderr
    )