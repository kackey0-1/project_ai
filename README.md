# Project AI
## 
[TensorFlow](https://caffeinedev.medium.com/how-to-install-tensorflow-on-m1-mac-8e9b91d93706)

## initialization
```bash
flask create-db
flask drop-db
```

## Run application
```bash
flask run --host 0.0.0.0 --port 8000
```

## Test 
```bash
pytest -s -vvvv -l --tb=long tests
```

## Check Endpoint
```bash
flack routes
```

## Check Database
```
psql -h localhost -U root -W root -d project_ai
```

## Release
```shell
heroku git:remote -a project-ai-v0
git add .
git commit -am "make it better"
git push heroku main 
```

## Database Setup on Heroku
https://qiita.com/Takao_/items/aeb3570b42a6aeb5461f#4mysql%E3%82%92%E8%BF%BD%E5%8A%A0
If you need to have mysql-client first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/mysql-client/bin:$PATH"' >> ~/.zshrc

For compilers to find mysql-client you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/mysql-client/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/mysql-client/include"

For pkg-config to find mysql-client you may need to set:
ImportError: dlopen(/Users/k-kakimoto/PycharmProjects/project_ai/.venv/lib/python3.9/site-packages/MySQLdb/_mysql.cpython-39-darwin.so, 0x0002): tried: '/usr/local/mysql/lib//_mysql.cpython-39-darwin.so' (no such file), '/Users/k-kakimoto/PycharmProjects/project_ai/.venv/lib/python3.9/site-packages/MySQLdb/_mysql.cpython-39-darwin.so' (mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64e')), '/usr/local/lib/_mysql.cpython-39-darwin.so' (no such file), '/usr/lib/_mysql.cpython-39-darwin.so' (no such file)
