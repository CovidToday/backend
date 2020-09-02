call F:\Anaconda3\Scripts\activate.bat
python unified_districts_metrics.py
git pull 
git status
git add --all
git commit -m "Updated on %date%"
git push --all
echo TODAY'S UPDATE IS COMPLETE 
shutdown /s
