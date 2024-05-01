# Treescript Files
Obtain the File Paths from TreeScript.

## How To
Provide the TreeScript file as an argument to treescript-files.
```
treescript-files ./script.tree
```
This will print out a list of the paths to each file in the tree.

### Parent Dir
To prefix the Tree, add the parent argument.
```
treescript-files ./script.tree --parent=~/projects/
```
This will add the parent directory to all files printed.
