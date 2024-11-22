import random
import time
import math


def clear_console(times):
    print('\n' * times)


class PC:
    def __init__(self, id):
        self.id = id
        self.hostname = 'PC' + f'{self.id}'
        self.ipv4 = '0.0.0.0'
        self.mask = '0.0.0.0'
        self.mac = '0099.0000.0000'  #0099 is this project manufacturer tag for a MAC address


    def generate_mac(self):
        possible_var = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        # Generate 8 random characters
        random_chars = [random.choice(possible_var) for _ in range(8)]
        
        # Format the new MAC address
        new_mac_suffix = ''.join(random_chars[:4]) + '.' + ''.join(random_chars[4:])
        self.mac = f'0099.{new_mac_suffix}'
        
            

    def net_config(self):
        clear_console(200)
        while True:
            clear_console(1)
            command = input(f"{self.hostname}:\\Network\\> ")
            command_parts = command.split()
            
            if len(command_parts) > 1:
                main_command = command_parts[0]    
                options = command_parts[1:]    
            else:
                main_command = command

            if main_command == 'ipv4':
                if len(options) == 1:
                    target = options[0]
                    self.ipv4 == target

            elif main_command == 'sh':
                print('+----------------------------------------------------------+')
                print('|  IPV4                  MASK                    MAC       |')
                print(f'| {self.ipv4}              {self.mask}              {self.mac} |')
                print('+----------------------------------------------------------+')

            elif main_command == 'clear':
                clear_console(200)

            elif main_command == 'exit':
                self.commands()

            elif main_command == 'mask':
                if len(options) == 1:
                    target = options[0]
                    self.mask == target

            elif main_command == 'mac':
                if len(options) == 1:
                    target = options[0]
                    self.mac == target

            elif main_command == 'dhcp':
                if len(options) == 1:
                    target = options[0]
                    if target == 'on':
                        self.ipv4 = 'DHCP on'
                        self.mask = 'DHCP on'
                    elif target == 'off':
                        self.ipv4 = '0.0.0.0'
                        self.mask = '0.0.0.0'
                    else:
                        print('Invalid command')

            elif main_command.strip() == '': 
                    pass
                        
            else:
                print(f"Unknown command: {command}")


    def commands(self):
        self.generate_mac()
        hostname = self.hostname
        documents = ['secret.txt']
        clear_console(200)
        while True:
            clear_console(1)
            command = input(f"{hostname}:\\> ")
            command_parts = command.split()
            
            if len(command_parts) > 1:
                main_command = command_parts[0]    
                options = command_parts[1:]    
            else:
                main_command = command  

            if main_command == '?' or main_command == 'help':
                print('HOSTNAME = Change the computer name\nPING = Send packets to a device\nLS = List all of the directory elements')


            elif main_command == 'net':
                self.net_config()

            elif main_command == 'hostname':
                if len(options) == 1:
                    target = options[0]
                    hostname = target
        
            elif main_command == 'ping':
                if len(options) == 1:  
                    target = options[0]
                    print(f"Pinging {target}...")
                else:
                    print("Usage: ping <IP address>")
        
            elif main_command == 'clear':
                clear_console(200)
        
            elif main_command == 'ls':
                print("Listing directory contents...")
                for document in documents:
                    print(document,'|', time.ctime())

            elif main_command == 'cat':
                if len(options) == 1:
                    target = options[0]
                    if target == 'secret.txt':
                        print('You found me !')
        
            elif main_command == '': 
                pass
            
            else:
                print(f"Unknown command: {command}")

    
'''
a = PC(1)
a.commands()
'''

