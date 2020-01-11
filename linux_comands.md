
# Linux basic commands

`pwd` => Show current diretory.
`ls` => Show directories and files in current directory.


### Basic command syntax

    <command> <option> <args>

#### Example

    ls --all --human_readable -l ~/my_dir

#### You can use short versions of options:

    ls -ahl ~/my_dir


`man` _command_ => Get help about a command.

`clear` => Clear terminal window.

`exit` => Close the terminal.

`ctrl-alt-t` - Open terminal.

`mkdir` _path_  => Create new directory in path.
* `-p`  => Option for create all directories in path.


`touch` => Create a file.

`cd` => Go to a directory.

`rm` => Delete a file.
+ `-r` => Option for delete a diretory too.
+ `rf` => option for delete without questitons.

`cp` _path1_ to  _path2_ => Copy file from _path1_ into _path2_
* `-r` => Option for copy a directory.

`mv` => Move file or directory.

## Running executable files from terminal
Then you run some programms from terminal, this terminal window will be
blocked and it will not react to other commands.

To run some programm, just type it name or alias in console and press **Enter**.

`ctrl + c` => Terminate running programm.
`ctrl + z` => Stop running programm for a time.

You can use `fg` for resume programm in _foreground_ mode
or `bg` for resume programm in _background_ mode.

`chmod` => Change file modes and permissions.
* `+x` =>  For adding a ***executable*** mode for a file.

## Simple text viewing and editing

`cat` _path_ => Show text file content in terminal.

`less` _path_ => Opet text file in new window.
You can use next commands:
* `q` for **exit**
* `/` for **search**
* `g` for going to **start**
* `G` for going to **end**

`nano` => Simple text editor.
* `ctrl + x` for **exit**


## Input and Output in programms

#### Basic syntax:
    <programm> <mode> <file>

#### Control
programm `<` file  =>  for **stdin** from file

programm `>` file  =>  for **stdout** to file

programm `>>` file  =>  for **stdout** to file with add new info


programm `2>` or `2>>` for **stderr** to file

## Pipe
**Pipe** is chain of two or more programms,
where **output** of first programm is **input** for second programm.

#### Basic sintax:
    <programm_1> | <programm_2> | ... | <programm_N>

## Downloading files from Internet

`wget` _link_ => Command for download file by link to current directory.

#### Basic commands

Use `-P path` for saving in another place with original name of file.
Use `-O path` for saving in another place with new name.

`-c` => for continue downloading.
`--spider` => check for file available.
`-i` => download files by links from text file.

#### Advanced commands

`-r -l` _deep_ _link_
Reccurent downloading file by link for setted deep.

`-r -A type1, type2, typeN` -_link_-
Reccurent downloading setted type files.


## Working with arhives.

#### Unpack arhive

`unzip` _file.zip_ => Unpack zip arhive.

`gungip` _file.gz_ => Unpack gz arhive and delete it.

#### Create arhive

`zip` _arhive_name.zip_ _files sep by comma_
Create a zip arhive.

`gzip` _filename_
Create a gz arhive and delete file. Can't arhive more, than 1 file or directory.

**Create many files gz arhive**
1. Create `tar` arhive by:
        tar -cvf arhive_name.tar file1 file2 dir etc
2.  Create `gz` archive by:
        gzip arhive_name.tar

**`Tar` commands:**
* `-c` -> for create archive
*  `-v` -> for show work info
*  `-f` -> for creating files in systems filesystem **! REQUIRED !**
and should be last.

You can easily arhive by `tar` with one line:

    tar -zcvf arhive_name.tar.gz file1 file2 dir1 etc...

And unpack arhive:

    tar -xvf arhive.tar

    tar -xzvf arhive.tar.gz


## Searching files by terminal

`find`

#### Basic sintax:
    find <dir_name> -name "<file_name>"

`grep`

#### Basic sintax:
    grep "str" filename

`-c` for count
`-r dirname` for find in all files in dir
