sudo gcc -fPIC -shared -o libmatmul.so mult_matrix.c

FILE=libmatmul.so

if test -f "$FILE"; then
    echo "SUCCESFUL: library is build"
else
    echo "ERROR: library is not build"
fi
