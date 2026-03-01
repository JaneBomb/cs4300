# How to Run Homework 2
-----
### 1. Start virtual environment
```bash
source venv/bin/activate
```

### 2. Move to correct directory
macOS/Linux  
```bash 
cd ~/cs4300/homework2
```
Windows  
```bash
cd %USERPROFILE%\cs4300\homework2
```
### 3. Run the Django File (manage.py)
``` bash
python3 manage.py runserver 0.0.0.0:3000
```
<br></br>
-----------------------
# Important Note
Tutorial(s) used: https://www.youtube.com/playlist?list=PL-2EBeDYMIbSXhV8FMC1hVD32Fi6e4l2u
HTML Files were made with the assistance of AI.


## Static Files Issue
DevEdu proxy returns 404 for all /static/ requests (including Django admin CSS).
Using inline CSS as workaround. Full Django static files configuration is correct
and will work in production (Render) deployment.
Spent 2 hours talking to Pardot in Slack, and came to the above conclusion.