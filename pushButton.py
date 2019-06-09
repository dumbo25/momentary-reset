Last login: Sun Jan 14 10:05:48 2018 from macbook-pro.attlocal.net
osmc@osmc-bens-room:~$ ls
Movies  Music  Pictures  TV Shows
osmc@osmc-bens-room:~$ sudo shutdown -h 0
Shutdown scheduled for Fri 2019-06-07 20:05:48 CDT, use 'shutdown -c' to cancel.
osmc@osmc-bens-room:~$ Connection to osmc-bens-room closed by remote host.
Connection to osmc-bens-room closed.
Jeffs-MBP:~ jeff$ ssh osmc@osmc-fam ily-room
ssh: Could not resolve hostname osmc-fam: nodename nor servname provided, or not known
Jeffs-MBP:~ jeff$ ssh osmc@osmc-family-room
osmc@osmc-family-room's password: 
Linux osmc-family-room 4.14.78-4-osmc #1 SMP PREEMPT Wed Dec 12 17:58:11 UTC 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Jun  6 21:27:16 2019 from 192.168.1.224
osmc@osmc-family-room:~$ logout

Connection to osmc-family-room closed.
Jeffs-MBP:~ jeff$ ssh osmc@osmc-jeffs-study
ssh: Could not resolve hostname osmc-jeffs-study: nodename nor servname provided, or not known
Jeffs-MBP:~ jeff$ ssh osmc@osmc-jeffs-office
osmc@osmc-jeffs-office's password: 

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Apr  6 07:37:10 2019 from jeffs-mbp.attlocal.net
osmc@osmc-jeffs-office:~$ ls
Movies  Music  Pictures  TV Shows
osmc@osmc-jeffs-office:~$ logout







Connection to osmc-jeffs-office closed.
Jeffs-MBP:~ jeff$ ssh osmc@osmc-family-room
osmc@osmc-family-room's password: 
Linux osmc-family-room 4.14.78-4-osmc #1 SMP PREEMPT Wed Dec 12 17:58:11 UTC 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jun  8 10:20:24 2019 from 192.168.1.224
osmc@osmc-family-room:~$ ls
blue.png  ky8LT0D.png  Movies  Music  nebula.jpg  nebula.png  Pictures  TV Shows
osmc@osmc-family-room:~$ sudo ls /usr/bin
[					lzegrep
2to3					lzfgrep
2to3-2.7				lzgrep
2to3-3.5				lzless
addpart					lzma
addr2line				lzmainfo
apt					lzmore
apt-cache				manual-update
apt-cdrom				mapscrn
apt-config				mawk
apt-extracttemplates			mcookie
apt-ftparchive				md5sum
apt-get					md5sum.textutils
apt-get-noninteractive			mediacenter
apt-get-real				mesg
apt-key					migrate-pubring-from-classic-gpg
apt-mark				mkfifo
apt-real				mk_modmap
apt-sortpkgs				mode2
ar					mpris-proxy
arch					mtrace
arm-linux-gnueabihf-addr2line		myosmc-id-setup
arm-linux-gnueabihf-ar			myosmc-report-installs
arm-linux-gnueabihf-as			namei
arm-linux-gnueabihf-c++filt		nawk
arm-linux-gnueabihf-cpp			newgrp
arm-linux-gnueabihf-cpp-4.9		nice
arm-linux-gnueabihf-cpp-6		nl
arm-linux-gnueabihf-dwp			nm
arm-linux-gnueabihf-elfedit		nohup
arm-linux-gnueabihf-gcc			nproc
arm-linux-gnueabihf-gcc-4.9		nsenter
arm-linux-gnueabihf-gcc-6		nstat
arm-linux-gnueabihf-gcc-ar		ntfsdecrypt
arm-linux-gnueabihf-gcc-ar-4.9		ntpdc
arm-linux-gnueabihf-gcc-ar-6		ntpq
arm-linux-gnueabihf-gcc-nm		ntpsweep
arm-linux-gnueabihf-gcc-nm-4.9		ntptrace
arm-linux-gnueabihf-gcc-nm-6		numfmt
arm-linux-gnueabihf-gcc-ranlib		objcopy
arm-linux-gnueabihf-gcc-ranlib-4.9	objdump
arm-linux-gnueabihf-gcc-ranlib-6	od
arm-linux-gnueabihf-gcov		openssl
arm-linux-gnueabihf-gcov-4.9		pager
arm-linux-gnueabihf-gcov-6		painter.py
arm-linux-gnueabihf-gcov-dump		partx
arm-linux-gnueabihf-gcov-dump-6		passwd
arm-linux-gnueabihf-gcov-tool		paste
arm-linux-gnueabihf-gcov-tool-6		paste-log
arm-linux-gnueabihf-gprof		pathchk
arm-linux-gnueabihf-ld			pdb
arm-linux-gnueabihf-ld.bfd		pdb2.7
arm-linux-gnueabihf-ld.gold		pdb3
arm-linux-gnueabihf-nm			pdb3.5
arm-linux-gnueabihf-objcopy		peekfd
arm-linux-gnueabihf-objdump		performance_tuner
arm-linux-gnueabihf-pkg-config		perl
arm-linux-gnueabihf-python2.7-config	perl5.24.1
arm-linux-gnueabihf-python-config	perl5.24-arm-linux-gnueabihf
arm-linux-gnueabihf-ranlib		perlbug
arm-linux-gnueabihf-readelf		perldoc
arm-linux-gnueabihf-size		perlivp
arm-linux-gnueabihf-strings		perlthanks
arm-linux-gnueabihf-strip		pg
arm-unknown-linux-gnueabihf-pkg-config	pgrep
as					pico
awk					piconv
b2sum					pilconvert.py
base32					pildriver.py
base64					pilfile.py
basename				pilfont.py
bashbug					pilprint.py
bccmd					pinentry
bluemoon				pinentry-curses
bluetoothctl				pinky
bootctl					pip
btmon					pip2
busctl					pkaction
c2ph					pkcheck
c89					pkexec
c89-gcc					pkg-config
c99					pkill
c99-gcc					pkttyagent
calc_tickadj				pl2pm
captoinfo				player.py
catchsegv				pldd
cc					ply-image
c++filt					pmap
chacl					pod2html
chage					pod2man
chardet					pod2text
chardetect				pod2usage
chattr					podchecker
chcon					podselect
chfn					pr
chrt					prename
chsh					preseed
cifscreds				preseed-agent
ciptool					print
cksum					printenv
clear					printf
clear_console				prlimit
cmp					pronto2lirc
codepage				prove
comm					prtstat
compose					psfaddtable
connmanctl				psfgettable
corelist				psfstriptable
cpan					psfxtable
cpan5.24-arm-linux-gnueabihf		pstree
cpp					pstree.x11
cpp-4.9					pstruct
cpp-6					ptar
createfontdatachunk.py			ptardiff
c_rehash				ptargrep
crontab					ptx
csplit					pwdx
ctstat					py3clean
curl					py3compile
cut					py3versions
dbus-cleanup-sockets			pybuild
dbus-daemon				pyclean
dbus-monitor				pycompile
dbus-run-session			pydoc
dbus-send				pydoc2.7
dbus-update-activation-environment	pydoc3
dbus-uuidgen				pydoc3.5
deallocvt				pygettext
debconf					pygettext2.7
debconf-apt-progress			pygettext3
debconf-communicate			pygettext3.5
debconf-copydb				python
debconf-escape				python2
debconf-set-selections			python2.7
debconf-show				python2.7-config
deb-systemd-helper			python2-config
deb-systemd-invoke			python3
delpart					python3.5
dh_pypy					python3.5m
dh_python2				python3m
dh_python3				python-config
dialog					pyversions
diff					ranlib
diff3					raspi-config
dircolors				rcp
dirmngr					rctest
dirmngr-client				readelf
dirname					realpath
dpkg					remote-cli
dpkg-deb				rename
dpkg-divert				rename.ul
dpkg-maintscript-helper			renice
dpkg-query				reset
dpkg-split				resizepart
dpkg-statoverride			rev
dpkg-trigger				rfcomm
du					rgrep
dumpkeys				rlogin
dwp					routef
easy_install				routel
edit					rpcgen
editor					rpi-btuart
eject					rpi-update
elfedit					rsh
enc2xs					rtstat
encguess				runcon
enhancer.py				run-mailcap
env					savelog
expand					scp
expiry					screendump
explode.py				script
expr					scriptreplay
factor					sdiff
faillog					sdptool
fallocate				see
find					select-editor
flock					sensible-browser
fmt					sensible-editor
fold					sensible-pager
free					seq
ftr					setarch
gcc					setcifsacl
gcc-4.9					setfacl
gcc-6					setkeycodes
gcc-ar					setleds
gcc-ar-4.9				setlogcons
gcc-ar-6				setmetamode
gcc-nm					setsid
gcc-nm-4.9				setterm
gcc-nm-6				setvtrgb
gcc-ranlib				sftp
gcc-ranlib-4.9				sg
gcc-ranlib-6				sha1sum
gcov					sha224sum
gcov-4.9				sha256sum
gcov-6					sha384sum
gcov-dump				sha512sum
gcov-dump-6				shasum
gcov-tool				showconsolefont
gcov-tool-6				showkey
gencat					shred
getcifsacl				shuf
getconf					size
getent					skill
getfacl					slabtop
getkeycodes				slogin
getopt					snice
gifmaker.py				sntp
gold					sort
gpasswd					sotruss
gpg					splain
gpg-agent				split
gpgconf					splitfont
gpg-connect-agent			sprof
gpgparsemail				ssh
gpgsplit				ssh-add
gpgv					ssh-agent
gpg-zip					ssh-argv0
gprof					ssh-copy-id
grab-logs				ssh-keygen
groups					ssh-keyscan
h2ph					start-network
h2xs					stat
hattrib					stdbuf
hcd					strings
hciattach				strip
hciconfig				sudo
hcidump					sudoedit
hcitool					sudoreplay
hcopy					sum
hdel					symcryptrun
hdir					systemd-analyze
head					systemd-cat
hex2hcd					systemd-cgls
hformat					systemd-cgtop
hls					systemd-delta
hmkdir					systemd-detect-virt
hmount					systemd-mount
host					systemd-path
hostid					systemd-resolve
hostnamectl				systemd-run
hpwd					systemd-socket-activate
hrename					systemd-stdio-bridge
hrmdir					tabs
http-time				tac
humount					tail
hvol					taskset
iconv					tee
id					test
infocmp					TexturePacker
infotocap				thresholder.py
install					tic
instmodsh				timedatectl
ionice					timeout
ipcmk					tload
ipcrm					toe
ipcs					top
iptables-xml				touch
ircat					tput
irexec					tr
ir-keytable				truncate
irpty					tset
irrecord				tsort
irsend					tty
irw					tzselect
ischroot				ucf
join					ucfq
json_pp					ucfr
kbdinfo					udisks
kbxutil					udisks-glue
kernel-install				udisks-tcp-bridge
killall					unexpand
kodi					unicode_stop
kodi-send				uniq
kodi-standalone				unlink
l2ping					unlzma
l2test					unshare
last					unxz
lastb					update-alternatives
lastlog					update-leap
lcf					uptime
ld					users
ld.bfd					utmpdump
ldd					viewer.py
ld.gold					vmstat
less					volname
lessecho				w
lessfile				wall
lesskey					watch
lesspipe				watchgnupg
libnetcfg				wc
line					wget
link					whereis
linux32					which
linux64					who
lircrcd					whoami
lnstat					wpa_passphrase
loadkeys				w.procps
loadunimap				xargs
locale					xbmc-send
localectl				xsubpp
localedef				xz
logger					xzcat
logname					xzcmp
lsattr					xzdiff
lscpu					xzegrep
lsipc					xzfgrep
lslocks					xzgrep
lslogins				xzless
lsns					xzmore
lspgpot					yes
lzcat					zdump
lzcmp					zipdetails
lzdiff
osmc@osmc-family-room:~$ sudo ls /usr/bin/p*
/usr/bin/pager			       /usr/bin/pip2	       /usr/bin/pstree
/usr/bin/painter.py		       /usr/bin/pkaction       /usr/bin/pstree.x11
/usr/bin/partx			       /usr/bin/pkcheck        /usr/bin/pstruct
/usr/bin/passwd			       /usr/bin/pkexec	       /usr/bin/ptar
/usr/bin/paste			       /usr/bin/pkg-config     /usr/bin/ptardiff
/usr/bin/paste-log		       /usr/bin/pkill	       /usr/bin/ptargrep
/usr/bin/pathchk		       /usr/bin/pkttyagent     /usr/bin/ptx
/usr/bin/pdb			       /usr/bin/pl2pm	       /usr/bin/pwdx
/usr/bin/pdb2.7			       /usr/bin/player.py      /usr/bin/py3clean
/usr/bin/pdb3			       /usr/bin/pldd	       /usr/bin/py3compile
/usr/bin/pdb3.5			       /usr/bin/ply-image      /usr/bin/py3versions
/usr/bin/peekfd			       /usr/bin/pmap	       /usr/bin/pybuild
/usr/bin/performance_tuner	       /usr/bin/pod2html       /usr/bin/pyclean
/usr/bin/perl			       /usr/bin/pod2man        /usr/bin/pycompile
/usr/bin/perl5.24.1		       /usr/bin/pod2text       /usr/bin/pydoc
/usr/bin/perl5.24-arm-linux-gnueabihf  /usr/bin/pod2usage      /usr/bin/pydoc2.7
/usr/bin/perlbug		       /usr/bin/podchecker     /usr/bin/pydoc3
/usr/bin/perldoc		       /usr/bin/podselect      /usr/bin/pydoc3.5
/usr/bin/perlivp		       /usr/bin/pr	       /usr/bin/pygettext
/usr/bin/perlthanks		       /usr/bin/prename        /usr/bin/pygettext2.7
/usr/bin/pg			       /usr/bin/preseed        /usr/bin/pygettext3
/usr/bin/pgrep			       /usr/bin/preseed-agent  /usr/bin/pygettext3.5
/usr/bin/pico			       /usr/bin/print	       /usr/bin/python
/usr/bin/piconv			       /usr/bin/printenv       /usr/bin/python2
/usr/bin/pilconvert.py		       /usr/bin/printf	       /usr/bin/python2.7
/usr/bin/pildriver.py		       /usr/bin/prlimit        /usr/bin/python2.7-config
/usr/bin/pilfile.py		       /usr/bin/pronto2lirc    /usr/bin/python2-config
/usr/bin/pilfont.py		       /usr/bin/prove	       /usr/bin/python3
/usr/bin/pilprint.py		       /usr/bin/prtstat        /usr/bin/python3.5
/usr/bin/pinentry		       /usr/bin/psfaddtable    /usr/bin/python3.5m
/usr/bin/pinentry-curses	       /usr/bin/psfgettable    /usr/bin/python3m
/usr/bin/pinky			       /usr/bin/psfstriptable  /usr/bin/python-config
/usr/bin/pip			       /usr/bin/psfxtable      /usr/bin/pyversions
osmc@osmc-family-room:~$ sudo ls /usr/bin/pow*
ls: cannot access '/usr/bin/pow*': No such file or directory
osmc@osmc-family-room:~$ ls
blue.png  ky8LT0D.png  Movies  Music  nebula.jpg  nebula.png  Pictures  TV Shows
osmc@osmc-family-room:~$ sudo crontab -e
No modification made
osmc@osmc-family-room:~$ ls /etc/init.d
avahi-daemon            killprocs              openvpn            skeleton
bootlogs                kmod                   power_ring_led.sh  ssh
bootmisc.sh             motd                   procps             sudo
checkfs.sh              mountall-bootclean.sh  rc                 udev
checkroot-bootclean.sh  mountall.sh            rc.local           ufw
checkroot.sh            mountdevsubfs.sh       rcS                umountfs
cron                    mountkernfs.sh         README             umountnfs.sh
dbus                    mountnfs-bootclean.sh  reboot             umountroot
fake-hwclock            mountnfs.sh            rmnologin          urandom
halt                    nagios-nrpe-server     rpcbind
hostname.sh             nfs-common             sendsigs
hwclock.sh              ntp                    single
osmc@osmc-family-room:~$ sudo cat /etc/init.d/power_ring_led.sh
#!/bin/sh
### BEGIN INIT INFO
# Provides:          scriptname
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

# Starts and stops power_ring_led.py
# Directory: /etc/init.d/power_ring_led.sh
# Permsissions: chmod 755 /etc/init.d/power_ring_led.sh

# Start or stop power_ring_led.py
case "$1" in
  start)
    /usr/local/bin/power_ring_led.py --light &
    ;;
  stop)
    /usr/local/bin/power_ring_led.py --off &
    ;;
  *)
    echo "Usage: /etc/init.d/power_ring_led.sh {start|stop}"
    exit 1
    ;;
