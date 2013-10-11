#! /bin/sh
### BEGIN INIT INFO
# Provides:          glassfish
# Required-Start:    $remote_fs $network $syslog
# Required-Stop:     $remote_fs $network $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Starts GlassFish
# Description:       Starts GlassFish application server
### END INIT INFO
 
# We need this, since NetworkServerControl uses $JAVA_HOME to find java
export JAVA_HOME=/usr/lib/jvm/java-8-oracle   #/usr/java/jdk1.7.0_25                         # Or whatever
# We need this, since asadmin contains the line 'JAVA=${AS_JAVA}/bin/java'
export AS_JAVA="$JAVA_HOME"

GLASSFISH=/home/mike/Dev/glassfish4   #/srv/glassfish
DERBY_BIN=/home/mike/Dev/glassfish4/javadb/bin   #/srv/glassfish/javadb/bin

case "$1" in
start)
  echo "Starting GlassFish from $GLASSFISH"
  sudo -u mike -E "$GLASSFISH/bin/asadmin" start-database
  sudo -u mike -E "$GLASSFISH/bin/asadmin" start-domain domain1
  ;;
stop)
  echo "Stopping GlassFish from $GLASSFISH"
  sudo -u mike -E "$GLASSFISH/bin/asadmin" stop-domain domain1
  sudo -u mike -E "$GLASSFISH/bin/asadmin" stop-database
  ;;
restart)
  $0 stop
  $0 start
  ;;
status)
  echo "# GlassFish at $GLASSFISH:"
  sudo -u mike -E "$GLASSFISH/bin/asadmin" list-domains | grep -v Command
  sudo -u mike -E "$GLASSFISH/bin/asadmin" list-domains | grep -q "domain1 running"
  if [ $? -eq 0 ]; then
    sudo -u mike -E "$GLASSFISH/bin/asadmin" uptime | grep -v Command
    echo "\n# Deployed applications:"
    sudo -u mike -E "$GLASSFISH/bin/asadmin" list-applications --long=true --resources | grep -v Command
    echo "\n# JDBC resources:"
    sudo -u mike -E "$GLASSFISH/bin/asadmin" list-jdbc-resources | grep "jdbc/"
  fi
  echo "\n# Derby:"
  sudo -u mike -E "$DERBY_BIN/NetworkServerControl" ping | sed "s/^.* : //"
  ;;
*)
  echo "Usage: $0 {start|stop|restart|status}"
  exit 1
  ;;
esac

exit 0
