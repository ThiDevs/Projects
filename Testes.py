from selenium import webdriver
from mailthon.postman import Postman
from mailthon.middleware import TLS, Auth
from mailthon import email
import socket
import time
import threading


def email():
    postman = Postman(
        host='SOLLOES-VM02.SOLLOBRASIL.NET',
        port=587,
        middlewares=[
            TLS(force=True),
            Auth(username='thiagoalves', password='991010')
        ],
    )

    envelope = email(
        sender='sender <thiagoalves@sollobrasil.com.br>',
        receivers=['thiagoalves@sollobrasil.com.br'],
        subject='Manutenção/Suporte',
        content='',
    )
    response = postman.send(envelope)
    print(response.message)
    print(response.status_code)

    if response.ok:
        print("OK! :)")


def OpenSuper(driver):
    # Optional argument, if not specified will search path.
    driver.get(
        'http://172.16.0.82/hermes_net_v4/Supervision/Login.aspx?Id_Admin=1&Culture_inf=pt-BR&Oid_User=SDTUkosK&Oid_Company=GzOShAEK&Ws_Admin=http://172.16.0.82/hermes_net_v4/Admin/Web_Service/&Oid_Network=&Oid_Network_Agent=&Station=1');
    time.sleep(15)
    frame = driver.find_element_by_xpath('//*[@id="main"]')
    driver.switch_to.frame(frame)
    try:
        login_form = driver.find_element_by_xpath('//*[@id="Mnu_Files"]')
        login_form.click()
    except Exception:
        time.sleep(2)
        login_form = driver.find_element_by_xpath('//*[@id="Mnu_Files"]')
        login_form.click()

    time.sleep(4)
    try:
        login_form = driver.find_element_by_xpath('//*[@id="Files_Tr_Menu_Files_Open"]/td[2]/span')
        login_form.click()
    except Exception:
        time.sleep(2)
        login_form = driver.find_element_by_xpath('//*[@id="Files_Tr_Menu_Files_Open"]/td[2]/span')
        login_form.click()
    try:
        login_form = driver.find_element_by_xpath(
            '//*[@id="ctxList_panel"]/div[2]/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div/div')
        login_form.click()
    except Exception:
        time.sleep(2)
        login_form = driver.find_element_by_xpath(
            '//*[@id="ctxList_panel"]/div[2]/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div/div')
        login_form.click()

    login_form = driver.find_element_by_xpath('//*[@id="scrollTop_b2_1"]')
    login_form.click()
    login_form.click()
    login_form.click()
    time.sleep(4)
    login_form = driver.find_element_by_xpath('//*[@id="scrollDiv_1"]/div/div/div[16]/div')
    login_form.click()
    time.sleep(2)
    login_form = driver.find_element_by_xpath('//*[@id="ctxList_panel"]/div[4]/table/tbody/tr/td[1]/div')
    login_form.click()
    time.sleep(2)

    html_source = driver.page_source
    while (True):
        Nome_Operador = driver.find_element_by_xpath('//*[@id="Agent_agent_2"]/div[4]/div[2]/div[3]/div[5]/span').text
        Campanha_Operador = driver.find_element_by_xpath(
            '//*[@id="Agent_agent_2"]/div[4]/div[2]/div[8]/div[5]/span').text
        PC_Operador = driver.find_element_by_xpath(
            '// *[ @ id = "Agent_agent_2"] / div[4] / div[2] / div[4] / div[5] / span').text
        Duracao_Operador = driver.find_element_by_xpath(
            '// *[ @ id = "Agent_agent_2"] / div[4] / div[2] / div[6] / div[5] / div / span').text

        if Nome_Operador != "":
            if(Nome_Anterior != Nome_Operador):
                print("Opa")

        Dados = Nome_Operador + " " + PC_Operador + " " + Campanha_Operador + " " + Duracao_Operador

        Nome_Operador = driver.find_element_by_xpath('//*[@id="Agent_agent_2"]/div[4]/div[2]/div[3]/div[6]/span').text
        Campanha_Operador = driver.find_element_by_xpath(
            '//*[@id="Agent_agent_2"]/div[4]/div[2]/div[8]/div[6]/span').text
        PC_Operador = driver.find_element_by_xpath(
            '// *[ @ id = "Agent_agent_2"] / div[4] / div[2] / div[4] / div[6] / span').text
        Duracao_Operador = driver.find_element_by_xpath(
            '// *[ @ id = "Agent_agent_2"] / div[4] / div[2] / div[6] / div[6] / div / span').text
        Dados2 = Nome_Operador + " " + PC_Operador + " " + Campanha_Operador + " " + Duracao_Operador

        Dados = Dados + ";" + Dados2
        t3 = threading.Thread(target=connect2, args=(Dados,))
        t3.start()
        time.sleep(1)
        print(Dados)
        Nome_Anterior = Nome_Operador


