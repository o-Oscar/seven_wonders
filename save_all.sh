set -e

echo "--- Running the python file seven_wonders.py"
python seven_wonders.py

echo "--- Saving everything using git" 
git status
git add .
git status
git commit -m "commit from save_all.sh"
git push
git status