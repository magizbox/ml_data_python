mkdocs build --clean
git add -A
git commit -m "update docs"
cd labs; nbconvert --to html visualization.ipynb
git push origin master