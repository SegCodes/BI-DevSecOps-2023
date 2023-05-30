#! /bin/bash

printf "users> "

read input
while [[ $input != "exit" ]]
do
	case $input in
		'create '*)
			userName=$(echo $input | cut -d ' ' -f 2)
			if [[ -f $userName.user ]]
			then
				echo "$userName already exists. Please choose another name."
			else
				printf "User: %s\nPassword: %s" $userName $RANDOM > $userName.user
				echo "Created $userName successfully."
			fi
			;;
		'find '*)
			userName=$(echo $input | cut -d ' ' -f 2)
			if [[ ! -f $userName.user ]]
			then
				echo "$userName does not exist."
			else
				cat $userName.user
				printf "\n"
			fi
			;;
		'del '*)
			userName=$(echo $input | cut -d ' ' -f 2)
			if [[ ! -f $userName.user ]]
			then
				echo "Cannot delete $userName: does not exist."
			else
				rm $userName.user
				echo "Deleted $userName successfully."
			fi
			;;
		'list')
			if [[ $(ls *.user | wc -l) -lt 1 ]]
			then
				echo "There are no users."
			else
				for file in $(ls *.user)
				do
					user=$(echo $file | cut -d '.' -f 1)
					printf "%s\n" $user
				done
			fi
			;;
		'exit')
			break
			;;
		'help')
			printf "======Available Commands======\n1) create <user> - Creates a new user.\n2) find <user> - Prints the info of the user.\n3) del <user> - Deletes the user.\n4) list - Lists all the users.\n5) exit - Exits the program.\n==============================\n"
			;;
		*)
			echo "Invalid command. User help to see the available commands."
			;;
	esac
	printf "users> "
	read input
done
