import paramiko
def ssh(server, username, password, command='id'):
    try:
        port = '22'
        
        client = paramiko.SSHClient()
         
        # here we are loading the system
        # host keys
#        client.load_system_host_keys()
	 
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
         
        # connecting paramiko using host
        # name and password
        client.connect(server, port=22, username=username,
                       password=password)
         
        # below line command will actually
        # execute in your remote machine
        (stdin, stdout, stderr) = client.exec_command(command)
         
        # redirecting all the output in cmd_output
        # variable
        cmd_output = stdout.read()
        print('log printing: ', command, cmd_output)
         
        # we are creating file which will read our
        # cmd_output and write it in output_file
        #with open(output_file, "w+") as file:
        #    file.write(str(cmd_output))
             
        # we are returning the output
        #return output_file
    except:
        exit()
    finally:
        client.close()
 
 
#paramiko_GKG('172.17.0.2', 'id')
