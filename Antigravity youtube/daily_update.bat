@echo off
rem Switch to the project directory
cd /d "C:\Users\mikas\OneDrive\Antigravity youtube"

rem Log start time
echo ================================================== >> update_log.txt
echo [%date% %time%] Starting Daily Update Task... >> update_log.txt

rem Run the Python Orchestrator
rem Using 'python' assuming it's in the system PATH. 
rem If it fails, we might need the full path to python.exe
python src/orchestrator.py --batch --auto-approve >> update_log.txt 2>&1

rem Log end time
echo [%date% %time%] Task Finished. >> update_log.txt
echo ================================================== >> update_log.txt
