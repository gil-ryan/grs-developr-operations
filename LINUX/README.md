# Linux Terminal Commands

A lot of these reference will absolutely carry over for OSX's shell.

## IO

Windows utilizes backslashes (\), OSX/Linux uses forward slashes (/). Therefore if you want programs to execute properly on all operating systems, it would be wise to write so your programs handle both.

```bash
history | grep PYTHON
```

## Utilize SCP for Remote File Transfer

```
burt@burt NETMIKO % scp file.txt grs@192.168.1.150:/flash.txt
```