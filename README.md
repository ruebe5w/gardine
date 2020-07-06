# gardine

crontab:
*/15 * * * * ps ax | grep 'gardine.py' | grep -v 'grep'  || bash /home/piscripts/gardine/start.sh > /home/pi/scrpts/gardine/gardine.log
@reboot ps ax | grep 'gardine.py' | grep -v 'grep'  || bash /home/pi/scripts/gardine/start.sh >/home/pi/scripts/gardine/gardine.log 2>&1
