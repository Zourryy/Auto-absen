
## Note

- PLease give me star if you like this tutorial <3.
- If you receive this error `OSError: [Errno 8] Exec format error: '/data/data/com.termux/files/usr/lib/python`**_X.YY_**`/site-packages/selenium/webdriver/common/linux/selenium-manager'`.
- Where **_X.YY_** is your Python version, example 3.8, 3.9, 3.10, 3.11, 3.12, ...
- That means you haven't installed the required package.
- Custom distro **&** modded termux **WON'T WORK**.

## Download

- Termux -> [F-Droid](https://f-droid.org/packages/com.termux/).
- <pre><code>pkg install python</code></pre>

## Requirements

| Step | Command                                                               |
| ---- | --------------------------------------------------------------------- |
| 1    | Open Termux                                                           |
| 2    | Allow access to storage memory                                        |
| 3    | <pre><code>termux-setup-storage</code></pre>                          |
| 4    | Force exit Termux                                                     |
| 5    | Reopen Termux                                                         |
| 6    | Update & Upgrade package                                              |
| 7    | <pre><code>yes \| pkg update -y && yes \| pkg upgrade -y</code></pre> |
| 8    | Install pip (they seperated it from python)                           |
| 9    | <pre><code>yes \| pkg install python-pip -y</code></pre>              |
| 10   | Install selenium                                                      |
| 11   | <pre><code>pip install selenium==4.9.1</code></pre>                   |

