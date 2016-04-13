let s:a = {'nama' : 'vim', 'versi': 7, 'web': 'http://www.vim.org'}

let s:akey = keys(s:a)
for i in s:akey
        echo i . ' : ' . s:a[i]
endfor
          
