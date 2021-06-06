#!/bin/bash
########## Author :- TARUN ARORA ##########
cd `dirname $0`
source colors.sh
clear
isexpert=1
if [  "$#" -eq  "0"  ]
    then
    isexpert=0
    echo "";
    printf "\t\t\t     \033[7;1;36m UNIX HELP MAIN MENU ${ENDCOLOUR}\n"
    echo "                                     "
    printf "    ${GREEN}1${ENDCOLOUR}  -- File and Directory Management Commands\n"
    printf "    ${GREEN}2${ENDCOLOUR}  -- Text Processing Commands\n"
    printf "    ${GREEN}3${ENDCOLOUR}  -- System Status Commands\n"
    printf "    ${GREEN}4${ENDCOLOUR}  -- \033[1;31mExit \033[0m\n"
    echo "                                     "
    printf "\033[1;35mEnter your choice: \033[0m" 
    flag=1;
    while [ $flag -eq 1 ]
        do
        read choice
        if [[ "$choice" =~ ^[1-4]$ ]]
        then
            flag=0
        else 
            printf "${RED}Enter a valid choice: ${ENDCOLOUR}"
        fi
        done;

    if [ $choice -eq 1 ]
    then
        printf "${GREEN}Opening the File management Submenu ${ENDCOLOUR}"
        ./spinner.sh sleep 3
        clear
        exec ./file.sh $isexpert

    elif [ $choice -eq 2 ]
    then
        printf "${GREEN}Opening the Text Processing Submenu ${ENDCOLOUR}"
        ./spinner.sh sleep 3
        clear
        exec ./text.sh $isexpert
    elif [ $choice -eq 3 ]
    then
        printf "${GREEN}Opening the System Status Submenu ${ENDCOLOUR}"
        ./spinner.sh sleep 3
        clear
        exec ./system.sh $isexpert
    else
        printf "\033[1;31mExiting the Program\033[0m\n"
        ./spinner.sh sleep 2
        exit 
    fi
    elif [ "$1" != "help" -a "$1" != "status" -a "$1" != "text" -a "$1" != "file" ]
    then
        printf "${BLUE}Enter a valid argument to Enter the Expert Mode.${ENDCOLOUR}\n"
        printf "${GREEN}\t-- file\n\t-- text\n\t-- status\n\t-- help\n${ENDCOLOUR}"
        printf "\033[1;31mExiting the Program\033[0m\n"
        ./spinner.sh sleep 2
        exit 1
    elif [ "$1" == "file" ]
    then
        printf "\n\t\t\t \033[7;1;36m Welcome to the Expert Mode !! \n\n${ENDCOLOUR}"
        printf "${GREEN}Opening the File management Submenu ${ENDCOLOUR}"
        ./spinner.sh sleep 3
        clear
        exec ./file.sh $isexpert
    elif [ "$1" == "text" ]
    then
        printf "\n\t\t\t \033[7;1;36m Welcome to the Expert Mode !! \n\n${ENDCOLOUR}"
        printf "${GREEN}Opening the Text Processing Submenu ${ENDCOLOUR}"
        ./spinner.sh sleep 3
        clear
        exec ./text.sh $isexpert
    elif [ "$1" == "status" ]
    then
        printf "\n\t\t\t \033[7;1;36m Welcome to the Expert Mode !! \n\n${ENDCOLOUR}"
        printf "${GREEN}Opening the System Status Submenu ${ENDCOLOUR}"
        ./spinner.sh sleep 3
        clear
        exec ./system.sh $isexpert
    elif [ "$1" == "help" ]
    then
        printf "${BLUE}Loading content about the program ...${ENDCOLOUR} "
        ./spinner.sh sleep 3
        clear
        exec ./help.sh
    fi