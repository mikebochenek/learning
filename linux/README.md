# Linux

Miscellaneous Linux learnings and utilities:
- commands.txt: sym links, services, filesystem, etc. 
- commands_presto.txt: compiling, git commands, app starts, stats, etc.

# Funny that
"My" local ubuntu doesn't have a root user (or at least one where I can do "su" to).  Instead, the recommend way is to always "sudo".  The funny bit is that I spent 10 minutes trying to remember the password!

# i3
A super neat window manager, which takes some time getting used to, but it has potential to improve productivity, or to be more exact, forces one to use the keyboard more and more.  Notes for myself:
- see [user manual](https://i3wm.org/docs/userguide.html)
- when logging in, select window manager using icon in top right
- alt+return opens new termindal
- alt+d search for executables
- alt+j/k/l to switch windows
- alt+f full screen
- alt+1/2/3 seperate desktops
- /usr/share/applications has links to other apps which cannot be found with alt+d (esp. visual code and sublime, etc.)
- ~/.config/i3/config
- already had a geany shortcut: bindsym $mod+Shift+g exec geany

### My ~/.config/i3/config 

~~~
...
bindsym $mod+Shift+f exec firefox
bindsym $mod+Shift+g exec geany
#bindsym $mod+Shift+j exec /home/mike/Tools/eclipse/java-2021-09/eclipse/eclipse
bindsym $mod+Shift+v exec /usr/share/code/code --unity-launch %F

# Start i3bar to display a workspace bar (plus the system information i3status
# finds out, if available)
bar {
        status_command i3status
}
~~~

