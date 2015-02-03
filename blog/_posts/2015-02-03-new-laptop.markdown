---
layout: post
title:  "New laptop"
date:   2015-01-03 23:13:22
categories: coding
---

After roughly 9 even years of quality usage of my old HP laptop, I have finally decided to get a new one.

- Product Name: HP 17-f115nz
- Product Number: K6Y75EA
- Microprocessor: Intel Pentium N3540 with Intel HD Graphics (2.16 GHz, 2 MB cache, 4 cores)
- Memory: 8 GB 1333 MHz DDR3 SDRAM (1 x 8 GB)
- Video Graphics: Intel HD Graphics
- Hard Drive: 500 GB 5400 rpm SATA (immediately replaced with Samsung EVO 840 Serie 250GB Sata-III SSD
- Multimedia Drive: SuperMulti DVD burner
- Display: 43.9 cm (17.3") diagonal HD+ BrightView WLED-backlit (1600 x 900)
- Network Card: Integrated 10/100 BASE-T Ethernet LAN
- Wireless Connectivity: 802.11b/g/n (1x1) and Bluetooth 4.0 combo (Miracast compatible)
- Sound: BeatsAudio with 2 speakers
- Keyboard: Full-size island-style keyboard with integrated numeric keypad
- Pointing Device: HP Imagepad with multi-touch gesture support
- External Ports: 1 multi-format SD media card reader, 1 HDMI, 1 headphone/microphone combo, 1 USB 2.0, 2 USB 3.0, 1 RJ-45
- Dimensions: 41.95 x 27.9 x 2.77 cm
- Weight: 2.82 kg
- Power: 45 W AC power adapter, 4-cell, 41 Wh Li-ion polymer
- Camera: HP TrueVision HD Webcam (front-facing) with integrated dual array digital microphone

And here is a link to where I got it: [Fust shop](http://www.fust.ch/de/p/pc-tablet-handy/notebook-macbook/notebook-17/pavilion-17-f115nz-8153425.html)

The computer is super fast, especially since its running Linux Mint 17.  Some basic performance tests show:
{%highlight bash linenos %}
sudo hdparm -Tt /dev/sda

/dev/sda:
 Timing cached reads:   2936 MB in  2.00 seconds = 1468.34 MB/sec
 Timing buffered disk reads: 802 MB in  3.01 seconds = 266.78 MB/sec
{%endhighlight%}
{%highlight bash linenos %}
dd if=/dev/zero of=/tmp/output bs=8k count=10k; rm -f /tmp/output
10240+0 records in
10240+0 records out
83886080 bytes (84 MB) copied, 0,210048 s, 399 MB/s
{%endhighlight%}

![new laptop]({{ site.url }}/blog/downloads/new-laptop.png)
