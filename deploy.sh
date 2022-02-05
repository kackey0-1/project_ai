#!/usr/bin/env bash
cd ui
npm run build
cd ..

git add .
git commit -m "commit for deploy"
git push heroku main
