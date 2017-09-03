import oslo_config
import libvirt
def connect():  
    connection = libvirt.open("qemu:///system")
    return connection


conn = connect()

xml = ""  
with open("a.xml", "r") as file:  
    xml = file.read()

print xml
conn.defineXML(xml)  
