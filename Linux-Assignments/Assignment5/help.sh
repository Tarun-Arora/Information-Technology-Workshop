#!/bin/bash
########## Author :- TARUN ARORA ##########
cd `dirname $0`
source colors.sh
printf "\t\t        \033[7;1;36m ----- Welcome to ITW Project ----- ${ENDCOLOUR}\n
${GREY}To perform any task on this system all you have to do in select your choice of options from given.${ENDCOLOUR}\n
# In ${BLUE}File Menu${ENDCOLOUR} you will find commands like ls, cat, cp etc.\n
# In ${BLUE}System Status Menu${ENDCOLOUR} you will find commands like ps, df, date, printenv\n
# In ${BLUE}Text Menu${ENDCOLOUR} you will find commands like grep, diff, wc\n\n"

printf "\n              ${GREEN}------ Press any key to go back to main program ------${ENDCOLOUR}\n"
read opt
echo "Taking You to the Main Menu";
./spinner.sh sleep 1
echo "Getting Things Ready for you"
./spinner.sh sleep 1
clear
exec ./myhelp.sh
