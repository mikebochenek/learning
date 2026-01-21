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

#### directory structure

Although it can change, may be useful to show as an overview
~~~
├───advent_of_code_2020
│   └───data
├───aoc2019
├───aoc2022
├───aoc2023
├───aoc2025
├───basics
├───gen_ai
├───puzzles
├───streamlit
│   └───.streamlit
├───try_uv
└───__pycache__
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
(back in '24 or '25 ?)
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
Note that basing new env off '-c conda-forge python=3.10' is important, because it resolves this versioning issue: AttributeError: module 'matplotlib.cbook' has no attribute 'MatplotlibDeprecationWarning'

##### other tools

At some point need to check either *poetry* or *uv* (which are supposedly better!)

~~~
cargo install --locked uv
~~~


### Install Spyder IDE

Not recommended (better to do a seperate env - as written [here](https://docs.spyder-ide.org/current/installation.html))
~~~
pip install spyder numpy scipy pandas matplotlib sympy cython
pip install jupyter

jupyter notebook
~~~

##### New Spyder version

Run the following command or commands in the Anaconda prompt to update manually:
~~~
conda install -c defaults spyder=6.1.0
~~~

Since you installed Spyder with Anaconda, please don't use pip to update it as that will break your installation.  For more information, visit our <a href="https://docs.spyder-ide.org/current/installation.html">installation guide</a>.

