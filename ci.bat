mkdocs build --clean
git add -A
git commit -m "update docs"
cd labs & ipython nbconvert --to html visualization.ipynb & cd ..
git push origin master