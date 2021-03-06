import json
import os
import re
import subprocess
import time


def get_images_names():
    output = subprocess.check_output(['sudo', 'docker', 'images'])
    return re.findall(r'\n([0-9a-z]+)', output)


def run_container(name, command='/bin/bash'):
    # subprocess.call(['sudo', 'docker', 'run' , '-it', name, command])
    os.system(
            'gnome-terminal -e "sudo docker run -it {} {}"'.format(
                name, command))
    # subprocess.call([
        # 'gnome-terminal', '-e',
        # '"sudo docker run -it {} {}"'.format(name, command)])
        #

def restart_container(self, name):
    os.system(
            'gnome-terminal -e "sudo docker restart {}"'.format(name))


def bind_pipework(num, interface, base, ip1, ip2):
    # subprocess.call("sudo pipework br{} -i {} {} {}@{}".format(
        # num, interface, base, ip1, ip2))
    subprocess.call(['sudo', 'pipework', 'br'+str(num), '-i', interface,
        base, ip1, ip2])


def get_containers_names():
    output = subprocess.check_output(['sudo', 'docker', 'ps', '-a'])
    return re.findall(r'\n([0-9a-z]+)', output)


def inspect_container(name):
    data = json.loads(subprocess.check_output(
        ['sudo', 'docker', 'inspect', name]))[0]
    ip_address=  data['NetworkSettings']['IPAddress']
    status = data['State']['Status']
    # import ipdb; ipdb.set_trace()
    return {name: [ip_address, status]}
    #TODO: dokonczyc to!!!


def stop_container(name):
    pass


if __name__ == '__main__':
    print(get_images_names())

    print(run_container('myapache'))
    time.sleep(3)
    print(get_containers_names())
    print(inspect_container(get_containers_names()[0]))

    # bind_pipework(1, 'enp0s3', '63b7470be77c', '172.17.0.2/16', '172.17.0.1')
    # bind_pipework(2, 'enp0s3', '9f0f2af0797e', '172.17.0.3/16', '172.17.0.1')


# sudo pipework br1 -i enp0s3 63b7470be77c 172.17.0.2/16@172.17.0.1
# sudo pipework br2 -i enp0s3 9f0f2af0797e 172.17.0.3/16@172.17.0.1

