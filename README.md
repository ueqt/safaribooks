# SafariBooks
Download and generate *EPUB* of your favorite books from [*Safari Books Online*](https://www.safaribooksonline.com) library.  
I'm not responsible for the use of this program, this is only for *personal* and *educational* purpose.  
Before any usage please read the *O'Reilly*'s [Terms of Service](https://learning.oreilly.com/terms/).  

> ## ⚠ *Attention needed* ⚠ 
> *If you are a developer and want to help this project, please take a look to the current [Milestone](https://github.com/lorenzodifuccia/safaribooks/milestone/1)*.  
> *Checkout also the new APIv2 branch: [apiv2](https://github.com/lorenzodifuccia/safaribooks/tree/apiv2)*  
> *The Community thanks 🙏🏻*

## Overview:
  * [Requirements & Setup](#requirements--setup)
  * [Usage](#usage)
  * [Single Sign-On (SSO), Company, University Login](https://github.com/lorenzodifuccia/safaribooks/issues/150#issuecomment-555423085)
  * [Calibre EPUB conversion](https://github.com/lorenzodifuccia/safaribooks#calibre-epub-conversion)
  * [Example: Download *Test-Driven Development with Python, 2nd Edition*](#download-test-driven-development-with-python-2nd-edition)
  * [Example: Use or not the `--kindle` option](#use-or-not-the---kindle-option)

## Requirements & Setup:
First of all, it requires `python3` and `pip3` or `pipenv` to be installed.  
```shell
$ git clone https://github.com/lorenzodifuccia/safaribooks.git
Cloning into 'safaribooks'...

$ cd safaribooks/
$ pip3 install -r requirements.txt

OR

$ pipenv install && pipenv shell
```  

The program depends of only two **Python _3_** modules:
```python3
lxml>=4.1.1
requests>=2.20.0
```
  
## Usage:
It's really simple to use, just choose a book from the library and replace in the following command:
  * X-es with its ID, 
  * `email:password` with your own. 

```shell
$ python3 safaribooks.py --cred "account_mail@mail.com:password01" XXXXXXXXXXXXX
```

The ID is the digits that you find in the URL of the book description page:  
`https://www.safaribooksonline.com/library/view/book-name/XXXXXXXXXXXXX/`  
Like: `https://www.safaribooksonline.com/library/view/test-driven-development-with/9781491958698/`  
  
#### Program options:
```shell
$ python3 safaribooks.py --help
usage: safaribooks.py [--cred <EMAIL:PASS> | --login] [--no-cookies]
                      [--kindle] [--preserve-log] [--help]
                      <BOOK ID>

Download and generate an EPUB of your favorite books from Safari Books Online.

positional arguments:
  <BOOK ID>            Book digits ID that you want to download. You can find
                       it in the URL (X-es):
                       `https://learning.oreilly.com/library/view/book-
                       name/XXXXXXXXXXXXX/`

optional arguments:
  --cred <EMAIL:PASS>  Credentials used to perform the auth login on Safari
                       Books Online. Es. ` --cred
                       "account_mail@mail.com:password01" `.
  --login              Prompt for credentials used to perform the auth login
                       on Safari Books Online.
  --no-cookies         Prevent your session data to be saved into
                       `cookies.json` file.
  --kindle             Add some CSS rules that block overflow on `table` and
                       `pre` elements. Use this option if you're going to
                       export the EPUB to E-Readers like Amazon Kindle.
  --preserve-log       Leave the `info_XXXXXXXXXXXXX.log` file even if there
                       isn't any error.
  --help               Show this help message.
```
  
The first time you use the program, you'll have to specify your Safari Books Online account credentials (look [`here`](/../../issues/15) for special character).  
The next times you'll download a book, before session expires, you can omit the credential, because the program save your session cookies in a file called `cookies.json`.  
For **SSO**, please use the `sso_cookies.py` program in order to create the `cookies.json` file from the SSO cookies retrieved by your browser session (please follow [`these steps`](/../../issues/150#issuecomment-555423085)).  
  
Pay attention if you use a shared PC, because everyone that has access to your files can steal your session. 
If you don't want to cache the cookies, just use the `--no-cookies` option and provide all time your credential through the `--cred` option or the more safe `--login` one: this will prompt you for credential during the script execution.

You can configure proxies by setting on your system the environment variable `HTTPS_PROXY` or using the `USE_PROXY` directive into the script.

#### Calibre EPUB conversion
**Important**: since the script only download HTML pages and create a raw EPUB, many of the CSS and XML/HTML directives are wrong for an E-Reader. To ensure best quality of the output, I suggest you to always convert the `EPUB` obtained by the script to standard-`EPUB` with [Calibre](https://calibre-ebook.com/).
You can also use the command-line version of Calibre with `ebook-convert`, e.g.:
```bash
$ ebook-convert "XXXX/safaribooks/Books/Test-Driven Development with Python 2nd Edition (9781491958698)/9781491958698.epub" "XXXX/safaribooks/Books/Test-Driven Development with Python 2nd Edition (9781491958698)/9781491958698_CLEAR.epub"
```
After the execution, you can read the `9781491958698_CLEAR.epub` in every E-Reader and delete all other files.

The program offers also an option to ensure best compatibilities for who wants to export the `EPUB` to E-Readers like Amazon Kindle: `--kindle`, it blocks overflow on `table` and `pre` elements (see [example](#use-or-not-the---kindle-option)).  
In this case, I suggest you to convert the `EPUB` to `AZW3` with Calibre or to `MOBI`, remember in this case to select `Ignore margins` in the conversion options:  
  
![Calibre IgnoreMargins](https://github.com/lorenzodifuccia/cloudflare/raw/master/Images/safaribooks/safaribooks_calibre_IgnoreMargins.png "Select Ignore margins")  
  
## Examples:
  * ## Download [Test-Driven Development with Python, 2nd Edition](https://www.safaribooksonline.com/library/view/test-driven-development-with/9781491958698/):  
    ```shell
    $ python3 safaribooks.py --cred "my_email@gmail.com:MyPassword1!" 9781491958698

           ____     ___         _ 
          / __/__ _/ _/__ _____(_)
         _\ \/ _ `/ _/ _ `/ __/ / 
        /___/\_,_/_/ \_,_/_/ /_/  
          / _ )___  ___  / /__ ___
         / _  / _ \/ _ \/  '_/(_-<
        /____/\___/\___/_/\_\/___/

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    [-] Logging into Safari Books Online...
    [*] Retrieving book info... 
    [-] Title: Test-Driven Development with Python, 2nd Edition                     
    [-] Authors: Harry J.W. Percival                                                
    [-] Identifier: 9781491958698                                                   
    [-] ISBN: 9781491958704                                                         
    [-] Publishers: O'Reilly Media, Inc.                                            
    [-] Rights: Copyright © O'Reilly Media, Inc.                                    
    [-] Description: By taking you through the development of a real web application 
    from beginning to end, the second edition of this hands-on guide demonstrates the 
    practical advantages of test-driven development (TDD) with Python. You’ll learn 
    how to write and run tests before building each part of your app, and then develop
    the minimum amount of code required to pass those tests. The result? Clean code
    that works.In the process, you’ll learn the basics of Django, Selenium, Git, 
    jQuery, and Mock, along with curre...
    [-] Release Date: 2017-08-18
    [-] URL: https://learning.oreilly.com/library/view/test-driven-development-with/9781491958698/
    [*] Retrieving book chapters...                                                 
    [*] Output directory:                                                           
        /XXXX/safaribooks/Books/Test-Driven Development with Python 2nd Edition (9781491958698)
    [-] Downloading book contents... (53 chapters)                                  
        [#####################################################################] 100%
    [-] Downloading book CSSs... (2 files)                                          
        [#####################################################################] 100%
    [-] Downloading book images... (142 files)                                      
        [#####################################################################] 100%
    [-] Creating EPUB file...                                                       
    [*] Done: /XXXX/safaribooks/Books/Test-Driven Development with Python 2nd Edition 
    (9781491958698)/9781491958698.epub
    
        If you like it, please * this project on GitHub to make it known:
            https://github.com/lorenzodifuccia/safaribooks
        e don't forget to renew your Safari Books Online subscription:
            https://learning.oreilly.com
    
    [!] Bye!!
    ```  
     The result will be (opening the `EPUB` file with Calibre):  

    ![Book Appearance](https://github.com/lorenzodifuccia/cloudflare/raw/master/Images/safaribooks/safaribooks_example01_TDD.png "Book opened with Calibre")  
 
  * ## Use or not the `--kindle` option:
    ```bash
    $ python3 safaribooks.py --kindle 9781491958698
    ```  
    On the right, the book created with `--kindle` option, on the left without (default):  
    
    ![NoKindle Option](https://github.com/lorenzodifuccia/cloudflare/raw/master/Images/safaribooks/safaribooks_example02_NoKindle.png "Version compare")  
    
---  
  
## Thanks!!
For any kind of problem, please don't hesitate to open an issue here on *GitHub*.  
  
*Lorenzo Di Fuccia*

## usage

create cookies.json

```
{"OptanonAlertBoxClosed": "2022-06-21T04:56:02.472Z", "OptanonConsent": "isIABGlobal=false&datestamp=Tue+Jun+21+2022+12%3A56%3A02+GMT%2B0800+(China+Standard+Time)&version=6.25.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=SG%3B", "_evga_5802": "{%22uuid%22:%22ede3082c8ed85e3f%22%2C%22puid%22:%223elgTPX5tTcpFUZaAl8F_IrsHHDSKIH3WC7fxQLQNnWIzzl70IrmNHuJ3xonjeKEkZ5nUX4mHAV_AQfHm7p8gwDkRxxAcb4uxHNaLSpkx16-tbyxc35P0qOKtWGIhLK0%22%2C%22affinityId%22:%220CB%22}", "_ga": "GA1.1.1228601484.1655346787", "_ga_4WZYL59WMV": "GS1.1.1655781136.2.0.1655781136.60", "_ga_ZMQH4QCXDQ": "GS1.1.1655787049.8.1.1655787362.60", "_gat_UA-112091926-1": "1", "_gid": "GA1.2.1228942496.1655713795", "_mkto_trk": "id:107-FMS-070&token:_mch-oreilly.com-1655348667892-98625", "_sfid_472e": "{%22anonymousId%22:%22ede3082c8ed85e3f%22%2C%22consents%22:[]}", "_vis_opt_exp_195_combi": "2", "_vis_opt_s": "1%7C", "_vis_opt_test_cookie": "1", "_vwo_ds": "3%241655781138%3A23.35388259%3A%3A", "_vwo_uuid": "DA6082348FE871D616CFDD9FFCE6946B3", "_vwo_uuid_v2": "DA6082348FE871D616CFDD9FFCE6946B3|0e57fdf6d196cba27d55545217903790", "akaalb_LearningALB": "~op=learning_oreilly_com_GCP_ALB:learning_oreilly_com_gcp1|~rv=1~m=learning_oreilly_com_gcp1:0|~os=3284f997983d0bd4e10a6b83f3b25a7c~id=48afc206cab4ea09b93f82063fe60365", "amp_49f7a6": "iQJJF5g-V3w0O6sphvL2nu.OThmYzRjNGQtZmJiOC00YTRlLThjMjUtZWQ0ZjQ4Y2IzYWJm..1g629iku9.1g629s4iu.p.r.1k", "groot_sessionid": "bhsv7q55n2iz6vpfgyay2f3fmga8aq63", "orm-jwt": "", "orm-rt": "c40c48d7264b4ba8882d5a42604fe59f"}
```

change `orm-jwt` from `Application` `Cookies`
change `index.py` `TOTAL` from `https://learning.oreilly.com/topics/?sort=date_added&format=book`

```
python index.py
python all.py
node epub
node indexall
```