import cx_Oracle
import conf

DEBUG = False
connect_str = ''


def read_conf():
    global DEBUG
    DEBUG = conf.DEBUG

    global connect_str
    connect_str = conf.connect_str


def main():
    read_conf()
    conn = cx_Oracle.connect(connect_str)


if __name__ == '__main__':
    main()
