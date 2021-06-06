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
        read opt
        if [[ "$opt" =~ ^[1-4]$ ]]
        then
            flag=0
        else 
            printf "${RED}Enter a valid choice: ${ENDCOLOUR}"
        fi
        done;
}

if [ $1 -eq 1 ];
then
printf "\n\t\t\t  \033[7;1;36m TEXT PROCESSING COMMANDS ${ENDCOLOUR}\n\n    ${GREEN}1${ENDCOLOUR}  -- Search a file for a pattern
    ${GREEN}2${ENDCOLOUR}  -- Count lines, words, and characters in specified files
    ${GREEN}3${ENDCOLOUR}  -- Display line differences between two files
    ${GREEN}4${ENDCOLOUR}  -- ${RED}Exit Program${ENDCOLOUR}
\n" | more
else
printf "\n\t\t\t  \033[7;1;36m TEXT PROCESSING COMMANDS ${ENDCOLOUR}\n\n    ${GREEN}1${ENDCOLOUR}  -- Search a file for a pattern
    ${GREEN}2${ENDCOLOUR}  -- Count lines, words, and characters in specified files
    ${GREEN}3${ENDCOLOUR}  -- Display line differences between two files
    ${GREEN}4${ENDCOLOUR}  -- ${RED}Quit${ENDCOLOUR} -- Return to Main Menu\n\n" | more
fi

takechoice

while [ 1 ]
do
if [ $opt -eq 1 ];
then
    printf "\nEnter file to check for pattern : "
    read file
    while [[ ! -f "$file" ]]
    do 
        echo -n "Enter a Valid Path: "
        read file
    done
    echo ""
    echo -n "Enter pattern to search for : "
    read pattern
    echo ""
    if ! grep -E $pattern $file
    then
        echo "An Error occurred which searching for the pattern";
    fi
    echo ""
elif [ $opt -eq 2 ];
then
    printf "\nEnter filename : "
    read file
    while [[ ! -f "$file" ]]
    do 
        echo -n "Enter a Valid Path : "
        read file
    done
    echo ""
    echo -n "Number of line : "
    wc -l $file | awk '{ print $1 }'
    echo -n "Number of words : "
    wc -w $file | awk '{ print $1 }'
    echo -n "Number of characters : "
    wc -c $file | awk '{ print $1 }'
elif [ $opt -eq 3 ];
then
    printf "\nEnter path of first file : "
    read file1
    while [[ ! -f "$file1" ]]
    do 
        echo -n "Enter a Valid Path: "
        read file1
    done
    echo -n "Now Enter path of second file : "
    read file
    while [[ ! -f "$file" ]]
    do 
        echo -n "Enter a Valid Path: "
        read file
    done
    echo "The differences (if any) in the content of the files are shown below :- "
    diff $file1 $file;
    echo ""

elif [ $opt -eq 4 -a $1 -eq 0 ];
then
    echo "Returning to the Main Menu";
    ./spinner.sh sleep 3
    clear
    exec ./myhelp.sh
elif [ $opt -eq 4 -a $1 -eq 1 ];
then
    printf "\033[1;31mExiting the Program\033[0m\n"
  ./spinner.sh sleep 3
  exit
fi
takechoice
done
