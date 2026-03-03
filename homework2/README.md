# How to Run Homework 2 Server
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

### 4. Locate the "App" button on the DevEdu dashboard
1. Navigate to Devedu.io 
2. Ensure container is running
3. Locate the light-blue "App" button beside the dark-blue "Editor" button
<br></br>

# How to run tests
### 1. Ensure virtual environment is still active
```bash
# Command line will start with '(venv)'
(venv) student@cs4300-21-6d9c576d5-snnw7:~/cs4300/homework2$ 
```

### 2. Ensure you're inside the correct directory with the 'manage.py'
```bash
ls
```
### 3. Run the tests script (unit and integration)
```bash
python3 manage.py tests
```

### 4. Run the behave test script (BDD)
#### 1. Move to correct directory
macOS/Linux  
```bash 
cd ~/cs4300/homework2/tests
```
Windows  
```bash
cd %USERPROFILE%\cs4300\homework2\tests
```
#### 2. Run the behave command  
```bash
behave
```
-----------------------
# Important Note
Tutorial(s) used: https://www.youtube.com/playlist?list=PL-2EBeDYMIbSXhV8FMC1hVD32Fi6e4l2u  
HTML and CSS Files were made with the assistance of Claude AI.  
Troubleshooting done via Claude AI and Pardot AI.
