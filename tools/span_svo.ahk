#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#IfWinActive ahk_class Notepad
$s::
Send, ^x
Send, <span class="subj">
Send, ^v
Send, </span>
return

$d::
Send, ^x
Send, <span class="obj">
Send, ^v
Send, </span>
return

$v::
Send, ^x
Send, <span class="verb">
Send, ^v
Send, </span>
return

$a::
Send, ^x
Send, <span class="aux">
Send, ^v
Send, </span>
return

$c::
Send, ^x
Send, <span class="comp">
Send, ^v
Send, </span>
return