esac
exit
osmc@osmc-family-room:~$ ls /usr/local/bin/pow*
/usr/local/bin/power_ring_led.py
osmc@osmc-family-room:~$ sudo nano /usr/local/bin/power_ring_led.py
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ sudo nano /usr/local/bin/power_ring_led.py
osmc@osmc-family-room:~$ sudo nano /usr/local/bin/power_ring_led.py
osmc@osmc-family-room:~$ which python3
/usr/bin/python3
osmc@osmc-family-room:~$ sudo nano /usr/local/bin/power_ring_led.py
osmc@osmc-family-room:~$ cp /usr/local/bin/power_ring_led.py .
osmc@osmc-family-room:~$ ls
blue.png     Movies  nebula.jpg  Pictures           TV Shows
ky8LT0D.png  Music   nebula.png  power_ring_led.py
osmc@osmc-family-room:~$ mv power_ring_led.py pushButton.py
osmc@osmc-family-room:~$ ls
blue.png     Movies  nebula.jpg  Pictures       TV Shows
ky8LT0D.png  Music   nebula.png  pushButton.py
osmc@osmc-family-room:~$ python3 pushButton.py
Traceback (most recent call last):
  File "pushButton.py", line 30, in <module>
    import RPi.GPIO as GPIO
ImportError: No module named 'RPi'
osmc@osmc-family-room:~$ pip install rpi.gpio
Collecting rpi.gpio
  Downloading https://files.pythonhosted.org/packages/af/2f/407b6e4cc8a0bdf434825a160bba1807991886b63cce16a5f1a6e1f24cdf/RPi.GPIO-0.6.5.tar.gz
