```bash
pipenv install
pipenv shell
hypercorn main:app --bind localhost:80 --reload
```
