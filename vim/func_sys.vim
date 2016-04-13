let s:contents = readfile(expand('%'))
for i in s:contents
    echo i
endfor
