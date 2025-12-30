---
layout: post
title:  "Laptop restore"
date:   2025-12-27 09:37:04
categories: idea
---

What's the best way to spend a short holiday at home?  Restore an old laptop and enjoy the simplicity!...

This went amazingly fast:  all I had to do is re-install the previous SSD and disable secure boot.  It literally took less than an hour, and I picked December 25th to do it.

## Software
See table below (super weird that below blank space is required for parser!)

| software | new HP on Windows 11 | old HP running Ubuntu 18.04.6 LTS |
| --- | --- | --- | 
| OS | Windows_NT x64 10.0.26200 | Linux x64 4.15.0-213-generic | 
| Visual Studio Code | 1.107.1 | 1.85.1 | 
| git | 2.51.0 | 2.17.1 | 
| python | 3.13.5 | 3.10.9 | 
| golang | 1.25.1 | 1.10.4 |
| rust | 1.92.0 | 1.65.0 | 
| java | 17.0.14 | 17.0.5 |
| ruby | 3.4.7 | 2.5.1 | 

## Command Line

{%highlight bash %}
(base) mike@hp:~$ python
Python 3.10.9 (main, Mar  1 2023, 18:23:06) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
(base) mike@hp:~$ cargo -V
cargo 1.65.0
(base) mike@hp:~$ go version
go version go1.10.4 linux/amd64
(base) mike@hp:~$ date
Thu Dec 25 14:08:45 CET 2025
(base) mike@hp:~$ 

(base) mike@hp:~/Documents/code/learning/python3/gen-ai$ python claude_says1.py 
System boot time: 2025-12-25 13:56:22
System uptime: 0 days, 0 hours, 17 minutes, 45 seconds

(base) mike@hp:~/Documents/code/learning/go$ go run hello.go 

hello world! with fmt [ 2025-12-25 14:15:11.113095341 +0100 CET m=+0.001804110 ]
2025/12/25 14:15:11 
hello world! with log [ 2025-12-25 14:15:11.113095341 +0100 CET m=+0.001804110 ]
(base) mike@hp:~/Documents/code/learning/go$ 


  this version of Cargo is older than the `2024` edition, and only supports `2015`, `2018`, and `2021` editions.


  Finished dev [unoptimized + debuginfo] target(s) in 21m 33s


(base) mike@hp:~/Documents/code/learning/python3$ python stonks-0.py 
2025-12-25 14:17:55,254 - INFO - <-- LOAD local ticker cache: /home/mike/Documents/opendata/ticker/MSFT.pickle
2025-12-25 14:17:55,341 - INFO - <-- LOAD local ticker cache: /home/mike/Documents/opendata/ticker/NVDA.pickle
2025-12-25 14:17:57,732 - ERROR - Failed to get ticker 'UBS' reason: Expecting value: line 1 column 1 (char 0)
2025-12-25 14:17:57,741 - ERROR - $UBS: possibly delisted; no timezone found
2025-12-25 14:17:57,743 - INFO - --> SAVE to local pickle cache: /home/mike/Documents/opendata/ticker/UBS.pickle
2025-12-25 14:17:58,212 - ERROR - Failed to get ticker 'BTC-USD' reason: Expecting value: line 1 column 1 (char 0)
2025-12-25 14:17:58,215 - ERROR - $BTC-USD: possibly delisted; no timezone found
2025-12-25 14:17:58,218 - INFO - --> SAVE to local pickle cache: /home/mike/Documents/opendata/ticker/BTC-USD.pickle
2025-12-25 14:17:58,861 - ERROR - Failed to get ticker 'SOL-USD' reason: Expecting value: line 1 column 1 (char 0)
2025-12-25 14:17:58,863 - ERROR - $SOL-USD: possibly delisted; no timezone found
2025-12-25 14:17:58,865 - INFO - --> SAVE to local pickle cache: /home/mike/Documents/opendata/ticker/SOL-USD.pickle
2025-12-25 14:17:59,470 - ERROR - Failed to get ticker 'ETH' reason: Expecting value: line 1 column 1 (char 0)
2025-12-25 14:17:59,476 - ERROR - $ETH: possibly delisted; no timezone found
2025-12-25 14:17:59,478 - INFO - --> SAVE to local pickle cache: /home/mike/Documents/opendata/ticker/ETH.pickle
2025-12-25 14:18:00,221 - ERROR - Failed to get ticker 'CHFCAD=X' reason: Expecting value: line 1 column 1 (char 0)
2025-12-25 14:18:00,224 - ERROR - $CHFCAD=X: possibly delisted; no timezone found
2025-12-25 14:18:00,228 - INFO - --> SAVE to local pickle cache: /home/mike/Documents/opendata/ticker/CHFCAD=X.pickle
2025-12-25 14:18:00,963 - ERROR - Failed to get ticker 'CHFJPY=X' reason: Expecting value: line 1 column 1 (char 0)
2025-12-25 14:18:00,969 - ERROR - $CHFJPY=X: possibly delisted; no timezone found
2025-12-25 14:18:00,973 - INFO - --> SAVE to local pickle cache: /home/mike/Documents/opendata/ticker/CHFJPY=X.pickle
2025-12-25 14:18:00,974 - INFO - 	 ->> all done: 0:00:05.720531
(base) mike@hp:~/Documents/code/learning/python3$ 
{%endhighlight%}


## Screenshots

![linux1]({{ site.url }}/img/dev_screenshots2/fract0.png)
<hr/>
![linux1]({{ site.url }}/img/dev_screenshots2/Screenshot%202024-07-07%20at%2019.25.58.png)
<hr/>
![linux1]({{ site.url }}/img/dev_screenshots2/Screenshot%202023-10-07%20at%2011.08.29.png)
<hr/>
![linux1]({{ site.url }}/img/dev_screenshots2/Screenshot%202024-02-18%20at%2015.25.22.png)
<hr/>
![linux1]({{ site.url }}/img/dev_screenshots2/Screenshot%202025-05-18%20082736.png)
<hr/>
![linux1]({{ site.url }}/img/dev_screenshots2/Screenshot%20from%202022-03-06%2009-59-22.png)
<hr/>
![linux1]({{ site.url }}/img/dev_screenshots2/Screenshot%20from%202024-02-18%2022-05-59.png)
<hr/>
![linux1]({{ site.url }}/img/dev_screenshots2/Screenshot%20from%202024-02-18%2022-27-45.png)
<hr/>
![linux1]({{ site.url }}/img/dev_screenshots2/Screenshot%20from%202024-04-14%2013-23-57.png)
<hr/>
![linux1]({{ site.url }}/img/dev_screenshots2/Screenshot%20from%202024-08-02%2023-22-49.png)
<hr/>
![linux1]({{ site.url }}/img/dev_screenshots2/Screenshot%20from%202024-09-22%2009-19-43.png)
<hr/>
![linux1]({{ site.url }}/img/dev_screenshots2/Screenshot%20from%202025-12-26%2013-26-45.png)
<hr/>
