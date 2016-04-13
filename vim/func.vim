let nama = "vim"

function Say_hello()
    echo "Hello"
endfunction  

function Say(message)
    echo a:message
endfunction

function Kuadrat(x)
    return a:x * a:x
endfunction

function Global_test()
    echo g:nama
endfunction
