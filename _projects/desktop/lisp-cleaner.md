---
layout: page
title: Lisp Cleaner
subtitle: Get rid of lisp viruses easily!
redirect_from: /projects/lspcleaner/
youtube: true
---

<p class="lead">
Get rid of acaddoc.lsp virus on your computer and servers. Also cleans all acad.lsp and other AutoCAD related worms.
</p>

{% include youtube.html video_id="Lek-LEWX_Ew" %}

## What is Lisp Cleaner

LspCleaner is a small application to clear viruses from your AutoCAD lisp files. To start the clearing process, just press "*Auto Scan*" button. Application will scan all the AutoCAD related folders and it will remove virus data from the lisp files. If you want to scan a specific folder use "*Scan Folder*" option.

<p class="btn-wrap"><a class="btn btn-lg btn-success btn-inline" href="https://sourceforge.net/projects/lispcleaner/files/latest/download/" rel="noopener" target="\_blank">Download Lisp Cleaner</a></p>

> **Note :** Please disable your anti-virus software before running cleaner. Otherwise your software may think Lisp Cleaner is a virus, because it reaches files with the virus.

## Lisp Cleaner Features

![Lisp Cleaner Banner](/assets/img/projects/lisp-cleaner/lisp-cleaner-banner3.png "Lisp Cleaner")

* **Fast & Effective**  
  Clears all autoCAD related folders automatically
* **Full Automatic Scan**  
  Scans program files, your desktop and user folders
* **Protective Removal**  
  Unlike antivirus software, Lisp cleaner only harmful parts of lisp files
* **Custom Scan**  
  Using *Scan Folder* option, you can scan any folder, even network folders

## Command Line Arguments

Lisp Cleaner can be run in background using command line or batch scripts at computer start-up.

    C:\Path\to\lisp\cleaner\lspcleaner.exe /auto /nobackup

Following command line switches are available:

+ `/auto` : Enables silent mode. When added after the link, it automatically searches relevant directories and clears possible errors.
+ `/nobackup` : This argument disables automatically generated back-up files. Normally lisp cleaner back-ups all lisp files before removing virus.

## Posts about Lisp Cleaner

{% include tagloop.html tag="lispcleaner" %}
