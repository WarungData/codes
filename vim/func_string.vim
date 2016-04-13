let s:a="Halo Apa Kabar"

echo "Panjang string '" . s:a . "' adalah " . strlen(s:a)

let s:b = toupper(s:a)
echo "B = " . s:b

let s:c = tolower(s:a)
echo "C = " . s:c

echo "Nama file: "  . expand('%')
