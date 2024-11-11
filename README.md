# SAML MFA Auto-Auth Tool

This tool automates the AWS login process via SAML with Multi-Factor Authentication (MFA). It generates a Time-Based One-Time Password (TOTP) using a secret key, then uses `saml2aws` to handle the login flow. Environment variables are used to securely store required credentials and configuration.

## Features

- **Automated TOTP Generation**: Uses `pyotp` to generate a TOTP code for MFA, allowing seamless AWS login.
- **Integration with `saml2aws`**: Utilizes the `saml2aws` CLI tool for the AWS SAML login flow.
- **Configurable via `.env` File**: Environment variables are managed through a local `.env` file, allowing for easy setup and secure storage of credentials.

## Requirements

- **Python 3**
- **Python Packages**:
  - `pyotp`
  - `python-dotenv`
- **saml2aws**: Ensure that `saml2aws` is installed and configured with your Identity Provider (IdP) account.
  
_Note: Running the pip installation and the script in a virtual environment is recommended but not mandatory_

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jonfernz6/saml2aws-mfa-auto-auth.git
   cd saml2aws-mfa-auto-auth
   ```

2. **Install Dependencies**: Use `pip` to install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the `.env` File**: Create an `.env` file in the root directory with the following structure. Replace each placeholder with your actual values:

   ```plaintext
   USERNAME=your-username@example.com
   SECRET_KEY=your-secret-key
   SAML2AWS_PASSWORD=your-saml2aws-password
   AWS_PROFILE=your-aws-profile
   SAML2AWS_ROLE=your-aws-role-arn
   SAML2AWS_IDP_ACCOUNT=your-idp-account-name
   ```
_Note: Make sure to keep your .env file secure and avoid committing it to version control._

## Usage

To simplify running the tool, you can create an alias in your shell configuration file (e.g., `.zshrc` or `.bashrc`). This allows you to execute the script without needing to specify the full path each time.

**Add an Alias**: Open your shell configuration file and add an alias, replacing the path with your actual script location:

   ```bash
   alias samlautoauth='python /path/to/your/saml2aws-mfa-auto-auth/auto_saml2aws.py'
   ```
**Reload the Shell**: After saving the file, reload your shell:

```bash
source ~/.zshrc  # or source ~/.bashrc
```

**Run the Tool**: Now you can simply run:

```bash
samlautoauth
```

## How It Works
- The script loads configuration details from the `.env` file.
- It generates a TOTP code using the `SECRET_KEY` provided in the `.env` file.  
- The `USERNAME`, `SAML2AWS_PASSWORD`, `AWS_PROFILE`, `SAML2AWS_ROLE`, and `SAML2AWS_IDP_ACCOUNT` values are retrieved from `.env`.  
- The script uses `saml2aws` to log in to AWS using the generated TOTP code, completing the MFA process automatically.

## Example `.env` File
Below is an example of the `.env` file structure. Replace each placeholder with the appropriate information for your AWS and SAML setup.

```plaintext
USERNAME=your-username@example.com
SECRET_KEY=your-secret-key
SAML2AWS_PASSWORD=your-saml2aws-password
AWS_PROFILE=your-aws-profile
SAML2AWS_ROLE=your-aws-role-arn
SAML2AWS_IDP_ACCOUNT=your-idp-account-name
```

## Security Tips

- **Keep the `.env` file secure**: Ensure that your `.env` file has restricted permissions to avoid unauthorized access:

```bash
chmod 600 ~/.saml2aws-mfa-auto-auth.env
```

**Alternative Secure Storage**: For added security, consider storing secrets in a secure store, like AWS Secrets Manager or a password manager CLI (e.g., Bitwarden CLI).

## Troubleshooting

- **Environment Variables Not Set**: Make sure you have `python-dotenv` installed and that the `.env` file is properly formatted.
- **Alias Not Working**: Ensure the alias points to the correct path of `auto_saml2aws.py`.
- **Missing Dependencies**: Double-check that you have installed all dependencies listed in `requirements.txt`.
- **AWS Configure**: If you get prompted with `aws configure` when you run any AWS CLI commands, it just means you haven't exported the AWS Profile that you intend to use.


## Additional Configuration

If you need to update any values, you can edit the `.env` file directly or rerun the script with updated environment variables.

## Example Usage

Once configured, running the tool will automate your login process for AWS with SAML and MFA. Ensure that your `.env` file is set up correctly with all required values.

Simply run:
```bash
samlautoauth
```
This command will use the information in your `.env` file to generate a TOTP code, authenticate with AWS using `saml2aws`, and complete the login process automatically.














