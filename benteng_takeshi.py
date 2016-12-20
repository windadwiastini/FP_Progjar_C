from twisted.internet import reactor
import ClientConnectFactory


print "Masukkan alamat server"
address = raw_input()
print "Masukkan port"
port = int(raw_input())
c = ClientConnectFactory.ClientConnectFactory()
reactor.connectTCP(address, port, c)
reactor.run()