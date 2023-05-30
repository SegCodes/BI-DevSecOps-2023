#! /bin/bash

items=$(ls)

for item in $items
do
	if [[ -f $item ]]
	then
		echo "Scanning $item..."
		if [[ $(grep -c PASSWORD $item) -gt 1 ]]
		then
			echo "Found PASSWORD in $item, removing..."
			rm $item
			echo "Removed Successfully."
		fi
	fi
done
