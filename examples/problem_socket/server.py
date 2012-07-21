# coding: utf-8
import sys
import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 5000))
    s.listen(5)
    try:
        while True:
            conn, addr = s.accept()
            buf = ""
            while True:
                buf += conn.recv(1024)
                if '\n' in buf:
                    line, buf = buf.split('\n', 1)
                    bits = line.split('+')
                    result = reduce(lambda a, b: a + b, map(int, bits))
                    conn.send("%d\n" % result)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == '__main__':
    main()
