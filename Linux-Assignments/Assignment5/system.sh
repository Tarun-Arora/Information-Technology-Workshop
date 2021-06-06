#!/bin/bash
########## Author :- TARUN ARORA ##########
cd `dirname $0`
source colors.sh
function takechoice ()
{
    printf "\033[1;35mEnter your choice: \033[0m"  
    flag=1;
    while [ $flag -eq 1 ]
        do
        read a
        if [[ "$a" =~ ^[1-5]$ ]]
        then
            flag=0
        else 
            printf "${RED}Enter a valid choice: ${ENDCOLOUR}"
        fi
        done;
}

if [ $1 -eq 1 ];
then
printf "\n\t\t\t     \033[7;1;36m SYSTEM STATUS COMMANDS ${ENDCOLOUR}\n\n    ${GREEN}1${ENDCOLOUR}  -- Display the current date and time
    ${GREEN}2${ENDCOLOUR}  -- Current disk usage
    ${GREEN}3${ENDCOLOUR}  -- List current local and enviornmental
    ${GREEN}4${ENDCOLOUR}  -- Display process status information
    ${GREEN}5${ENDCOLOUR}  -- \033[1;31mExit\033[0m the Program\n\n" | more
else
printf "\n\t\t\t     \033[7;1;36m SYSTEM STATUS COMMANDS ${ENDCOLOUR}\n\n    ${GREEN}1${ENDCOLOUR}  -- Display the current date and time
    ${GREEN}2${ENDCOLOUR}  -- Current disk usage
    ${GREEN}3${ENDCOLOUR}  -- List current local and enviornmental
    ${GREEN}4${ENDCOLOUR}  -- Display process status information
    ${GREEN}5${ENDCOLOUR}  -- \033[1;31mQuit\033[0m -- Return to Main Menu\n\n" | more
fi

takechoice

while ((1))
do
if [ "$a" -eq 1 ];
then
    echo ""
    date +"%d/%h/%Y %R"
    echo ""
elif [ "$a" -eq 2 ];
then
    echo ""
    df | more
    echo ""
elif [ "$a" -eq 3 ];
then
     echo ""
     printenv | more
     echo ""
elif [ "$a" -eq 4 ];
then
    echo ""
    ps -e | more
    echo ""
elif [ "$a" -eq 5 -a "$1" -eq 0 ];
then
    echo "Returning to the Main Menu";
    ./spinner.sh sleep 3
    clear
    exec ./myhelp.sh
elif [ "$a" -eq 5 -a "$1" -eq 1 ];
then
    printf "\033[1;31mExiting the Program\033[0m\n"
    ./spinner.sh sleep 3
    exit
fi
takechoice
done
