
io.write ('Menghitung akar kuadrat\n')
io.write ('Masukkan bilangan: ')
bil = io.stdin:read('*number')
io.write ('Anda memasukkan: ' .. bil .. '\n')
result = math.sqrt (bil)
io.write ('Akar kuadrat dari ' .. bil .. ' adalah ' .. result .. '\n')
