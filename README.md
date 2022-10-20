# Gmailer
Sends email via a Gmail account.

## Notes
### Gmail app passwords
Signing into Gmail with an app password: https://support.google.com/accounts/answer/185833

### Configuration file
* Rename configTEMPLATE.json to config.json
* Add your Gmail information to config.json

# Usage
* Call the * *send_email()* * function, passing in the following arguments:
  * recipient (str): the recipient's email address.
  * subject (str): the email subject.
  * message (str): the body of the email.
