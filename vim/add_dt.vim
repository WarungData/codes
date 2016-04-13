let s:now = strftime("%d-%m-%Y %H:%M:%S")
let s:lastline = line('$') + 1
call setline(s:lastline, s:now)
