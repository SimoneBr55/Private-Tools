# Private-Tools Package (pt)

>Simone Brazioli
--------------------------------

## Modules implemented


### bruteforcer (bf)

This module allows brute forcing credentials for different protocols.

#### Functions Implemented

```python3
ssh_brute_pass(server, user, <pass_list>, port=22)
```
This function assumes you know the user to ssh with and bruteforces the password. It uses 12 threads.

<br>

```python3
ssh_command(server, username, password, cmd='id', port=22)
```
Still not implemented.
Takes a command to pass in a SSH successful connection.

<br>

```python3
ssh(server, username, password, port=22, verbose=False)
```
Function called by other methods in ssh protocols methods.
It executes an SSH connection and outputs information if called with the verbose=True flag.
