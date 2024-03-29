
CHROME_OPTIONS = [
    # '--headless',
    '--start-maximized',
    '--no-sandbox',
    '--disable-gpu',
    '--user-data-dir=/tmp/user-data',
    '--hide-scrollbars',
    '--enable-logging',
    '--log-level=0',
    '--v=99',
    '--data-path=/tmp/data-path',
    '--ignore-certificate-errors',
    '--homedir=/tmp',
    '--disk-cache-dir=/tmp/cache-dir',
    'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    '--disable-blink-features=AutomationControlled'
]
