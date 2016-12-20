from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor
import ClientConnect
import GUI


class ClientConnectFactory(ClientFactory):
    def __init__(self):
        pass

    def startedConnecting(self, connector):
        print 'Menghubungkan ke server'

    def buildProtocol(self, addr):
        print 'Terhubung!'
        # myGUI = GUI.GUI(client)
        # myGUI.jalankan()
        return ClientConnect.ClientConnect()

    def clientConnectionLost(self, connector, reason):
        print 'Lost connection.  Reason:', reason
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed. Reason:', reason
        reactor.stop()
