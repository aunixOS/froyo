### Froyo a simple AUR helper written in Python and Shell
## Setup
you need to add the froyo shell script to you .local/bin directory
```sh
cd froyo
```
```sh
cp froyo-home-directory/froyo ~/.local/bin
```
then i like to chmod the froyo file
```sh 
chmod +x ~/.local/bin/froyo
```
you now need to create the froyo directory in /opt/ and move froyo.py there
```sh
sudo mkdir /opt/froyo
```
```sh
sudo cp froyo-home-directory/froyo.py /opt/froyo/
```
now when you run 
```sh
froyo
```

alternatively you could just run the setup script
it should be all setup

## Issues
if there is an issue (and there will be one) please open an issue
