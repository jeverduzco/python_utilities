# Python utilities
Tools for my daily life made in python

## Usage
* Clone this repo
* Open folder in VS Code
* Open utlity file

If you have a python utility that you want to share just make a pull request.

## Instructions by utility

### Password generator

By default this utility generates a random password of 20 characters and does not accept any input arguments.

To use it just do the following:

```
$ python3 password_generator.py
```
The result is a random password of 20 characters:
```
$ The new password is: &fEaG!C#d1#))7$53!6)
```

### Certificate converter

This utility helps to convert a .pem certificate into a .pfx certificate for use in Windows or Azure environments.

To use it just run the following command with its arguments and valid paths:

```
$ python3 certificate_converter.py 
                     --cert /path/to/cert.pem 
                     --key /path/to/key.pem 
                     --passphrase PassPhraseOfPrivateKey 
                     --out /path/to/cert.pfx
```