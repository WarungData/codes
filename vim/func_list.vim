let s:a = [1, 2, 3, "vim"]
let s:b = [6, 5, 7, 0]


echo "A: " . string(s:a)
echo "B: " . string(s:b)

for i in range(1, 5)
        let s:a = add(s:a, i)
endfor
echo "NEW A: " . string(s:a)
