let s:start = 1
let s:end = line('$')
let s:content = getline(s:start, s:end)

let s:count = 1
for i in s:content
        let s:temp = printf("%03d: ", s:count) . i
        call setline(s:count, s:temp)
        let s:count += 1
endfor
