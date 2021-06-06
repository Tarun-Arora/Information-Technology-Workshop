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
        read choice
        if [[ "$choice" =~ ^[1-6]$ ]]
        then
            flag=0
        else 
            printf "${RED}Enter a valid choice: ${ENDCOLOUR}"
        fi
        done;
}

function display_file_content(){
    echo -n 'Enter the Path of File which you want to view: '   
    read file
    while [[ ! -f "$file" ]]
    do 
        echo -n "Enter a Valid Path: "
        read file
    done  
    if ! cat $file
    then
        echo "An Error occured while Displaying the contents of file";
    fi
}

function remove_file(){
    echo -n 'Enter the Path of File which you want to remove: '    
    read file
    while [[ ! -f "$file" ]]
    do 
        echo -n "Enter a Valid Path: "
        read file
    done  
    if ! rm $file
    then
        echo "An Error occured while removing the file";
    else echo "$file removed successfully.";
    fi
}

function copy_file(){
    echo -n 'Enter the Path of File from which content is to be copied: '    
    read file1
    while [[ ! -f "$file1" ]]
    do 
        echo -n "Enter a Valid Path: "
        read file1
    done 
    echo -n 'Enter the path of the file onto which content is to be pasted: '
    read file2
    if ! cp $file1 $file2
    then
        echo "An Error occured while copying content of the file";
    else echo "Contents copied successfully";
    fi
}

function list_file(){
    echo -n 'Enter the Path of File which you want to list: '   
    read file
    while [[ ! -f "$file" ]]
    do 
        echo -n "Enter a Valid Path: "
        read file
    done  
    if ! ls $file -l
    then
        echo "An Error occured while listing the file details";
    fi
}

function size_of_file(){
    echo -n 'Enter the Path of File: '   
    read file
    while [ ! -f $file ]
    do 
    echo -n "Enter Valid Path: "
    read file
    done  
    ls -sh $file | awk '{ if(NR==1) print $1 }'
}
clear
printf "\n\t\t     \033[7;1;36m FILE AND DIRECTORY MANAGEMENT COMMANDS ${ENDCOLOUR}\n\n"
printf "    ${GREEN}1${ENDCOLOUR}  -- Display the contents of a file\n"
printf "    ${GREEN}2${ENDCOLOUR}  -- Remove a file \n"
printf "    ${GREEN}3${ENDCOLOUR}  -- Copy a file\n"
printf "    ${GREEN}4${ENDCOLOUR}  -- List a file\n"
printf "    ${GREEN}5${ENDCOLOUR}  -- Size of a file\n"
if [ "$1" == "1" ]
 then 
    printf "    ${GREEN}6${ENDCOLOUR}  -- \033[1;31mExit\033[0m the program\n"   # Expert Mode               
else  
    printf "    ${GREEN}6${ENDCOLOUR}  -- \033[1;31mQuit\033[0m -- Return to main Menu\n"   # Novice Mode
fi
echo ""
takechoice


while [ 1 ]
do
if [ $choice -eq 1 ]
then
    display_file_content
fi

if [ $choice -eq 2 ]
then
    remove_file
fi

if [ $choice -eq 3 ]
then
    copy_file;
fi

if [ $choice -eq 4 ]
then
    list_file
fi

if [ $choice -eq 5 ]
then
    size_of_file
fi

if [ $choice -eq 6 ]
then
    if [ "$1" == 1 ]
    then 
    printf "\033[1;31mExiting the Program\033[0m\n"
    ./spinner.sh sleep 3
    exit
    else
    echo "Returning to the Main Menu";
    ./spinner.sh sleep 3
    clear
    exec ./myhelp.sh
    fi
fi
takechoice
done