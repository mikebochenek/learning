---
layout: post
title:  "Rebuilding my 10 year old HP laptop"
date:   2024-12-29 15:43:01
categories: idea
---

One of my colleagues always quotes Hillary Clinton: _never waste a good crisis_.  And my laptop rebuild started with a small crisis, because my Mac is not longer a viable option to citrix into my work environment (long story)

## The path less travelled
Below is what I had to do over the last two days to upgrade the laptop.
1. physically re-install _original_ harddisk which contained Windows 8.  I was hoping it would already have version 10 or at least 8.1, but alas that wasn't the case
2. allow automatic updates (literally took all of 25th)
3. try to install Windows 10 using update center (failed because device unsupported)
4. sign up for _Windows Insider_ program, and download both Windows 10 and 11 ISO images
5. attempt to install Windows 11 Insider directly (fail because of missing TPM and processor too slow)
6. attempt to install Windows 10 Insider (failed half way because safe boot mode was not enabled - enable in BIOS afterwards)
7. Install Windows 10 Insider, and immediately try Citrix

## List of installed applications
At first I wanted to keep the install very minimal, but I quickly got carried away, when I realized that the performance is actually half decent.
| software  | version   | comment  |
| --------- | --------- | -------- |
| Brave | BraveBrowserSetup-BRV011.exe | a "secure" browser | 
| Citrix | CitrixWorkspaceApp.exe | needed for work | 
| DiskInternals Linux Reader | Linux_Reader 4.22.5 | access _old_ linux SSDs |
| FTP client | FileZilla_3.68.1_win64_sponsored2-setup.exe | manage bochenek domain | 
| Firefox | Firefox Installer.exe | a "secure" browser | 
| git | Git-2.47.1-64-bit.exe | coding | 
| golang | go1.23.4.windows-amd64 | coding |
| citrix add-on | HDX_RealTime_Media_Engine_2.9.600_for_Windows.msi | needed for work | 
| java | jdk-21_windows-x64_bin.exe | coding | 
| KeePass | KeePass-2.57.1-Setup.exe | password management | 
| LibreOffice | LibreOffice_24.8.4_Win_x86-64.msi | edit books read etc. | 
| python | Miniconda3-latest-Windows-x86_64.exe | coding | 
| notepad++ | npp.8.7.5.Installer.x64.exe | because it's fast |
| ownCloud | ownCloud-5.3.1.14018.x64.msi | sync files | 
| ruby | rubyinstaller-devkit-3.3.6-2-x64.exe | blog authoring | 
| mail client | Thunderbird Setup 128.5.2esr.exe | download bochenek emails | 
| visual code studio | VSCodeUserSetup-x64-1.96.2.exe | coding | 

Along the way discovered new features such as FTP+Thunderbird minimize to tray (and also Thunderbird chat integration with matrix + IRC)

## Conclusion
It almost felt like a mini Christmas present for myself, because it somehow worked, and brought me joy :-)

I think a small part why I felt happy is because it's good for the environment, and also because re-installing the workspace from scratch allows me to keep an minimal workspace (just how I want it)

Maybe next I can try to re-purpose my old iPad?  despite being 13-14 years old, I was able to browse the internet this month, so maybe no change really required.