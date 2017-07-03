mkdocs build --clean
cd labs & ipython nbconvert --to html visualization.ipynb & cd ..
git add -A
git commit -m "update docs"
git push origin master