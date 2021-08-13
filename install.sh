#!/bin/bash
echo "Welcome to the installer of the Linux quiz!"
echo "First, please enter your language: German (D) or English (E)."



while true; do
    read -p "> " language
    case $language in
        [D]* ) cp src/DE src/active.py; break;;
        [E]* ) cp src/EN src/active.py;break;;
        * ) echo;echo "Please type 'D' for German or 'E' for English as language.";;
    esac
done

echo "Done!"

