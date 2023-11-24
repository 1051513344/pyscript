

function getTimeStamp() {
    return +(new Date()) + '';
}
function do_encrypt_rc4(pwd, timestamp) {
    var i, j = 0, a = 0, b = 0, c = 0, temp;
    var plen = timestamp.length,
        size = pwd.length;

    var key = Array(256); //int
    var sbox = Array(256); //int
    var output = Array(size); //code of data
    for (i = 0; i < 256; i++) {
        key[i] = timestamp.charCodeAt(i % plen);
        sbox[i] = i;
    }
    for (i = 0; i < 256; i++) {
        j = (j + sbox[i] + key[i]) % 256;
        temp = sbox[i];
        sbox[i] = sbox[j];
        sbox[j] = temp;
    }
    for (i = 0; i < size; i++) {
        a = (a + 1) % 256;
        b = (b + sbox[a]) % 256;
        temp = sbox[a];
        sbox[a] = sbox[b];
        sbox[b] = temp;
        c = (sbox[a] + sbox[b]) % 256;
        temp = pwd.charCodeAt(i) ^ sbox[c];//String.fromCharCode(src.charCodeAt(i) ^ sbox[c]);
        temp = temp.toString(16);
        if (temp.length === 1) {
            temp = '0' + temp;
        } else if (temp.length === 0) {
            temp = '00';
        }
        output[i] = temp;
    }
    return output.join('');
}