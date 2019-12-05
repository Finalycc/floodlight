#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6653)

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)

#disable ipv6
    h1.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
    h1.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
    h1.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")
    h2.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
    h2.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
    h2.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")
    h3.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
    h3.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
    h3.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")
    h4.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
    h4.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
    h4.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")
    
      
    s1.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
    s1.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
    s1.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")

    info( '*** Add links\n')
    net.addLink(s1, h2)
    net.addLink(s1, h3)
    net.addLink(s1, h4)
    net.addLink(h1, s1)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

