# TDN: Three- (or Two-) Digit Numbers

See `tdn.py`. Runs on Python 3.8 for sure, probably anything 3.6 and
up (f-strings). I used `pytest` but it's not important.

```bash
pyenv virtualenv 3.8.11 tdn
pyenv local tdn
pip install pytest
pip install --upgrade pip
pip freeze > requirements.txt

pytest
```
