import argparse
import subprocess

def run_command(command):
    """Runs a shell command and prints its output."""
    print(f"> {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print("-" * 40)  # line divider

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Add-Commit-Push Helper")
    parser.add_argument("-m", "--message", help="Commit message", required=False)
    args = parser.parse_args()

    # 1️⃣ Print git status
    print("git status:")
    run_command("git status")

    # 2️⃣ Print queued commands
    print("Queued commands:")
    print("  git add -A")
    print(f"  git commit -m \"{args.message or 'default commit message'}\"")
    print("  git push")

    # 3️⃣ Ask user to confirm
    confirm = input("\nRun these commands? (y/n) > ").lower()
    if confirm != "y":
        print("❌ Cancelled.")
        return

    # 4️⃣ Execute each command
    run_command("git add -A")
    run_command(f"git commit -m \"{args.message or 'default commit message'}\"")
    run_command("git push")

if __name__ == "__main__":
    main()
