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
