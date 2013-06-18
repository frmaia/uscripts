#!/bin/bash 

## 
## A simple way to monitore your free mem and run some troubleshooting when necessary.
##

if [ -z $1 ] ; then
  echo "usage: '$0 <threshold_percent> [ admin_mail_addr ]'"
  echo "--------------------------------------------------------"
  echo "  <threshold_percent> -Threshold percent for free mem"
  echo "  [ admin_mail_addr ] - sys admin mail address that will receive a feedback when some throubleshooting action be done. ( 'mutt' must be installed )"
  exit 1
fi 

log_file=$(mktemp)

#Threshold - minimal percent of free mem 
free_mem_threshold=$1
email_admin=$2

get_free_mem(){
  echo $(free | grep Mem | awk '{printf ("%0.f", ($4+$7)/$2 * 100.0)}')
} 

do_troubleshooting_actions() {
    echo "******************************"

    ### Throubleshooting Examples:
    
    #echo -e "\n\n#Restarting supervisord ...\n"
    #/etc/init.d/supervisor stop && /etc/init.d/supervisor start; sleep 60 ;
    
    #echo "Checking 'foo' service port"
    #nc -zv localhost 8888

    #echo "Checking 'mysql' service port"
    #nc -zv localhost 8888

    echo "******************************"

}

send_mail_to_admin() {
  if [ ! -z email_admin ]; then
    cat $1 | mutt -s "free_mem_fix -- $(hostname)" -- $email_admin
  fi
}

main() {
  free_mem=$(get_free_mem)
  if [ $free_mem -lt $free_mem_threshold ] ; 
    then
      echo "Critical free mem = ${free_mem}%! Threshold is ${free_mem_threshold}%. Running troubleshooting_actions." |tee -a $log_file 2>>$log_file
      do_troubleshooting_actions |tee -a $log_file 2>>$log_file
      echo "Now, free mem = $(get_free_mem)%!!!" |tee -a $log_file 2>>$log_file
      send_mail_to_admin $log_file
    else
      echo "Ok! free mem = ${free_mem}%. Threshold is ${free_mem_threshold}%."
  fi
}

main