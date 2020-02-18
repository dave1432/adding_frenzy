# Adding Frenzy
## Adding Frenzy Contest

Rules are simple. There is a test which tests function. Function has to add two numbers and return result. Make test pass.
But make it pass in most obscure, crazy and creative way you can.

## Installation guide

Clone repository.

Make virtualenv `python3 -m venv ~/adding_frenzy`, and activate it.

Install requirements `pip install -r requirements.txt`.

## Testing guide

Just `make test`.

## My answer

I've just used something that is called visual spoofing.
This is a method that uses different combinations of unicode characters to get a similiar output for example:

U+006F U+0336 U+0335	o̶̵

U+006F U+0335 U+0336	o̵̶

more about this is available via this link: http://websec.github.io/unicode-security-guide/visual-spoofing/

