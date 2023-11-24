import requests
import os
import time
import execjs

if __name__ == "__main__":

    pwdUtil_js = """
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
    """
    # 自动连接wifi有延迟，这里等待连接完毕后执行
    time.sleep(20)
    pwdUtil = execjs.compile(pwdUtil_js)
    timeStamp = pwdUtil.call('getTimeStamp')
    encryptPwd = pwdUtil.call('do_encrypt_rc4', '3997', timeStamp)
    url = "http://1.1.1.4/ac_portal/login.php"
    form_data = {
        "opr": "pwdLogin",
        "userName": "3997",
        "pwd": encryptPwd,
        "auth_tag": timeStamp,
        "rememberPwd": 0
    }
    print(requests.post(url, data=form_data).content.decode("utf-8"))
    time.sleep(30)
    os.system("D:/toDesk/ToDesk.exe")

