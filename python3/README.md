## What do we have here? 

A bunch of _truly_ random python scripts:  advent of code, project euler, machine learning + AI integrations, data visualization, etc.  

### Dependencies
* Usually requires common libs (maybe create a requirements.txt at some point?)
* Google API key

### Miscellenous 

Compile all with:
~~~
python3 -m compileall . -q -f
~~~

#### Windows 10
C:\Users/mike\Documents\WindowsPowerShell\profile.ps1
~~~
#region conda initialize
# !! Contents within this block are managed by 'conda init' !!
If (Test-Path "C:\Users\mike\miniconda3\Scripts\conda.exe") {
    (& "C:\Users\mike\miniconda3\Scripts\conda.exe" "shell.powershell" "hook") | Out-String | ?{$_} | Invoke-Expression
}
#endregion
~~~

### Luke coding

1. Tiger jython (some kind of IDE)
2. [tutorials link](https://python-online.ch/)
3. libs to import
* nicrobit
* neopixel 

### Basic environment management with conda & pip

~~~
conda init powershell
conda create -n first
conda create --name first -c conda-forge python=3.10
conda info --envs
conda activate first 
pip install -r ./requirements.txt
~~~

### Install Spyder IDE

Not recommended (better to do a seperate env - as written [here](https://docs.spyder-ide.org/current/installation.html))
~~~
pip install spyder numpy scipy pandas matplotlib sympy cython
~~~
