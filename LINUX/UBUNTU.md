# Ubuntu

I caught a couple of bugs immediately using __vi__ in Ubuntu VMware Workstation 15. I
 don't know why I'm mentioning that here, but I needed to put it somewhere.

## Terminal

### Remove PWD from Terminal

First thing that didn't sit exactly well with me is the PWD sitting on your terminal
line. In some cases that could be useful, but I already has such a long path that it
would immediately cause a carriage return for any shell type command entered. So to r
emove it :

```terminal
grs@ubuntu:$ vi ~/.bashrc
```

You'll see a line in there that goes somewhat like this:

> PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '

You'll just need to remove the __\w__.