Building wheels for collected packages: rpi.gpio
  Running setup.py bdist_wheel for rpi.gpio ... error
  Complete output from command /usr/bin/python -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-tFqXM_/rpi.gpio/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" bdist_wheel -d /tmp/tmpjy5Jv8pip-wheel- --python-tag cp27:
  usage: -c [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or: -c --help [cmd1 cmd2 ...]
     or: -c --help-commands
     or: -c cmd --help
  
  error: invalid command 'bdist_wheel'
  
  ----------------------------------------
  Failed building wheel for rpi.gpio
  Running setup.py clean for rpi.gpio
Failed to build rpi.gpio
Installing collected packages: rpi.gpio
  Running setup.py install for rpi.gpio ... done
Successfully installed rpi.gpio-0.6.5
osmc@osmc-family-room:~$ python3 pushButton.py
Traceback (most recent call last):
  File "pushButton.py", line 30, in <module>
    import RPi.GPIO as GPIO
ImportError: No module named 'RPi'
osmc@osmc-family-room:~$ pip3 install rpi.gpio
-bash: pip3: command not found
osmc@osmc-family-room:~$ sudo apt-get install python3-pip
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  armv7-libcrossguid-osmc bluez libapt-inst1.5 libbind9-90 libdbus-1-dev libdns100
  libgif4 libgnutls-deb0-28 libhogweed2 libicu52 libisc95 libisccc90 libisccfg90
  liblwres90 libmicrohttpd10 libmysqlclient18 libnettle4 libntdb1 libplist2 libpng12-0
  libpsl0 libssl1.0.0 libwebp5 libwebpdemux1 libwebpmux1 libxtables10 pkg-config
  python-colorama python-dbus-dev python-distlib python-html5lib python-webencodings
Use 'sudo apt autoremove' to remove them.
Recommended packages:
  build-essential python3-dev python3-setuptools python3-wheel
The following NEW packages will be installed:
  python3-pip
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 142 kB of archives.
After this operation, 599 kB of additional disk space will be used.
Get:1 http://ftp.debian.org/debian stretch/main armhf python3-pip all 9.0.1-2+deb9u1 [142 kB]
Fetched 142 kB in 0s (178 kB/s)     
Selecting previously unselected package python3-pip.
(Reading database ... 30464 files and directories currently installed.)
Preparing to unpack .../python3-pip_9.0.1-2+deb9u1_all.deb ...
Unpacking python3-pip (9.0.1-2+deb9u1) ...
Setting up python3-pip (9.0.1-2+deb9u1) ...
osmc@osmc-family-room:~$ pip3 install rpi.gpio
Collecting rpi.gpio
  Using cached https://files.pythonhosted.org/packages/af/2f/407b6e4cc8a0bdf434825a160bba1807991886b63cce16a5f1a6e1f24cdf/RPi.GPIO-0.6.5.tar.gz
    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
    ImportError: No module named 'setuptools'
    
    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-j23fz8_t/rpi.gpio/
osmc@osmc-family-room:~$ python3 pushButton.py
Traceback (most recent call last):
  File "pushButton.py", line 30, in <module>
    import RPi.GPIO as GPIO
ImportError: No module named 'RPi'
osmc@osmc-family-room:~$ history
    1  sudo apt-get install cron
    2  sudo crontab -e
    3  sudo service cron restart
    4  sudo nano /boot/config.txt
    5  sudo reboot
    6  vcgencmd codec_enabled MPG2
    7  sudo shutdown -h 0
    8  uptime
    9  lgout
   10  logout
   11  hostname
   12  sudo nano /etc/hostname
   13  sudo nano /etc/hosts
   14  sudo reboot
   15  sudo shutdown -h 0
   16  sudo nano /etc/hosts
   17  sudo nano /etc/hostname
   18  which avahi-daemon
   19  lgout
   20  logout
   21  ifconfig
   22  hostname
   23  sudo apt-get install avahi-daemon
   24  logout
   25  sudo nano /boot/config.txt
   26  vcgencmd codec_enabled MPG2
   27  logout
   28  ls
   29  ls pictures
   30  ls Pictures
   31  ls /home/kodi
   32  sudo ls -l 
   33  sudo ls -l /home/osmc/
   34  sudo ls -l /home/osmc/.xbmc
   35  sudo ls -ls /home/osmc
   36  sudo ls -la /home/osmc
   37  sudo ls -la /home/osmc/.kodi
   38  sudo ls -la /home/osmc/.kodi/addons
   39  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080
   40  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/1080i
   41  sudo ls -la /home/osmc/.kodi/addons/
   42  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080
   43  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080-more
   44  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080
   45  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras
   46  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds
   47  ls
   48  cp nebula.png /home/osmc/.kodi/addons/skin.xperience1080/extras/backg
   49  cp nebula.png /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds/.
   50  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds
   51  logout
   52  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds
   53  cp nebula.jpg /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds/.
   54  logout
   55  cp blue.png /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds/.
   56  logout
   57  ls
   58  logout
   59  sudo ls -l /home/osmc/.kodi/addons/skin.xperience1080/extras
   60  sudo rm /home/osmc/.kodi/addons/skin.xperience1080/extras/backg
   61  sudo ls -l /home/osmc/.kodi/addons/skin.xperience1080/extras
   62  sudo ls -l /home/osmc/.kodi/addons/skin.xperience1080/
   63  logout
   64  sudo apt-get install nagios-nrpe-server nagios-plugins -y
   65  sudo nano /etc/nagios/nrpe.cfg
   66  sudo systemctl restart nagios-nrpe-server
   67  hostname
   68  cat /var/log/syslog
   69  ls /var
   70  ls /var/log
   71  ls /etc/log
   72  ls /log
   73  ls -lrt /var/log
   74  sudo ls -lrt /var/log
   75  cat /etc/syslog
   76  sudo journalctl
   77  sudo journalctl | grep refuse
   78  ufw status verbose
   79  lsof -P
   80  sudo lsof -P
   81  sudo ufw status verbose
   82  sudo netstat -lptu
   83  history
   84  sudo nano /etc/nagios/nrpe.cfg
   85  ls /etc/nagios
   86  ls /etc/nagios/drpe.d
   87  sudo ls /etc/nagios/drpe.d
   88  $ netstat -na | grep 12489
   89  $ sudo netstat -na | grep 12489
   90  sudo netstat -na | grep 12489
   91  sudo netstat -lptu | grep 12489
   92  sudo /sbin/iptables -L
   93  sudo nano /etc/sysconfig/iptables
   94  nmap -p 8092 192.168.1.202
   95  sudo nano /etc/iptables
   96  sudo apt-get install ufw
   97  sudo ufw allow 12489
   98  sudo netstat -lptu 
   99  history
  100  sudo ls/etc
  101  sudo ls /etc
  102  sudo ls /etc/systemd
  103  /system
  104  ls /systemd/system
  105  ls /systemd
  106  ls /lib
  107  ls /lib/systemd
  108  ls /lib/systemd/system
  109  ls /lib/systemd/system | frep nagios-nrpe-server
  110  ls /lib/systemd/system | grep nagios-nrpe-server
  111  sudo nano /lib/systemd/system/nagios-nrpe-server.service
  112  sudo nano /etc/nagios/nrpe.cfg
  113  sudo nano /etc/default/nagios-nrpe-server
  114  sudo ls /etc/nagios
  115  sudo nano /etc/nagios/nrpe_local.cfg
  116  sudo ls /etc/nagios/drpe.d
  117  sudo nano /etc/nagios/nrpe.d
  118  sudo ls /etc/nagios/nrpe.d
  119  sudo ls /etc/default
  120  sudo nano /etc/default/nagios-nrpe-server
  121  sudo nano /lib/systemd/system/nagios-nrpe-server.service
  122  sudo nano /var/run/nagios/nrpe.pid
  123  history
  124  sudo netstat -lptu
  125  ps -ax | grep nrpe
  126  sudo ls /usr/lib/nagios
  127  sudo ls /usr/lib/nagios/plugins
  128  cat /usr/lib/nagios/plugins/check_nagios
  129  cat /usr/lib/nagios/plugins/check_nagios | grep nsclient
  130  ifconfig
  131  history
  132  sudo netstat -lptu 
  133  sudo nano /etc/nagios/nrpe.cfg
  134  history | grep systemctl
  135  sudo systemctl restart nagios-nrpe-server
  136  sudo nano /etc/nagios/nrpe.cfg
  137  sudo systemctl restart nagios-nrpe-server
  138  sudo reboot
  139  logout
  140  sudo reboot
  141  sudo nano /boot/config.txt
  142  vcgencmd codec_enabled MPG2
  143  logout
  144  top
  145  history
  146  vcgencmd measure_temp
  147  grep Kodi .kodi/temp/kodi.log | head -3
  148  sudo reboot
  149  top
  150  sudo crontab -e
  151  ls -al
  152  uname
  153  uname -r
  154  history | grep vcgen
  155  vcgencmd measure_temp
  156  vcgencmd codec_enabled MPG2
  157  ca /var/log/syslog
  158  cat /var/log/syslog
  159  ls /var
  160  ls /var/log
  161  dmesg
  162  sudo fsck
  163  ls /var/log
  164  ls /var/log/fsck
  165  ls /var/log/apt
  166  cat /var/log/apt/history.log
  167  sudo apt-get update
  168  sudo apt-get dist-upgrade
  169  history | grep vgcen
  170  history | grep vg
  171  vcgencmd codec_enabled MPG2
  172  vcgencmd measure_temperature
  173  vcgencmd help
  174  vcgencmd --help
  175  vcgencmd -help
  176  vcgencmd ?
  177  vcgencmd measure_temp
  178  ls /var/log
  179  cat /var/log/faillog
  180  cat /var/log/lastlog
  181  cat /var/log/dpkg.log
  182  ls /var/log
  183  ls /var/log/fsck
  184  cat /var/log/fsck/checkfs
  185  cat /var/log/fsck/checkroot
  186  ls /var/log/samba
  187  ls /var/log/wtmp
  188  cat /var/log/wtmp
  189  vcgencmd measure_temp
  190  sudo cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq
  191  cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
  192  vcgencmd measure_temp
  193  ls /var/log/
  194  pwd
  195  ls
  196  ls /osmc
  197  ls /root
  198  sudo ls /root
  199  ifconfig
  200  vcgencmd measure_temp
  201  cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
  202  vcgencmd measure_temp
  203  ls
  204  ls /var
  205  ls /var/log
  206  dmesg
  207  ls /var/log
  208  ls /var/log/fsck
  209  cat /var/log/fsck/checkroot
  210  cat /var/log/fsck/checkfs
  211  cat /var/log/lircd
  212  ls /var/log/fsck
  213  ls /var/log
  214  cat /var/log/wtmp
  215  ls
  216  ls /var/log
  217  cat /var/log/lastlog
  218  cat /var/log/failog
  219  cat /var/log/faillog
  220  cat /var/log/alternatives.log
  221  ls /var/log
  222  cat /var/log/dpkg.log
  223  ls /var/log
  224  top
  225  mpstat
  226  sar -u 2 5t
  227  sudo sar -u 2 5t
  228  logout
  229  sudo reboot
  230  logout
  231  ls
  232  sudo ls /usr/bin
  233  sudo ls /usr/bin/p*
  234  sudo ls /usr/bin/pow*
  235  ls
  236  sudo crontab -e
  237  ls /etc/init.d
  238  sudo cat /etc/init.d/power_ring_led.sh
  239  ls /usr/local/bin/pow*
  240  sudo nano /usr/local/bin/power_ring_led.py
  241  which python3
  242  sudo nano /usr/local/bin/power_ring_led.py
  243  cp /usr/local/bin/power_ring_led.py .
  244  ls
  245  mv power_ring_led.py pushButton.py
  246  ls
  247  python3 pushButton.py
  248  pip install rpi.gpio
  249  python3 pushButton.py
  250  pip3 install rpi.gpio
  251  sudo apt-get install python3-pip
  252  pip3 install rpi.gpio
  253  python3 pushButton.py
  254  history
osmc@osmc-family-room:~$ apt-get install python3-pip python3-dev gcc
E: Could not open lock file /var/lib/dpkg/lock - open (13: Permission denied)
E: Unable to lock the administration directory (/var/lib/dpkg/), are you root?
osmc@osmc-family-room:~$ sudo apt-get install python3-pip python3-dev gcc
Reading package lists... Done
Building dependency tree       
Reading state information... Done
gcc is already the newest version (4:6.3.0-4).
python3-pip is already the newest version (9.0.1-2+deb9u1).
The following packages were automatically installed and are no longer required:
  armv7-libcrossguid-osmc bluez libapt-inst1.5 libbind9-90 libdbus-1-dev libdns100
  libgif4 libgnutls-deb0-28 libhogweed2 libicu52 libisc95 libisccc90 libisccfg90
  liblwres90 libmicrohttpd10 libmysqlclient18 libnettle4 libntdb1 libplist2 libpng12-0
  libpsl0 libssl1.0.0 libwebp5 libwebpdemux1 libwebpmux1 libxtables10 pkg-config
  python-colorama python-dbus-dev python-distlib python-html5lib python-webencodings
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libpython3-dev libpython3.5 libpython3.5-dev python3.5-dev
The following NEW packages will be installed:
  libpython3-dev libpython3.5 libpython3.5-dev python3-dev python3.5-dev
0 upgraded, 5 newly installed, 0 to remove and 0 not upgraded.
Need to get 38.7 MB of archives.
After this operation, 50.9 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://ftp.debian.org/debian stretch/main armhf libpython3.5 armhf 3.5.3-1+deb9u1 [1,204 kB]
Get:2 http://ftp.debian.org/debian stretch/main armhf libpython3.5-dev armhf 3.5.3-1+deb9u1 [37.0 MB]
Get:3 http://ftp.debian.org/debian stretch/main armhf libpython3-dev armhf 3.5.3-1 [18.7 kB]
Get:4 http://ftp.debian.org/debian stretch/main armhf python3.5-dev armhf 3.5.3-1+deb9u1 [413 kB]
Get:5 http://ftp.debian.org/debian stretch/main armhf python3-dev armhf 3.5.3-1 [1,158 B]
Fetched 38.7 MB in 5s (7,688 kB/s)      
Selecting previously unselected package libpython3.5:armhf.
(Reading database ... 30542 files and directories currently installed.)
Preparing to unpack .../libpython3.5_3.5.3-1+deb9u1_armhf.deb ...
Unpacking libpython3.5:armhf (3.5.3-1+deb9u1) ...
Selecting previously unselected package libpython3.5-dev:armhf.
Preparing to unpack .../libpython3.5-dev_3.5.3-1+deb9u1_armhf.deb ...
Unpacking libpython3.5-dev:armhf (3.5.3-1+deb9u1) ...
Selecting previously unselected package libpython3-dev:armhf.
Preparing to unpack .../libpython3-dev_3.5.3-1_armhf.deb ...
Unpacking libpython3-dev:armhf (3.5.3-1) ...
Selecting previously unselected package python3.5-dev.
Preparing to unpack .../python3.5-dev_3.5.3-1+deb9u1_armhf.deb ...
Unpacking python3.5-dev (3.5.3-1+deb9u1) ...
Selecting previously unselected package python3-dev.
Preparing to unpack .../python3-dev_3.5.3-1_armhf.deb ...
Unpacking python3-dev (3.5.3-1) ...
Setting up libpython3.5:armhf (3.5.3-1+deb9u1) ...
Setting up libpython3.5-dev:armhf (3.5.3-1+deb9u1) ...
Processing triggers for libc-bin (2.24-11+deb9u4) ...
Setting up python3.5-dev (3.5.3-1+deb9u1) ...
Setting up libpython3-dev:armhf (3.5.3-1) ...
Setting up python3-dev (3.5.3-1) ...
osmc@osmc-family-room:~$ sudo pip3 install rpi.gpio
Collecting rpi.gpio
  Downloading https://files.pythonhosted.org/packages/af/2f/407b6e4cc8a0bdf434825a160bba1807991886b63cce16a5f1a6e1f24cdf/RPi.GPIO-0.6.5.tar.gz
    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
    ImportError: No module named 'setuptools'
    
    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-6njqhab5/rpi.gpio/
osmc@osmc-family-room:~$ sudo apt-get install setuptools
Reading package lists... Done
Building dependency tree        
Reading state information... Done
E: Unable to locate package setuptools
osmc@osmc-family-room:~$ python pushButton.py
Traceback (most recent call last):
  File "pushButton.py", line 43, in <module>
    fileLog = open('/home/pi/pushButton.log', 'w+')
IOError: [Errno 2] No such file or directory: '/home/pi/pushButton.log'
osmc@osmc-family-room:~$ python pushButton.py
Traceback (most recent call last):
  File "pushButton.py", line 43, in <module>
    fileLog = open('/home/pi/pushButton.log', 'w+')
IOError: [Errno 2] No such file or directory: '/home/pi/pushButton.log'
osmc@osmc-family-room:~$ pwd
/home/osmc
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ history
    1  sudo apt-get install cron
    2  sudo crontab -e
    3  sudo service cron restart
    4  sudo nano /boot/config.txt
    5  sudo reboot
    6  vcgencmd codec_enabled MPG2
    7  sudo shutdown -h 0
    8  uptime
    9  lgout
   10  logout
   11  hostname
   12  sudo nano /etc/hostname
   13  sudo nano /etc/hosts
   14  sudo reboot
   15  sudo shutdown -h 0
   16  sudo nano /etc/hosts
   17  sudo nano /etc/hostname
   18  which avahi-daemon
   19  lgout
   20  logout
   21  ifconfig
   22  hostname
   23  sudo apt-get install avahi-daemon
   24  logout
   25  sudo nano /boot/config.txt
   26  vcgencmd codec_enabled MPG2
   27  logout
   28  ls
   29  ls pictures
   30  ls Pictures
   31  ls /home/kodi
   32  sudo ls -l 
   33  sudo ls -l /home/osmc/
   34  sudo ls -l /home/osmc/.xbmc
   35  sudo ls -ls /home/osmc
   36  sudo ls -la /home/osmc
   37  sudo ls -la /home/osmc/.kodi
   38  sudo ls -la /home/osmc/.kodi/addons
   39  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080
   40  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/1080i
   41  sudo ls -la /home/osmc/.kodi/addons/
   42  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080
   43  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080-more
   44  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080
   45  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras
   46  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds
   47  ls
   48  cp nebula.png /home/osmc/.kodi/addons/skin.xperience1080/extras/backg
   49  cp nebula.png /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds/.
   50  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds
   51  logout
   52  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds
   53  cp nebula.jpg /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds/.
   54  logout
   55  cp blue.png /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds/.
   56  logout
   57  ls
   58  logout
   59  sudo ls -l /home/osmc/.kodi/addons/skin.xperience1080/extras
   60  sudo rm /home/osmc/.kodi/addons/skin.xperience1080/extras/backg
   61  sudo ls -l /home/osmc/.kodi/addons/skin.xperience1080/extras
   62  sudo ls -l /home/osmc/.kodi/addons/skin.xperience1080/
   63  logout
   64  sudo apt-get install nagios-nrpe-server nagios-plugins -y
   65  sudo nano /etc/nagios/nrpe.cfg
   66  sudo systemctl restart nagios-nrpe-server
   67  hostname
   68  cat /var/log/syslog
   69  ls /var
   70  ls /var/log
   71  ls /etc/log
   72  ls /log
   73  ls -lrt /var/log
   74  sudo ls -lrt /var/log
   75  cat /etc/syslog
   76  sudo journalctl
   77  sudo journalctl | grep refuse
   78  ufw status verbose
   79  lsof -P
   80  sudo lsof -P
   81  sudo ufw status verbose
   82  sudo netstat -lptu
   83  history
   84  sudo nano /etc/nagios/nrpe.cfg
   85  ls /etc/nagios
   86  ls /etc/nagios/drpe.d
   87  sudo ls /etc/nagios/drpe.d
   88  $ netstat -na | grep 12489
   89  $ sudo netstat -na | grep 12489
   90  sudo netstat -na | grep 12489
   91  sudo netstat -lptu | grep 12489
   92  sudo /sbin/iptables -L
   93  sudo nano /etc/sysconfig/iptables
   94  nmap -p 8092 192.168.1.202
   95  sudo nano /etc/iptables
   96  sudo apt-get install ufw
   97  sudo ufw allow 12489
   98  sudo netstat -lptu 
   99  history
  100  sudo ls/etc
  101  sudo ls /etc
  102  sudo ls /etc/systemd
  103  /system
  104  ls /systemd/system
  105  ls /systemd
  106  ls /lib
  107  ls /lib/systemd
  108  ls /lib/systemd/system
  109  ls /lib/systemd/system | frep nagios-nrpe-server
  110  ls /lib/systemd/system | grep nagios-nrpe-server
  111  sudo nano /lib/systemd/system/nagios-nrpe-server.service
  112  sudo nano /etc/nagios/nrpe.cfg
  113  sudo nano /etc/default/nagios-nrpe-server
  114  sudo ls /etc/nagios
  115  sudo nano /etc/nagios/nrpe_local.cfg
  116  sudo ls /etc/nagios/drpe.d
  117  sudo nano /etc/nagios/nrpe.d
  118  sudo ls /etc/nagios/nrpe.d
  119  sudo ls /etc/default
  120  sudo nano /etc/default/nagios-nrpe-server
  121  sudo nano /lib/systemd/system/nagios-nrpe-server.service
  122  sudo nano /var/run/nagios/nrpe.pid
  123  history
  124  sudo netstat -lptu
  125  ps -ax | grep nrpe
  126  sudo ls /usr/lib/nagios
  127  sudo ls /usr/lib/nagios/plugins
  128  cat /usr/lib/nagios/plugins/check_nagios
  129  cat /usr/lib/nagios/plugins/check_nagios | grep nsclient
  130  ifconfig
  131  history
  132  sudo netstat -lptu 
  133  sudo nano /etc/nagios/nrpe.cfg
  134  history | grep systemctl
  135  sudo systemctl restart nagios-nrpe-server
  136  sudo nano /etc/nagios/nrpe.cfg
  137  sudo systemctl restart nagios-nrpe-server
  138  sudo reboot
  139  logout
  140  sudo reboot
  141  sudo nano /boot/config.txt
  142  vcgencmd codec_enabled MPG2
  143  logout
  144  top
  145  history
  146  vcgencmd measure_temp
  147  grep Kodi .kodi/temp/kodi.log | head -3
  148  sudo reboot
  149  top
  150  sudo crontab -e
  151  ls -al
  152  uname
  153  uname -r
  154  history | grep vcgen
  155  vcgencmd measure_temp
  156  vcgencmd codec_enabled MPG2
  157  ca /var/log/syslog
  158  cat /var/log/syslog
  159  ls /var
  160  ls /var/log
  161  dmesg
  162  sudo fsck
  163  ls /var/log
  164  ls /var/log/fsck
  165  ls /var/log/apt
  166  cat /var/log/apt/history.log
  167  sudo apt-get update
  168  sudo apt-get dist-upgrade
  169  history | grep vgcen
  170  history | grep vg
  171  vcgencmd codec_enabled MPG2
  172  vcgencmd measure_temperature
  173  vcgencmd help
  174  vcgencmd --help
  175  vcgencmd -help
  176  vcgencmd ?
  177  vcgencmd measure_temp
  178  ls /var/log
  179  cat /var/log/faillog
  180  cat /var/log/lastlog
  181  cat /var/log/dpkg.log
  182  ls /var/log
  183  ls /var/log/fsck
  184  cat /var/log/fsck/checkfs
  185  cat /var/log/fsck/checkroot
  186  ls /var/log/samba
  187  ls /var/log/wtmp
  188  cat /var/log/wtmp
  189  vcgencmd measure_temp
  190  sudo cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq
  191  cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
  192  vcgencmd measure_temp
  193  ls /var/log/
  194  pwd
  195  ls
  196  ls /osmc
  197  ls /root
  198  sudo ls /root
  199  ifconfig
  200  vcgencmd measure_temp
  201  cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
  202  vcgencmd measure_temp
  203  ls
  204  ls /var
  205  ls /var/log
  206  dmesg
  207  ls /var/log
  208  ls /var/log/fsck
  209  cat /var/log/fsck/checkroot
  210  cat /var/log/fsck/checkfs
  211  cat /var/log/lircd
  212  ls /var/log/fsck
  213  ls /var/log
  214  cat /var/log/wtmp
  215  ls
  216  ls /var/log
  217  cat /var/log/lastlog
  218  cat /var/log/failog
  219  cat /var/log/faillog
  220  cat /var/log/alternatives.log
  221  ls /var/log
  222  cat /var/log/dpkg.log
  223  ls /var/log
  224  top
  225  mpstat
  226  sar -u 2 5t
  227  sudo sar -u 2 5t
  228  logout
  229  sudo reboot
  230  logout
  231  ls
  232  sudo ls /usr/bin
  233  sudo ls /usr/bin/p*
  234  sudo ls /usr/bin/pow*
  235  ls
  236  sudo crontab -e
  237  ls /etc/init.d
  238  sudo cat /etc/init.d/power_ring_led.sh
  239  ls /usr/local/bin/pow*
  240  sudo nano /usr/local/bin/power_ring_led.py
  241  which python3
  242  sudo nano /usr/local/bin/power_ring_led.py
  243  cp /usr/local/bin/power_ring_led.py .
  244  ls
  245  mv power_ring_led.py pushButton.py
  246  ls
  247  python3 pushButton.py
  248  pip install rpi.gpio
  249  python3 pushButton.py
  250  pip3 install rpi.gpio
  251  sudo apt-get install python3-pip
  252  pip3 install rpi.gpio
  253  python3 pushButton.py
  254  history
  255  apt-get install python3-pip python3-dev gcc
  256  sudo apt-get install python3-pip python3-dev gcc
  257  sudo pip3 install rpi.gpio
  258  sudo apt-get install setuptools
  259  python pushButton.py
  260  pwd
  261  nano pushButton.py
  262  history
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ python pushButton.py
Traceback (most recent call last):
  File "pushButton.py", line 97, in <module>
    GPIO.setup(GPIO_RESET, GPIO.IN)
RuntimeError: No access to /dev/mem.  Try running as root!
osmc@osmc-family-room:~$ python3 pushButton.py
Traceback (most recent call last):
  File "pushButton.py", line 34, in <module>
    import RPi.GPIO as GPIO
ImportError: No module named 'RPi'
osmc@osmc-family-room:~$ history
    1  sudo apt-get install cron
    2  sudo crontab -e
    3  sudo service cron restart
    4  sudo nano /boot/config.txt
    5  sudo reboot
    6  vcgencmd codec_enabled MPG2
    7  sudo shutdown -h 0
    8  uptime
    9  lgout
   10  logout
   11  hostname
   12  sudo nano /etc/hostname
   13  sudo nano /etc/hosts
   14  sudo reboot
   15  sudo shutdown -h 0
   16  sudo nano /etc/hosts
   17  sudo nano /etc/hostname
   18  which avahi-daemon
   19  lgout
   20  logout
   21  ifconfig
   22  hostname
   23  sudo apt-get install avahi-daemon
   24  logout
   25  sudo nano /boot/config.txt
   26  vcgencmd codec_enabled MPG2
   27  logout
   28  ls
   29  ls pictures
   30  ls Pictures
   31  ls /home/kodi
   32  sudo ls -l 
   33  sudo ls -l /home/osmc/
   34  sudo ls -l /home/osmc/.xbmc
   35  sudo ls -ls /home/osmc
   36  sudo ls -la /home/osmc
   37  sudo ls -la /home/osmc/.kodi
   38  sudo ls -la /home/osmc/.kodi/addons
   39  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080
   40  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/1080i
   41  sudo ls -la /home/osmc/.kodi/addons/
   42  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080
   43  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080-more
   44  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080
   45  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras
   46  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds
   47  ls
   48  cp nebula.png /home/osmc/.kodi/addons/skin.xperience1080/extras/backg
   49  cp nebula.png /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds/.
   50  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds
   51  logout
   52  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds
   53  cp nebula.jpg /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds/.
   54  logout
   55  cp blue.png /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds/.
   56  logout
   57  ls
   58  logout
   59  sudo ls -l /home/osmc/.kodi/addons/skin.xperience1080/extras
   60  sudo rm /home/osmc/.kodi/addons/skin.xperience1080/extras/backg
   61  sudo ls -l /home/osmc/.kodi/addons/skin.xperience1080/extras
   62  sudo ls -l /home/osmc/.kodi/addons/skin.xperience1080/
   63  logout
   64  sudo apt-get install nagios-nrpe-server nagios-plugins -y
   65  sudo nano /etc/nagios/nrpe.cfg
   66  sudo systemctl restart nagios-nrpe-server
   67  hostname
   68  cat /var/log/syslog
   69  ls /var
   70  ls /var/log
   71  ls /etc/log
   72  ls /log
   73  ls -lrt /var/log
   74  sudo ls -lrt /var/log
   75  cat /etc/syslog
   76  sudo journalctl
   77  sudo journalctl | grep refuse
   78  ufw status verbose
   79  lsof -P
   80  sudo lsof -P
   81  sudo ufw status verbose
   82  sudo netstat -lptu
   83  history
   84  sudo nano /etc/nagios/nrpe.cfg
   85  ls /etc/nagios
   86  ls /etc/nagios/drpe.d
   87  sudo ls /etc/nagios/drpe.d
   88  $ netstat -na | grep 12489
   89  $ sudo netstat -na | grep 12489
   90  sudo netstat -na | grep 12489
   91  sudo netstat -lptu | grep 12489
   92  sudo /sbin/iptables -L
   93  sudo nano /etc/sysconfig/iptables
   94  nmap -p 8092 192.168.1.202
   95  sudo nano /etc/iptables
   96  sudo apt-get install ufw
   97  sudo ufw allow 12489
   98  sudo netstat -lptu 
   99  history
  100  sudo ls/etc
  101  sudo ls /etc
  102  sudo ls /etc/systemd
  103  /system
  104  ls /systemd/system
  105  ls /systemd
  106  ls /lib
  107  ls /lib/systemd
  108  ls /lib/systemd/system
  109  ls /lib/systemd/system | frep nagios-nrpe-server
  110  ls /lib/systemd/system | grep nagios-nrpe-server
  111  sudo nano /lib/systemd/system/nagios-nrpe-server.service
  112  sudo nano /etc/nagios/nrpe.cfg
  113  sudo nano /etc/default/nagios-nrpe-server
  114  sudo ls /etc/nagios
  115  sudo nano /etc/nagios/nrpe_local.cfg
  116  sudo ls /etc/nagios/drpe.d
  117  sudo nano /etc/nagios/nrpe.d
  118  sudo ls /etc/nagios/nrpe.d
  119  sudo ls /etc/default
  120  sudo nano /etc/default/nagios-nrpe-server
  121  sudo nano /lib/systemd/system/nagios-nrpe-server.service
  122  sudo nano /var/run/nagios/nrpe.pid
  123  history
  124  sudo netstat -lptu
  125  ps -ax | grep nrpe
  126  sudo ls /usr/lib/nagios
  127  sudo ls /usr/lib/nagios/plugins
  128  cat /usr/lib/nagios/plugins/check_nagios
  129  cat /usr/lib/nagios/plugins/check_nagios | grep nsclient
  130  ifconfig
  131  history
  132  sudo netstat -lptu 
  133  sudo nano /etc/nagios/nrpe.cfg
  134  history | grep systemctl
  135  sudo systemctl restart nagios-nrpe-server
  136  sudo nano /etc/nagios/nrpe.cfg
  137  sudo systemctl restart nagios-nrpe-server
  138  sudo reboot
  139  logout
  140  sudo reboot
  141  sudo nano /boot/config.txt
  142  vcgencmd codec_enabled MPG2
  143  logout
  144  top
  145  history
  146  vcgencmd measure_temp
  147  grep Kodi .kodi/temp/kodi.log | head -3
  148  sudo reboot
  149  top
  150  sudo crontab -e
  151  ls -al
  152  uname
  153  uname -r
  154  history | grep vcgen
  155  vcgencmd measure_temp
  156  vcgencmd codec_enabled MPG2
  157  ca /var/log/syslog
  158  cat /var/log/syslog
  159  ls /var
  160  ls /var/log
  161  dmesg
  162  sudo fsck
  163  ls /var/log
  164  ls /var/log/fsck
  165  ls /var/log/apt
  166  cat /var/log/apt/history.log
  167  sudo apt-get update
  168  sudo apt-get dist-upgrade
  169  history | grep vgcen
  170  history | grep vg
  171  vcgencmd codec_enabled MPG2
  172  vcgencmd measure_temperature
  173  vcgencmd help
  174  vcgencmd --help
  175  vcgencmd -help
  176  vcgencmd ?
  177  vcgencmd measure_temp
  178  ls /var/log
  179  cat /var/log/faillog
  180  cat /var/log/lastlog
  181  cat /var/log/dpkg.log
  182  ls /var/log
  183  ls /var/log/fsck
  184  cat /var/log/fsck/checkfs
  185  cat /var/log/fsck/checkroot
  186  ls /var/log/samba
  187  ls /var/log/wtmp
  188  cat /var/log/wtmp
  189  vcgencmd measure_temp
  190  sudo cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq
  191  cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
  192  vcgencmd measure_temp
  193  ls /var/log/
  194  pwd
  195  ls
  196  ls /osmc
  197  ls /root
  198  sudo ls /root
  199  ifconfig
  200  vcgencmd measure_temp
  201  cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
  202  vcgencmd measure_temp
  203  ls
  204  ls /var
  205  ls /var/log
  206  dmesg
  207  ls /var/log
  208  ls /var/log/fsck
  209  cat /var/log/fsck/checkroot
  210  cat /var/log/fsck/checkfs
  211  cat /var/log/lircd
  212  ls /var/log/fsck
  213  ls /var/log
  214  cat /var/log/wtmp
  215  ls
  216  ls /var/log
  217  cat /var/log/lastlog
  218  cat /var/log/failog
  219  cat /var/log/faillog
  220  cat /var/log/alternatives.log
  221  ls /var/log
  222  cat /var/log/dpkg.log
  223  ls /var/log
  224  top
  225  mpstat
  226  sar -u 2 5t
  227  sudo sar -u 2 5t
  228  logout
  229  sudo reboot
  230  logout
  231  ls
  232  sudo ls /usr/bin
  233  sudo ls /usr/bin/p*
  234  sudo ls /usr/bin/pow*
  235  ls
  236  sudo crontab -e
  237  ls /etc/init.d
  238  sudo cat /etc/init.d/power_ring_led.sh
  239  ls /usr/local/bin/pow*
  240  sudo nano /usr/local/bin/power_ring_led.py
  241  which python3
  242  sudo nano /usr/local/bin/power_ring_led.py
  243  cp /usr/local/bin/power_ring_led.py .
  244  ls
  245  mv power_ring_led.py pushButton.py
  246  ls
  247  python3 pushButton.py
  248  pip install rpi.gpio
  249  python3 pushButton.py
  250  pip3 install rpi.gpio
  251  sudo apt-get install python3-pip
  252  pip3 install rpi.gpio
  253  python3 pushButton.py
  254  history
  255  apt-get install python3-pip python3-dev gcc
  256  sudo apt-get install python3-pip python3-dev gcc
  257  sudo pip3 install rpi.gpio
  258  sudo apt-get install setuptools
  259  python pushButton.py
  260  pwd
  261  nano pushButton.py
  262  history
  263  nano pushButton.py
  264  python pushButton.py
  265  python3 pushButton.py
  266  history
osmc@osmc-family-room:~$ python pushButton.py
Traceback (most recent call last):
  File "pushButton.py", line 97, in <module>
    GPIO.setup(GPIO_RESET, GPIO.IN)
RuntimeError: No access to /dev/mem.  Try running as root!
osmc@osmc-family-room:~$ sudo python pushButton.py
osmc@osmc-family-room:~$ ls
blue.png     Movies  nebula.jpg  Pictures        pushButton.py
ky8LT0D.png  Music   nebula.png  pushButton.log  TV Shows
osmc@osmc-family-room:~$ cat pushButton.log
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py
packet_write_wait: Connection to 192.168.1.99 port 22: Broken pipe
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ ssh osmc@osmc-family-room
osmc@osmc-family-room's password: 
Linux osmc-family-room 4.14.78-4-osmc #1 SMP PREEMPT Wed Dec 12 17:58:11 UTC 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jun  8 15:06:59 2019 from 192.168.1.224
osmc@osmc-family-room:~$ history
    1  sudo apt-get install cron
    2  sudo crontab -e
    3  sudo service cron restart
    4  sudo nano /boot/config.txt
    5  sudo reboot
    6  vcgencmd codec_enabled MPG2
    7  sudo shutdown -h 0
    8  uptime
    9  lgout
   10  logout
   11  hostname
   12  sudo nano /etc/hostname
   13  sudo nano /etc/hosts
   14  sudo reboot
   15  sudo shutdown -h 0
   16  sudo nano /etc/hosts
   17  sudo nano /etc/hostname
   18  which avahi-daemon
   19  lgout
   20  logout
   21  ifconfig
   22  hostname
   23  sudo apt-get install avahi-daemon
   24  logout
   25  sudo nano /boot/config.txt
   26  vcgencmd codec_enabled MPG2
   27  logout
   28  ls
   29  ls pictures
   30  ls Pictures
   31  ls /home/kodi
   32  sudo ls -l 
   33  sudo ls -l /home/osmc/
   34  sudo ls -l /home/osmc/.xbmc
   35  sudo ls -ls /home/osmc
   36  sudo ls -la /home/osmc
   37  sudo ls -la /home/osmc/.kodi
   38  sudo ls -la /home/osmc/.kodi/addons
   39  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080
   40  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/1080i
   41  sudo ls -la /home/osmc/.kodi/addons/
   42  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080
   43  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080-more
   44  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080
   45  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras
   46  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds
   47  ls
   48  cp nebula.png /home/osmc/.kodi/addons/skin.xperience1080/extras/backg
   49  cp nebula.png /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds/.
   50  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds
   51  logout
   52  sudo ls -la /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds
   53  cp nebula.jpg /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds/.
   54  logout
   55  cp blue.png /home/osmc/.kodi/addons/skin.xperience1080/extras/backgrounds/.
   56  logout
   57  ls
   58  logout
   59  sudo ls -l /home/osmc/.kodi/addons/skin.xperience1080/extras
   60  sudo rm /home/osmc/.kodi/addons/skin.xperience1080/extras/backg
   61  sudo ls -l /home/osmc/.kodi/addons/skin.xperience1080/extras
   62  sudo ls -l /home/osmc/.kodi/addons/skin.xperience1080/
   63  logout
   64  sudo apt-get install nagios-nrpe-server nagios-plugins -y
   65  sudo nano /etc/nagios/nrpe.cfg
   66  sudo systemctl restart nagios-nrpe-server
   67  hostname
   68  cat /var/log/syslog
   69  ls /var
   70  ls /var/log
   71  ls /etc/log
   72  ls /log
   73  ls -lrt /var/log
   74  sudo ls -lrt /var/log
   75  cat /etc/syslog
   76  sudo journalctl
   77  sudo journalctl | grep refuse
   78  ufw status verbose
   79  lsof -P
   80  sudo lsof -P
   81  sudo ufw status verbose
   82  sudo netstat -lptu
   83  history
   84  sudo nano /etc/nagios/nrpe.cfg
   85  ls /etc/nagios
   86  ls /etc/nagios/drpe.d
   87  sudo ls /etc/nagios/drpe.d
   88  $ netstat -na | grep 12489
   89  $ sudo netstat -na | grep 12489
   90  sudo netstat -na | grep 12489
   91  sudo netstat -lptu | grep 12489
   92  sudo /sbin/iptables -L
   93  sudo nano /etc/sysconfig/iptables
   94  nmap -p 8092 192.168.1.202
   95  sudo nano /etc/iptables
   96  sudo apt-get install ufw
   97  sudo ufw allow 12489
   98  sudo netstat -lptu 
   99  history
  100  sudo ls/etc
  101  sudo ls /etc
  102  sudo ls /etc/systemd
  103  /system
  104  ls /systemd/system
  105  ls /systemd
  106  ls /lib
  107  ls /lib/systemd
  108  ls /lib/systemd/system
  109  ls /lib/systemd/system | frep nagios-nrpe-server
  110  ls /lib/systemd/system | grep nagios-nrpe-server
  111  sudo nano /lib/systemd/system/nagios-nrpe-server.service
  112  sudo nano /etc/nagios/nrpe.cfg
  113  sudo nano /etc/default/nagios-nrpe-server
  114  sudo ls /etc/nagios
  115  sudo nano /etc/nagios/nrpe_local.cfg
  116  sudo ls /etc/nagios/drpe.d
  117  sudo nano /etc/nagios/nrpe.d
  118  sudo ls /etc/nagios/nrpe.d
  119  sudo ls /etc/default
  120  sudo nano /etc/default/nagios-nrpe-server
  121  sudo nano /lib/systemd/system/nagios-nrpe-server.service
  122  sudo nano /var/run/nagios/nrpe.pid
  123  history
  124  sudo netstat -lptu
  125  ps -ax | grep nrpe
  126  sudo ls /usr/lib/nagios
  127  sudo ls /usr/lib/nagios/plugins
  128  cat /usr/lib/nagios/plugins/check_nagios
  129  cat /usr/lib/nagios/plugins/check_nagios | grep nsclient
  130  ifconfig
  131  history
  132  sudo netstat -lptu 
  133  sudo nano /etc/nagios/nrpe.cfg
  134  history | grep systemctl
  135  sudo systemctl restart nagios-nrpe-server
  136  sudo nano /etc/nagios/nrpe.cfg
  137  sudo systemctl restart nagios-nrpe-server
  138  sudo reboot
  139  logout
  140  sudo reboot
  141  sudo nano /boot/config.txt
  142  vcgencmd codec_enabled MPG2
  143  logout
  144  top
  145  history
  146  vcgencmd measure_temp
  147  grep Kodi .kodi/temp/kodi.log | head -3
  148  sudo reboot
  149  top
  150  sudo crontab -e
  151  ls -al
  152  uname
  153  uname -r
  154  history | grep vcgen
  155  vcgencmd measure_temp
  156  vcgencmd codec_enabled MPG2
  157  ca /var/log/syslog
  158  cat /var/log/syslog
  159  ls /var
  160  ls /var/log
  161  dmesg
  162  sudo fsck
  163  ls /var/log
  164  ls /var/log/fsck
  165  ls /var/log/apt
  166  cat /var/log/apt/history.log
  167  sudo apt-get update
  168  sudo apt-get dist-upgrade
  169  history | grep vgcen
  170  history | grep vg
  171  vcgencmd codec_enabled MPG2
  172  vcgencmd measure_temperature
  173  vcgencmd help
  174  vcgencmd --help
  175  vcgencmd -help
  176  vcgencmd ?
  177  vcgencmd measure_temp
  178  ls /var/log
  179  cat /var/log/faillog
  180  cat /var/log/lastlog
  181  cat /var/log/dpkg.log
  182  ls /var/log
  183  ls /var/log/fsck
  184  cat /var/log/fsck/checkfs
  185  cat /var/log/fsck/checkroot
  186  ls /var/log/samba
  187  ls /var/log/wtmp
  188  cat /var/log/wtmp
  189  vcgencmd measure_temp
  190  sudo cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq
  191  cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
  192  vcgencmd measure_temp
  193  ls /var/log/
  194  pwd
  195  ls
  196  ls /osmc
  197  ls /root
  198  sudo ls /root
  199  ifconfig
  200  vcgencmd measure_temp
  201  cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
  202  vcgencmd measure_temp
  203  ls
  204  ls /var
  205  ls /var/log
  206  dmesg
  207  ls /var/log
  208  ls /var/log/fsck
  209  cat /var/log/fsck/checkroot
  210  cat /var/log/fsck/checkfs
  211  cat /var/log/lircd
  212  ls /var/log/fsck
  213  ls /var/log
  214  cat /var/log/wtmp
  215  ls
  216  ls /var/log
  217  cat /var/log/lastlog
  218  cat /var/log/failog
  219  cat /var/log/faillog
  220  cat /var/log/alternatives.log
  221  ls /var/log
  222  cat /var/log/dpkg.log
  223  ls /var/log
  224  top
  225  mpstat
  226  sar -u 2 5t
  227  sudo sar -u 2 5t
  228  logout
  229  sudo reboot
  230  logout
  231  history
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ ls
blue.png     Movies  nebula.jpg  Pictures        pushButton.py
ky8LT0D.png  Music   nebula.png  pushButton.log  TV Shows
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ ps -aux | grep power
osmc      1146  0.0  0.0   3840   592 pts/1    S+   15:11   0:00 grep power
osmc@osmc-family-room:~$ ps -uax
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.4  0.6  25448  4944 ?        Ss   15:06   0:01 /sbin/init
root         2  0.0  0.0      0     0 ?        S    15:06   0:00 [kthreadd]
root         4  0.0  0.0      0     0 ?        I<   15:06   0:00 [kworker/0:0H]
root         6  0.0  0.0      0     0 ?        I<   15:06   0:00 [mm_percpu_wq]
root         7  0.0  0.0      0     0 ?        S    15:06   0:00 [ksoftirqd/0]
root         8  0.0  0.0      0     0 ?        I    15:06   0:00 [rcu_preempt]
root         9  0.0  0.0      0     0 ?        I    15:06   0:00 [rcu_sched]
root        10  0.0  0.0      0     0 ?        I    15:06   0:00 [rcu_bh]
root        11  0.0  0.0      0     0 ?        S    15:06   0:00 [migration/0]
root        12  0.0  0.0      0     0 ?        S    15:06   0:00 [cpuhp/0]
root        13  0.0  0.0      0     0 ?        S    15:06   0:00 [cpuhp/1]
root        14  0.0  0.0      0     0 ?        S    15:06   0:00 [migration/1]
root        15  0.0  0.0      0     0 ?        S    15:06   0:00 [ksoftirqd/1]
root        17  0.0  0.0      0     0 ?        I<   15:06   0:00 [kworker/1:0H]
root        18  0.0  0.0      0     0 ?        S    15:06   0:00 [cpuhp/2]
root        19  0.0  0.0      0     0 ?        S    15:06   0:00 [migration/2]
root        20  0.0  0.0      0     0 ?        S    15:06   0:00 [ksoftirqd/2]
root        22  0.0  0.0      0     0 ?        I<   15:06   0:00 [kworker/2:0H]
root        23  0.0  0.0      0     0 ?        S    15:06   0:00 [cpuhp/3]
root        24  0.0  0.0      0     0 ?        S    15:06   0:00 [migration/3]
root        25  0.0  0.0      0     0 ?        S    15:06   0:00 [ksoftirqd/3]
root        27  0.0  0.0      0     0 ?        I<   15:06   0:00 [kworker/3:0H]
root        28  0.0  0.0      0     0 ?        S    15:06   0:00 [kdevtmpfs]
root        29  0.0  0.0      0     0 ?        I<   15:06   0:00 [netns]
root        30  0.0  0.0      0     0 ?        I    15:06   0:00 [kworker/0:1]
root        31  0.0  0.0      0     0 ?        I    15:06   0:00 [kworker/1:1]
root        32  0.0  0.0      0     0 ?        I    15:06   0:00 [kworker/2:1]
root        33  0.0  0.0      0     0 ?        S    15:06   0:00 [khungtaskd]
root        34  0.0  0.0      0     0 ?        S    15:06   0:00 [oom_reaper]
root        35  0.0  0.0      0     0 ?        I<   15:06   0:00 [writeback]
root        36  0.0  0.0      0     0 ?        S    15:06   0:00 [kcompactd0]
root        37  0.0  0.0      0     0 ?        I<   15:06   0:00 [crypto]
root        38  0.0  0.0      0     0 ?        I<   15:06   0:00 [kblockd]
root        39  0.0  0.0      0     0 ?        I<   15:06   0:00 [watchdogd]
root        40  0.0  0.0      0     0 ?        I<   15:06   0:00 [rpciod]
root        41  0.0  0.0      0     0 ?        I<   15:06   0:00 [xprtiod]
root        42  0.0  0.0      0     0 ?        S    15:06   0:00 [kauditd]
root        43  0.0  0.0      0     0 ?        S    15:06   0:00 [kswapd0]
root        44  0.0  0.0      0     0 ?        I<   15:06   0:00 [kworker/u9:0]
root        45  0.0  0.0      0     0 ?        I<   15:06   0:00 [nfsiod]
root        68  0.0  0.0      0     0 ?        I<   15:06   0:00 [kthrotld]
root        69  0.0  0.0      0     0 ?        I    15:06   0:00 [kworker/3:1]
root        70  0.0  0.0      0     0 ?        I<   15:06   0:00 [iscsi_eh]
root        71  0.0  0.0      0     0 ?        I<   15:06   0:00 [dwc_otg]
root        72  0.0  0.0      0     0 ?        I<   15:06   0:00 [DWC Notificatio]
root        74  0.1  0.0      0     0 ?        S<   15:06   0:00 [vchiq-slot/0]
root        75  0.1  0.0      0     0 ?        S<   15:06   0:00 [vchiq-recy/0]
root        76  0.0  0.0      0     0 ?        S<   15:06   0:00 [vchiq-sync/0]
root        77  0.0  0.0      0     0 ?        S    15:06   0:00 [vchiq-keep/0]
root        78  0.0  0.0      0     0 ?        S<   15:06   0:00 [SMIO]
root        79  0.0  0.0      0     0 ?        I    15:06   0:00 [kworker/u8:1]
root        84  0.0  0.0      0     0 ?        S    15:06   0:00 [irq/92-mmc1]
root        85  0.0  0.0      0     0 ?        I    15:06   0:00 [kworker/0:3]
root       112  0.1  0.0      0     0 ?        S    15:06   0:00 [mmcqd/0]
root       127  0.0  0.0      0     0 ?        I    15:06   0:00 [kworker/u8:2]
root       131  0.0  0.0      0     0 ?        I<   15:06   0:00 [kworker/2:1H]
root       134  0.0  0.0      0     0 ?        S    15:06   0:00 [jbd2/mmcblk0p2-]
root       135  0.0  0.0      0     0 ?        I<   15:06   0:00 [ext4-rsv-conver]
root       150  0.0  0.0      0     0 ?        I<   15:06   0:00 [ipv6_addrconf]
root       182  0.1  0.4  10448  3684 ?        Ss   15:06   0:00 /lib/systemd/systemd-journ
root       196  0.0  0.0      0     0 ?        I    15:06   0:00 [kworker/2:2]
root       198  0.0  0.3  13372  2712 ?        Ss   15:06   0:00 /lib/systemd/systemd-udevd
root       200  0.0  0.0      0     0 ?        I    15:06   0:00 [kworker/1:2]
root       208  0.0  0.3   5876  2544 ?        Ss   15:06   0:00 /sbin/rpcbind -f -w
root       210  0.0  0.0      0     0 ?        I    15:06   0:00 [kworker/3:2]
root       217  0.0  0.4   6144  3348 ?        Ss   15:06   0:00 /lib/systemd/systemd-login
root       218  0.0  0.2   3056  1628 ?        Ss   15:06   0:00 /usr/sbin/cron -f
message+   220  0.0  0.3   5592  2736 ?        Ss   15:06   0:00 /usr/bin/dbus-daemon --sys
root       281  0.0  0.0      0     0 ?        I<   15:06   0:00 [cfg80211]
root       282  0.0  0.0      0     0 ?        I<   15:06   0:00 [brcmf_wq/mmc1:0]
root       283  0.0  0.6   9024  4736 ?        Ss   15:06   0:00 /usr/sbin/connmand -n --no
root       285  0.0  0.0      0     0 ?        S    15:06   0:00 [brcmf_wdog/mmc1]
avahi      286  0.0  0.3   5280  2388 ?        Ss   15:06   0:00 avahi-daemon: running [osm
root       292  0.0  0.0   1976   616 ?        Ss   15:06   0:00 /usr/sbin/eventlircd --evm
root       295  0.0  0.1   3428  1440 ?        Ss   15:06   0:00 /usr/sbin/irqbalance
root       306  0.0  0.0      0     0 ?        I<   15:06   0:00 [kworker/0:1H]
avahi      314  0.0  0.0   5280   296 ?        S    15:06   0:00 avahi-daemon: chroot helpe
nagios     341  0.0  0.3   3632  2564 ?        Ss   15:06   0:00 /usr/sbin/nrpe -c /etc/nag
root       342  0.0  0.2   2844  2064 ?        Ss   15:06   0:00 /bin/bash /usr/bin/mediace
root       387  0.0  0.5   8576  3996 ?        Ss   15:06   0:00 /usr/sbin/sshd -D
root       392  0.0  0.0   1860   112 ?        Ss   15:06   0:00 /usr/sbin/lircd --driver=d
root       404  0.0  0.3   5784  2488 ?        S    15:06   0:00 sudo -u osmc LIRC_SOCKET_P
osmc       405 25.9 22.9 822484 175640 ?       Sl   15:06   1:26 /usr/lib/kodi/kodi.bin --s
osmc       412  0.0  0.4   7716  3620 ?        Ss   15:06   0:00 /usr/bin/udisks-glue --for
root       414  0.0  0.6  26892  4884 ?        Ssl  15:06   0:00 /usr/lib/udisks/udisks-dae
root       415  0.0  0.2   8184  1704 ?        S    15:06   0:00 udisks-daemon: not polling
root       416  0.0  0.2   7848  1832 ?        Ss   15:06   0:00 /sbin/wpa_supplicant -u -s
root       420  0.0  0.6  36260  5264 ?        Ssl  15:06   0:00 /usr/lib/policykit-1/polki
root       457  0.0  0.0      0     0 ?        I<   15:06   0:00 [kworker/u9:1]
root       458  0.0  0.0   1532    84 ?        S    15:06   0:00 /usr/bin/hciattach /dev/se
root       462  0.0  0.1   5696  1292 ?        Ss   15:06   0:00 /usr/libexec/bluetooth/blu
root       465  0.0  0.0      0     0 ?        I<   15:06   0:00 [kworker/3:1H]
ntp        546  0.0  0.3   7068  2852 ?        Ssl  15:06   0:00 /usr/sbin/ntpd -p /var/run
root      1012  0.0  0.6   9732  4712 ?        Ss   15:06   0:00 sshd: osmc [priv]
osmc      1030  0.0  0.5   8092  4364 ?        Ss   15:06   0:00 /lib/systemd/systemd --use
osmc      1031  0.0  0.1   9504  1256 ?        S    15:06   0:00 (sd-pam)
osmc      1037  0.0  0.4   9732  3260 ?        S    15:06   0:00 sshd: osmc@pts/0
osmc      1038  0.0  0.3   4680  2792 pts/0    Ss+  15:06   0:00 -bash
root      1066  0.0  0.0      0     0 ?        I<   15:07   0:00 [kworker/1:1H]
root      1095  0.0  0.6   9732  4796 ?        Ss   15:07   0:00 sshd: osmc [priv]
osmc      1101  0.0  0.4   9732  3100 ?        R    15:08   0:00 sshd: osmc@pts/1
osmc      1102  0.0  0.3   4680  2712 pts/1    Ss   15:08   0:00 -bash
root      1121  0.0  0.0      0     0 ?        I    15:11   0:00 [kworker/0:0]
osmc      1152  0.0  0.3   6808  2476 pts/1    R+   15:12   0:00 ps -uax
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ sudo service /etc/init.d/power_ring_led.sh
/etc/init.d/power_ring_led.sh: unrecognized service
osmc@osmc-family-room:~$ sudo service /etc/init.d/power_ring_led.sh stop
Failed to stop etc-init.d-power_ring_led.service.mount: Unit etc-init.d-power_ring_led.service.mount not loaded.
osmc@osmc-family-room:~$ sudo service /etc/init.d/power_ring_led.py stop
Failed to stop etc-init.d-power_ring_led.py.service.mount: Unit etc-init.d-power_ring_led.py.service.mount not loaded.
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py
packet_write_wait: Connection to 192.168.1.99 port 22: Broken pipe
Jeffs-MBP:~ jeff$ ssh osmc@osmc-family-room
osmc@osmc-family-room's password: 
Linux osmc-family-room 4.14.78-4-osmc #1 SMP PREEMPT Wed Dec 12 17:58:11 UTC 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jun  8 15:18:41 2019 from 192.168.1.224
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ ls -l
total 7900
-rw-r--r-- 1 osmc osmc 3750142 Feb 16 17:01 blue.png
-rw-r--r-- 1 osmc osmc  779235 Feb 16 18:07 ky8LT0D.png
drwxr-xr-x 2 osmc osmc    4096 May  3  2017 Movies
drwxr-xr-x 2 osmc osmc    4096 May  3  2017 Music
-rw-r--r-- 1 osmc osmc 1196584 Feb 16 16:57 nebula.jpg
-rw-r--r-- 1 osmc osmc 2333104 Feb 16 16:41 nebula.png
drwxr-xr-x 2 osmc osmc    4096 May  3  2017 Pictures
-rw-r--r-- 1 osmc osmc       0 Jun  8 15:17 pushButton.log
-rwxr-xr-x 1 osmc osmc    3385 Jun  8 15:11 pushButton.py
drwxr-xr-x 2 osmc osmc    4096 May  3  2017 TV Shows
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ ls -l /etc/init.d
total 208
-rwxr-xr-x 1 root root 2401 Apr 13  2015 avahi-daemon
-rwxr-xr-x 1 root root 1276 Apr  6  2015 bootlogs
-rwxr-xr-x 1 root root 1248 Apr  6  2015 bootmisc.sh
-rwxr-xr-x 1 root root 3807 Feb 12  2017 checkfs.sh
-rwxr-xr-x 1 root root 1072 Apr  6  2015 checkroot-bootclean.sh
-rwxr-xr-x 1 root root 9353 Feb 12  2017 checkroot.sh
-rwxr-xr-x 1 root root 3049 Jun 11  2015 cron
-rwxr-xr-x 1 root root 2813 Oct 10  2016 dbus
-rwxr-xr-x 1 root root  824 Sep  5  2014 fake-hwclock
-rwxr-xr-x 1 root root 1336 Apr  6  2015 halt
-rwxr-xr-x 1 root root 1423 Apr  6  2015 hostname.sh
-rwxr-xr-x 1 root root 3809 Mar  7  2018 hwclock.sh
-rwxr-xr-x 1 root root 1300 Apr  6  2015 killprocs
-rwxr-xr-x 1 root root 2044 Dec 25  2016 kmod
-rwxr-xr-x 1 root root  995 Apr  6  2015 motd
-rwxr-xr-x 1 root root  677 Apr  6  2015 mountall-bootclean.sh
-rwxr-xr-x 1 root root 2301 Feb 12  2017 mountall.sh
-rwxr-xr-x 1 root root 1461 Apr  6  2015 mountdevsubfs.sh
-rwxr-xr-x 1 root root 1564 Apr  6  2015 mountkernfs.sh
-rwxr-xr-x 1 root root  685 Apr  6  2015 mountnfs-bootclean.sh
-rwxr-xr-x 1 root root 2456 Apr  6  2015 mountnfs.sh
-rwxr-xr-x 1 root root 2071 Apr 19  2017 nagios-nrpe-server
-rwxr-xr-x 1 root root 5658 Aug 12  2014 nfs-common
-rwxr-xr-x 1 root root 1561 Feb 15  2018 ntp
-rwxr-xr-x 1 root root 9138 Jul 18  2017 openvpn
-rwxr-xr-x 1 root root  721 Nov 22  2017 power_ring_led.sh
-rwxr-xr-x 1 root root 1191 May 17  2018 procps
-rwxr-xr-x 1 root root 6290 Feb 12  2017 rc
-rwxr-xr-x 1 root root  820 Apr  6  2015 rc.local
-rwxr-xr-x 1 root root  117 Feb 12  2017 rcS
-rw-r--r-- 1 root root 2427 Feb 12  2017 README
-rwxr-xr-x 1 root root  661 Apr  6  2015 reboot
-rwxr-xr-x 1 root root 1042 Apr  6  2015 rmnologin
-rwxr-xr-x 1 root root 2358 May  5  2017 rpcbind
-rwxr-xr-x 1 root root 3207 Apr  6  2015 sendsigs
-rwxr-xr-x 1 root root  597 Apr  6  2015 single
-rw-r--r-- 1 root root 1087 Feb 12  2017 skeleton
-rwxr-xr-x 1 root root 4033 Mar  1  2018 ssh
-rwxr-xr-x 1 root root  731 Jan  5  2016 sudo
-rwxr-xr-x 1 root root 6087 Jan 15 03:59 udev
-rwxr-xr-x 1 root root 2083 Jan 10  2017 ufw
-rwxr-xr-x 1 root root 2748 Feb 12  2017 umountfs
-rwxr-xr-x 1 root root 2202 Apr  6  2015 umountnfs.sh
-rwxr-xr-x 1 root root 1234 Feb 12  2017 umountroot
-rwxr-xr-x 1 root root 3111 Apr  6  2015 urandom
osmc@osmc-family-room:~$ sudo mv /etc/init.d/power_ring_led.sh .
osmc@osmc-family-room:~$ ls -l /etc/init.d
total 204
-rwxr-xr-x 1 root root 2401 Apr 13  2015 avahi-daemon
-rwxr-xr-x 1 root root 1276 Apr  6  2015 bootlogs
-rwxr-xr-x 1 root root 1248 Apr  6  2015 bootmisc.sh
-rwxr-xr-x 1 root root 3807 Feb 12  2017 checkfs.sh
-rwxr-xr-x 1 root root 1072 Apr  6  2015 checkroot-bootclean.sh
-rwxr-xr-x 1 root root 9353 Feb 12  2017 checkroot.sh
-rwxr-xr-x 1 root root 3049 Jun 11  2015 cron
-rwxr-xr-x 1 root root 2813 Oct 10  2016 dbus
-rwxr-xr-x 1 root root  824 Sep  5  2014 fake-hwclock
-rwxr-xr-x 1 root root 1336 Apr  6  2015 halt
-rwxr-xr-x 1 root root 1423 Apr  6  2015 hostname.sh
-rwxr-xr-x 1 root root 3809 Mar  7  2018 hwclock.sh
-rwxr-xr-x 1 root root 1300 Apr  6  2015 killprocs
-rwxr-xr-x 1 root root 2044 Dec 25  2016 kmod
-rwxr-xr-x 1 root root  995 Apr  6  2015 motd
-rwxr-xr-x 1 root root  677 Apr  6  2015 mountall-bootclean.sh
-rwxr-xr-x 1 root root 2301 Feb 12  2017 mountall.sh
-rwxr-xr-x 1 root root 1461 Apr  6  2015 mountdevsubfs.sh
-rwxr-xr-x 1 root root 1564 Apr  6  2015 mountkernfs.sh
-rwxr-xr-x 1 root root  685 Apr  6  2015 mountnfs-bootclean.sh
-rwxr-xr-x 1 root root 2456 Apr  6  2015 mountnfs.sh
-rwxr-xr-x 1 root root 2071 Apr 19  2017 nagios-nrpe-server
-rwxr-xr-x 1 root root 5658 Aug 12  2014 nfs-common
-rwxr-xr-x 1 root root 1561 Feb 15  2018 ntp
-rwxr-xr-x 1 root root 9138 Jul 18  2017 openvpn
-rwxr-xr-x 1 root root 1191 May 17  2018 procps
-rwxr-xr-x 1 root root 6290 Feb 12  2017 rc
-rwxr-xr-x 1 root root  820 Apr  6  2015 rc.local
-rwxr-xr-x 1 root root  117 Feb 12  2017 rcS
-rw-r--r-- 1 root root 2427 Feb 12  2017 README
-rwxr-xr-x 1 root root  661 Apr  6  2015 reboot
-rwxr-xr-x 1 root root 1042 Apr  6  2015 rmnologin
-rwxr-xr-x 1 root root 2358 May  5  2017 rpcbind
-rwxr-xr-x 1 root root 3207 Apr  6  2015 sendsigs
-rwxr-xr-x 1 root root  597 Apr  6  2015 single
-rw-r--r-- 1 root root 1087 Feb 12  2017 skeleton
-rwxr-xr-x 1 root root 4033 Mar  1  2018 ssh
-rwxr-xr-x 1 root root  731 Jan  5  2016 sudo
-rwxr-xr-x 1 root root 6087 Jan 15 03:59 udev
-rwxr-xr-x 1 root root 2083 Jan 10  2017 ufw
-rwxr-xr-x 1 root root 2748 Feb 12  2017 umountfs
-rwxr-xr-x 1 root root 2202 Apr  6  2015 umountnfs.sh
-rwxr-xr-x 1 root root 1234 Feb 12  2017 umountroot
-rwxr-xr-x 1 root root 3111 Apr  6  2015 urandom
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ ls
blue.png     Movies  nebula.jpg  Pictures           pushButton.log  TV Shows
ky8LT0D.png  Music   nebula.png  power_ring_led.sh  pushButton.py
osmc@osmc-family-room:~$ sudo reboot
Connection to osmc-family-room closed by remote host.
Connection to osmc-family-room closed.
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ ssh osmc@osmc-family-room
osmc@osmc-family-room's password: 
Linux osmc-family-room 4.14.78-4-osmc #1 SMP PREEMPT Wed Dec 12 17:58:11 UTC 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jun  8 15:21:12 2019 from 192.168.1.224
osmc@osmc-family-room:~$ ls
blue.png     Movies  nebula.jpg  Pictures           pushButton.log  TV Shows
ky8LT0D.png  Music   nebula.png  power_ring_led.sh  pushButton.py
osmc@osmc-family-room:~$ nsno pudhButton.py
-bash: nsno: command not found
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py
^X^Cosmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py --light
^Cosmc@osmc-family-room:~$ sudo python pushButton.py --off
^Cosmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py --light
Push Button LED on
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
ignore noise
^Cosmc@osmc-family-room:~nano pushButton.pyht
osmc@osmc-family-room:~$ sudo python pushButton.py --light
Push Button LED on



^Cosmc@osmc-family-room:~$ sudo python pushButton.py --off
Push Button Ring LED off
^[[B^Cosmc@osmc-family-room:~$ sudo python pushButton.py --light
Push Button LED on
^Cosmc@osmc-family-room:~nano pushButton.pyht
osmc@osmc-family-room:~$ sudo python pushButton.py --off
Push Button Ring LED off
^[[A^[[A^Cosmc@osmc-familsudo python pushButton.py --light
Push Button LED on
^Cosmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py --light
Push Button LED on
^Cosmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py --light
  File "pushButton.py", line 75
    print(button time = " + str(button_time))
                    ^
SyntaxError: invalid syntax
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py --light
Push Button LED on
in interrupt = 23
start time = 1560034123.46
button is up
Traceback (most recent call last):
  File "pushButton.py", line 75, in resetInterrupt
    print("button time = " + str(button_time))
NameError: global name 'button_time' is not defined
in interrupt = 23
start time = 1560034132.82
button is up
Traceback (most recent call last):
  File "pushButton.py", line 75, in resetInterrupt
    print("button time = " + str(button_time))
NameError: global name 'button_time' is not defined
in interrupt = 23
start time = 1560034135.63
^Csys.excepthook is missing
lost sys.stderr
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py --light
Push Button LED on
in interrupt = 23
start time = 1560035090.69
button is up
button time = 10.5082941055
Shutting down
Shutdown scheduled for Sat 2019-06-08 18:05:01 CDT, use 'shutdown -c' to cancel.
in interrupt = 23
start time = 1560035101.23
Connection to osmc-family-room closed by remote host.
Connection to osmc-family-room closed.
Jeffs-MBP:~ jeff$ ssh osmc@osmc-family-room
ssh: connect to host osmc-family-room port 22: Operation timed out
Jeffs-MBP:~ jeff$ ssh osmc@osmc-family-room
osmc@osmc-family-room's password: 
Linux osmc-family-room 4.14.78-4-osmc #1 SMP PREEMPT Wed Dec 12 17:58:11 UTC 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jun  8 17:13:34 2019 from 192.168.1.224
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py --light
Push Button LED on
in interrupt, channel = 23
start time = 1560035976.77

button is up
button time = 25.6822831631
Shutting down
Shutdown scheduled for Sat 2019-06-08 18:20:02 CDT, use 'shutdown -c' to cancel.
in interrupt, channel = 23
start time = 1560036002.5
Connection to osmc-family-room closed by remote host.
Connection to osmc-family-room closed.
Jeffs-MBP:~ jeff$ ssh osmc@osmc-family-room
osmc@osmc-family-room's password: 
Linux osmc-family-room 4.14.78-4-osmc #1 SMP PREEMPT Wed Dec 12 17:58:11 UTC 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jun  8 18:07:16 2019 from 192.168.1.224
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py --light
Push Button LED on
in interrupt, channel = 23
last time = 1560036854.21
in interrupt, channel = 23
next time = 1560036881.33
Traceback (most recent call last):
  File "pushButton.py", line 82, in resetInterrupt
    buttonTime = nextTime - lastTime
UnboundLocalError: local variable 'lastTime' referenced before assignment
^Cosmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py --light
Push Button LED on
in interrupt, channel = 23
last time = 1560036985.85
in interrupt, channel = 23
next time = 1560037053.55
button time = 67.7017481327
in interrupt, channel = 23
next time = 1560037086.1
button time = 32.5467028618
in interrupt, channel = 23
next time = 1560037100.8
button time = 14.6997220516
in interrupt, channel = 23
next time = 1560037105.53
button time = 4.73522400856
in interrupt, channel = 23
next time = 1560037112.34
button time = 11.5377259254
in interrupt, channel = 23
next time = 1560037113.89
button time = 1.54814004898
rebooting
Connection to osmc-family-room closed by remote host.
Connection to osmc-family-room closed.
Jeffs-MBP:~ jeff$ ssh osmc@osmc-family-room
osmc@osmc-family-room's password: 
Linux osmc-family-room 4.14.78-4-osmc #1 SMP PREEMPT Wed Dec 12 17:58:11 UTC 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jun  8 18:34:28 2019 from 192.168.1.224
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py --light
Push Button LED on
in interrupt, channel = 23
last time = 1560037277.52
in interrupt, channel = 23
next time = 1560037277.98
button time = 0.455246210098
in interrupt, channel = 23
next time = 1560037302.98
button time = 25.4572911263
resetting last time = 1560037302.98
in interrupt, channel = 23
next time = 1560037312.54
button time = 9.55523204803
Shutting down
Shutdown scheduled for Sat 2019-06-08 18:41:52 CDT, use 'shutdown -c' to cancel.
Connection to osmc-family-room closed by remote host.
Connection to osmc-family-room closed.
Jeffs-MBP:~ jeff$ ssh osmc@osmc-family-room
osmc@osmc-family-room's password: 
Linux osmc-family-room 4.14.78-4-osmc #1 SMP PREEMPT Wed Dec 12 17:58:11 UTC 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jun  8 18:39:42 2019 from 192.168.1.224
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py --light
Push Button LED on
in interrupt, channel = 23
last time = 1560037393.44
in interrupt, channel = 23
next time = 1560037395.04
button time = 1.59085702896
rebooting
Connection to osmc-family-room closed by remote host.
Connection to osmc-family-room closed.
Jeffs-MBP:~ jeff$ ssh osmc@osmc-family-room
osmc@osmc-family-room's password: 
Linux osmc-family-room 4.14.78-4-osmc #1 SMP PREEMPT Wed Dec 12 17:58:11 UTC 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jun  8 18:42:20 2019 from 192.168.1.224
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ sudo python pushButton.py --light
Push Button LED on
in interrupt, channel = 23
last time = 1560037588.6
in interrupt, channel = 23
next time = 1560037678.01
button time = 89.4120731354
resetting last time = 1560037678.01
^Cosmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ nano pushButton.py
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ 
osmc@osmc-family-room:~$ nano pushButton.py

  GNU nano 2.7.4                              File: pushButton.py                                        

#!/usr/bin/env python

#########################
#
# pushButton.py controls Adafruit's Momentary Rugged Metal Pushbutton with Blue
# LED Ring. The script turns on the led when a Raspberry Pi is running, and it
# will shutdown the Raspberry Pi if the button is pushed twice within 3 seconds
# or reboot if pushed twice more than 10 seconds and less than 20 seconds apart.
#
# The choice of a momentary push button was the wrong choice.
#
# Adafruit's momentary rugged blue led  button has five pins:
#   +   = power, which attaches to GPIO_LED pin
#   -   = ground, which attaches to ground
#   NO1 = Normally open, which is attached to GPIO_RESET pin
#   NC1 = Normally Closed, which is not used
#   C1  = This is not used

# I use three question (???) marks to indicate features that are not quite
# finished
#   ??? add logfile - nothing is being written to the logfile
#   ??? move from init.d to systemd
#
# pushButton.py was tested on a Raspberry Pi 3 model B+ running raspbian
# stretch and osmc
#
# Run the script using the command:
#   $ sudo python pushButton.py --light
#
# pushButton.py requires:
#   $ sudo apt-get install python-pip python-dev gcc
#   $ sudo pip install rpi.gpio
#
# Previous versions of this script used the "run pins" on the Raspberry Pi.
# This approach had two drawbacks: 1) shorting the run pins can allow the
# microSD card to become corrupt and require it to be reflashed, 2) the run
# pins required soldering headers on the Raspberry Pi.
#
# This script either reboots the Raspberry Pi or does a proper shutdown.

#########################
import RPi.GPIO as GPIO
import subprocess
import argparse
import time
import datetime

#########################
# Global Constants
HOME = "/home/osmc"
# Don't use run pins or GPIO 4
GPIO_RESET = 23
GPIO_LED = 24

#########################
# Global Variables
fileLog = open(HOME + '/pushButton.log', 'w+')
firstPush = True
lastTime = 0
nextTime = 0

#########################
# Log messages should be time stamped
def timeStamp():
    t = time.time()
    s = datetime.datetime.fromtimestamp(t).strftime('%Y/%m/%d %H:%M:%S - ')
    return s

# Write messages in a standard format
def printMsg(s):
    fileLog.write(timeStamp() + s + "\n")

# from https://raspberrypi.stackexchange.com/questions/63512/how-can-i-detect-how-long-a-button-is-press$
def resetInterrupt(channel):
    global lastTime
    global nextTime
    global firstPush

    # print("in interrupt, channel = " + str(channel))
    if firstPush:
        lastTime = time.time()
        firstPush = False
        # print("last time = " + str(lastTime))
        return
    else:
        nextTime = time.time()
        # print("next time = " + str(nextTime))

    buttonTime = nextTime - lastTime

    # print("button time = " + str(buttonTime))

    if buttonTime >= 10 and buttonTime <= 20:
        # print("Shutting down")
        printMsg("Shutting down")
        cmd = "sudo shutdown -h 0"
        subprocess.call(cmd, shell=True)
    elif buttonTime >= 0.5 and buttonTime <= 3:
        # print("rebooting")
        printMsg("Rebooting")
        cmd = "sudo reboot"
        subprocess.call(cmd, shell=True)
    elif buttonTime > 20:
        # print("resetting last time = " + str(lastTime))
        lastTime = nextTime

#########################
# start of main
parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument("-l", "--light", action="store_true")
group.add_argument("-o", "--off", action="store_true")

# Disable warnings
GPIO.setwarnings(False)

# turn on gpio pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_RESET, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(GPIO_RESET, GPIO.FALLING, callback=resetInterrupt)

GPIO.setup(GPIO_LED, GPIO.OUT)

# parse arguments
args = parser.parse_args()
if args.light:
    # print("Push Button LED on")
    GPIO.output(GPIO_LED,True)
elif args.off:
    # print("Push Button Ring LED off")
    GPIO.output(GPIO_LED,False)

try:
    while True:
        # there is no point in running all the time
        time.sleep(10000)

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    printMsg("keyboard exception occurred")

except Exception as ex:
    printMsg("ERROR: an unhandled exception occurred: " + str(ex))

finally:
    GPIO.cleanup()
    printMsg("pushButton terminated")
    fileLog.close()
