## various (useful) commands

### uptime
~~~
wmic path Win32_OperatingSystem get LastBootUpTime
or
systeminfo | find "System Boot Time"
~~~

### execution policy
After setting up conda init, needed to allow scripts according to [this link](https:/go.microsoft.com/fwlink/?LinkID=135170)
~~~
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
~~~
