import os
import pyotp
import subprocess
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    # Secret key
    secret_key = os.getenv('SECRET_KEY')

    # Generate TOTP code
    totp = pyotp.TOTP(secret_key)
    code = totp.now()

    # Get username and password
    username = os.getenv('USERNAME')
    password = os.getenv('SAML2AWS_PASSWORD')
    aws_profile = os.getenv('AWS_PROFILE')

    if not password:
        print('Error: SAML2AWS_PASSWORD environment variable is not set.')
        return

    # Command to run
    cmd = [
        'saml2aws', 'login',
        '--idp-account', os.getenv('SAML2AWS_IDP_ACCOUNT'),
        '--profile', aws_profile,
        '--username', username,
        '--password', password,
        '--mfa-token', code,
        '--role', os.getenv('SAML2AWS_ROLE'),
        '--skip-prompt'
    ]

    # Run the command
    result = subprocess.run(cmd, text=True, capture_output=True)

    # Check the result
    if result.returncode == 0:
        print(f'saml2aws login successful with {aws_profile}')
        print(result.stdout)
    else:
        print('saml2aws login failed')
        print('Output:', result.stdout)
        print('Error:', result.stderr)

if __name__ == '__main__':
    main()
