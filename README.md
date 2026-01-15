# Project CI/CD fix summary

This repository originally had CI/CD issues which have been fixed and validated.

## 🔧 What was fixed
- **requirements.txt**: pinned insecure `requests==0.0.1` to the stable `requests==2.31.0` and added a pinned `mypy==1.8.0`.
- **app.py**: added `--check-config` CLI option so `cd_pipeline.bat` can validate config and provided a non-invalid `API_KEY`.
- **.venv**: created a clean virtual environment under `.venv/` and installed dependencies.
- **CI / CD scripts**: executed from the correct directories so relative paths work (no modifications to the scripts themselves).
- **.gitignore**: ensures `.venv/` and `logs/` are not committed.

## 📁 Generated files
- `.venv/` — local virtual environment (created locally, not checked-in)
- `logs/test_run.log` — consolidated log for CI and CD runs
- `report.json` — structured list of CI/CD problems and fixes

## ▶️ How to run CI / CD locally
```powershell
# Create a clean environment
if (Test-Path .venv) { Remove-Item -Recurse -Force .venv }
python -m venv .venv

# Install deps into .venv
.venv\Scripts\python -m pip install -r requirements.txt

# Run CI (from the ci/ directory)
Push-Location ci; $env:Path=(Resolve-Path '..\.venv\Scripts').Path + ';' + $env:Path; .\ci_pipeline.bat; Pop-Location

# Run CD (from the cd/ directory)
Push-Location cd; $env:Path=(Resolve-Path '..\.venv\Scripts').Path + ';' + $env:Path; .\cd_pipeline.bat; Pop-Location
```

The CI and CD logs are appended to `logs/test_run.log`.

## 💡 Notes
- The CI script expects to be run from the `ci/` directory so the relative `..\requirements.txt` path resolves;
- The CD script expects to be run from the `cd/` directory.

If you prefer to run scripts from the repository root, you can adapt the bat files to use absolute paths or run them with the working directory adjusted as above.
