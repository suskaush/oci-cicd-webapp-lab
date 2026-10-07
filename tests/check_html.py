from pathlib import Path

page = Path("app/index.html").read_text(encoding="utf-8")

assert "OCI CI/CD Web App" in page
assert "Version" in page

print("HTML validation passed.")