def main():
    try:
        driver = webdriver.Chrome("C:\\Users\\redes\\Desktop\\chromedriver.exe")
        driver2 = webdriver.Chrome("C:\\Users\\redes\\Desktop\\chromedriver.exe")

        t1 = threading.Thread(target=OpenSuper, args=(driver,))
        t2 = threading.Thread(target=OpenSuper2, args=(driver2,))
        t1.start()
        t2.start()

    finally:
        driver.close()
        driver2.close()


def connect(Dados):
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # get local machine name
        host = socket.gethostname()
        print(socket.gethostbyname(socket.gethostname()))

        port = 9998

        # bind to the port
        serversocket.bind((host, port))

        # queue up to 5 requests
        serversocket.listen(5)

        # establish a connection
        clientsocket, addr = serversocket.accept()

        print("Got a connection from %s" % str(addr))
        msg = Dados + "\r\n"
        clientsocket.send(msg.encode('ascii'))

        clientsocket.close()

        print("Sai")
    except Exception:
        pass


def connect2(Dados):
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # get local machine name
        host = socket.gethostname()
        print(socket.gethostbyname(socket.gethostname()))

        port = 9999

        # bind to the port
        serversocket.bind((host, port))

        # queue up to 5 requests
        serversocket.listen(5)

        # establish a connection
        clientsocket, addr = serversocket.accept()

        print("Got a connection from %s" % str(addr))
        msg = Dados + "\r\n"

        with open('operadores.txt', 'a') as the_file:
            if " ;" or "; " or " ; " or "   ;   " not in Dados:
                the_file.write(Dados + '\n')

        clientsocket.send(msg.encode('ascii'))

        clientsocket.close()

        print("Sai")
    except Exception:
        pass


def OpenSuper2(driver3):
    # Optional argument, if not specified will search path.

    driver3.get(
        'http://172.16.0.86/hermes_net_v4/Supervision/Login.aspx?Id_Admin=1&Culture_inf=pt-BR&Oid_User=SDTXtCUK&Oid_Company=KOsWcAEK&Ws_Admin=http://172.16.0.86/hermes_net_v4/Admin/Web_Service/&Oid_Network=&Oid_Network_Agent=&Station=1')
    time.sleep(15)
    frame = driver3.find_element_by_xpath('//*[@id="main"]')
    time.sleep(5)
    driver3.switch_to.frame(frame)
    time.sleep(5)
    login_form = driver3.find_element_by_xpath('//*[@id="Mnu_Files"]')
    time.sleep(5)
    login_form.click()
    time.sleep(4)
    login_form = driver3.find_element_by_xpath('//*[@id="Files_Tr_Menu_Files_Open"]/td[2]/span')
    login_form.click()
    login_form = driver3.find_element_by_xpath(
        '//*[@id="ctxList_panel"]/div[2]/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div/div')
    login_form.click()
    time.sleep(2)
    login_form = driver3.find_element_by_xpath('//*[@id="scrollDiv_1"]/div/div/div[4]/div')
    login_form.click()
    time.sleep(2)
    login_form = driver3.find_element_by_xpath('//*[@id="ctxList_panel"]/div[4]/table/tbody/tr/td[1]/div')
    login_form.click()
    time.sleep(2)
    html_source = driver3.page_source
    while (True):
        Nome_Operador = driver3.find_element_by_xpath('//*[@id="Agent_agent_2"]/div[4]/div[2]/div[3]/div[5]/span').text
        Campanha_Operador = driver3.find_element_by_xpath(
            '//*[@id="Agent_agent_2"]/div[4]/div[2]/div[8]/div[5]/span').text
        PC_Operador = driver3.find_element_by_xpath('//*[@id="Agent_agent_2"]/div[4]/div[2]/div[6]/div[5]/span').text
        Duracao_Operador = driver3.find_element_by_xpath(
            '//*[@id="Agent_agent_2"]/div[4]/div[2]/div[5]/div[5]/div/span').text
        Dados3 = Nome_Operador + " " + PC_Operador + " " + Campanha_Operador + " " + Duracao_Operador

        Nome_Operador = driver3.find_element_by_xpath('//*[@id="Agent_agent_2"]/div[4]/div[2]/div[3]/div[6]/span').text
        Campanha_Operador = driver3.find_element_by_xpath(
            '//*[@id="Agent_agent_2"]/div[4]/div[2]/div[8]/div[6]/span').text
        PC_Operador = driver3.find_element_by_xpath('//*[@id="Agent_agent_2"]/div[4]/div[2]/div[6]/div[6]/span').text
        Duracao_Operador = driver3.find_element_by_xpath(
            '//*[@id="Agent_agent_2"]/div[4]/div[2]/div[5]/div[6]/div/span').text
        Dados2 = Nome_Operador + " " + PC_Operador + " " + Campanha_Operador + " " + Duracao_Operador
        #  connect()
        Dados3 = Dados3 + ";" + Dados2
        t4 = threading.Thread(target=connect, args=(Dados3,))
        t4.start()
        time.sleep(1)
        print(Dados3)


main()

time.sleep(10)