## various (useful) commands

### uptime
~~~
wmic path Win32_OperatingSystem get LastBootUpTime
or
systeminfo | find "System Boot Time"
~~~

Can be also added to profile.ps as shown below
~~~
Function uptime {
	wmic path Win32_OperatingSystem get LastBootUpTime 
	systeminfo | find "System Boot Time"
}
~~~

### execution policy
After setting up conda init, needed to allow scripts according to [this link](https:/go.microsoft.com/fwlink/?LinkID=135170)
~~~
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
~~~

### visual code studio shortcuts + tips&tricks
To switch between *terminal* and *code editor* try [ref link](https://superuser.com/questions/1270103/how-to-switch-the-cursor-between-terminal-and-code-in-vscode)
* to go to the terminal: Ctrl + ~ 
* to go back to the editor: Ctrl + 1 

Also good to check Release Notes (re: AI / agents / code assist etc.)
