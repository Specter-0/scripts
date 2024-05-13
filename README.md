# Scripts

### a Collection of CLI tool i have made

---

programs don't have the extension, just add it back, language can prob be read from the shebang 

---

## **To Use**

run the setup file to turn all files executables
change .setup into an executable using chmod
``` bash
chmod +x .setup.sh
```
then run
``` bash
.setup
```

then add the path to scripts to your shells config: bash *~/.bashrc* or zsh *~/.zshrc*
``` bash
export PATH="$HOME/replace/with/path/to/scripts:$PATH"
```
you should now be able to run the files as CLI tools

>#### If you can't get the path to work
> Move scripts folder to the home directory and use 
>``` bash
>export PATH="$HOME/scripts:$PATH"
>```
> as the path

---

# *Scripts docs*

## **gits**
#### Setup and push git with fast commands

usage: gits [message] [-h HELP] [-s SETUP]


positional arguments:
message **&lt;Commit message&gt;**


Flags:

-h, --help : **Show help message.**
 

-s, --setup : **initalize remote git and configure origin**
args: [**remote git repo**]

-o, --open : **Clone a github repo into current dir**
args: [**remote git repo**]

-r, --revert : **Undo all changes back to previus commit**

-l, --local : **Commit localy**

---

## **mkmf**
#### create makefiles for languages

usage: mkmf [language]

---

## **del**
#### fast sudo rm -rf delete

usage: del [file/dir] [-h HELP] [-p PASSWORD]


positional arguments:
To be deleted **&lt;File or Dir&gt;**


Flags:

-h, --help : **Show help message.**


-p : **Setup .env file with encrypted password**
args: [**password**]


---

## **play**
#### youtube mp3 player

usage: play [name] [-h HELP] [-a ADD] [-v, VOLUME] [-l PLAYLIST] [-d DELETE] [-r REPETE]


positional arguments:

named mp3 **&lt;Name&gt;**

previus **if 'previus' in place of name then play the previus song**

Flags:

-h, --help : **Show help message.**


-a, --add : **Add a mp3 from youtube by passing link, name must be uniqe**
args: [**name, youtube link**]


-v, --volume **Set the volume of the player**
args: [**(float) volume**]


-l, --playlist **Select a playlist, if it does not exist creates a new one, params after will be added to list**
args: [**playlist, item to add to playlist?...**]


-d, --delete **Delete a song or playlist, if selection a playlist and a second arg is passed, will remove song(s) for the playlist**
args: [**item, playlist items?...**]


-r, --repeat **Repeat chosen song**


--config: **Prints config to cmdline**

--store: **Prints all songs added to cmdline**


> Note: you can dump .mp3 files into music
> to run them as any other downloaded yt mp3.
> Remember: run without .mp3 extension

---

## **longmake**
#### run the makefile of a saved directory from anywhere 

usage: longmake [directory alias] [-h HELP] [-a ADD]


positional arguments:
args: **&lt;alias, &#42;kwargs&gt;**


Flags:

-h, --help : **Show help message.**

-a, --add : **Add a directory under an alias**
args: [**alias, path from home**]

-r, --args : **Add args to automaticaly run when running directory alias**
args: [**a saved dir alias, &#42;args &#42;kwargs**]

--config : **Display config file**

> Note: use &#x0060;pwd&#x0060; as the path to add current directory as target
> pwd: returns current working dir for home

---

## **mac**
#### run an api and frontend website in on terminal with one command

usage: mac [-h] [-a API API] [-f FRONTEND FRONTEND]


Flags:

-h, --help : **Show help message.**

-a, --api : **Configure api**
args: [**path to api directory, command as string**]

-f, --frontend : **Configure frontend**
args: [**path to frontend directory, command as string**]

> Note: To run normaly just run mac in terminal after configuration

---
