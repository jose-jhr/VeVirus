Set WshShell = CreateObject("WScript.Shell")
WshShell.SendKeys "% "  ' Alt + Barra espaciadora
WScript.Sleep 100
WshShell.SendKeys "n"