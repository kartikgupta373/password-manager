<h1>Password Manager and Random Password Generator</h1>

<p>
  The project is a password manager which asks the user for a username and a password linked to that username and it can later fetch all those passwords for user to see.
</p>
<br>
<p>
  The catch of the program is that the user is authenticated at the beginning of the program and if the user enters the wrong master password, 
then the program will give a pseudo entry with garbage values for operations and will not return any useful information.
</p>
<br>
<p>
  The master password when entered correct, will allow the user to add a username and password, 
view the saved passwords, create a random password and quit the program whenever they choose to.
</p>
<br>
<p>
  The file used to save the passwords uses an encryption method from the python library cryptography.fernet to save the passwords which uses AES encryption to save the data. 
  This means if the password file is being accessed by unauthorized parties, they will not be able to access any data from it. 
  Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography.
</p>
<br>
<p>The random password generator as the name suggests helps generate random passwords of desired length by the user. It uses random ascii letters to create randomized strong passwords.
</p>
<br>
<p>
We create a key in the beginning of the execution of the program which is to be run only once. 
  It creates a unique key that will be used to encrypt and decrypt the data of the passwords which use encryption to store the data in bytes format. 
  A key.key file is used to store the key and the passwords.txt file makes use of that key to decode the passwords when the user is authorized and authenticated.
</p>

