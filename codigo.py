from mininet.topo import Topo

class MyTopo( Topo ):
     "Create custom topo"

     def __init__(self):
          "Create custom topo."

          # Initialize topology
          Topo.__init__(self)

          leftHost = self.addHost('h1')
          leftHost1a = self.addHost('h2')
          Hosts2_a = self.addHost('h3')
          Hosts2_b = self.addHost('h4')
          Hosts3_a = self.addHost('h5')
          Hosts3_b = self.addHost('h6')
          rightHosts4_a = self.addHost('h7')
          rightHosts4_b = self.addHost('h8')
          rightHosts4_c = self.addHost('h9')
          leftSwitch = self.addSwitch('s1')
          centerSwitch1 = self.addSwitch('s2')
          centerSwitch2 = self.addSwitch('s3')
          rightSwitch = self.addSwitch('s4')

          self.addLink(leftHost, leftSwitch)
          self.addLink(leftHost1a, leftSwitch)
          self.addLink(Hosts2_a, centerSwitch1)
          self.addLink(Hosts2_b, centerSwitch1)
          self.addLink(Hosts3_a, centerSwitch2)
          self.addLink(Hosts3_b, centerSwitch2)
          self.addLink(rightHosts4_a, rightSwitch)
          self.addLink(rightHosts4_b, rightSwitch)
          self.addLink(rightHosts4_c, rightSwitch)


topos = {'mytopo': (lambda: MyTopo())}
