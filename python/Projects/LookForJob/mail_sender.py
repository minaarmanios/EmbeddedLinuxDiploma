import yagmail
import os

class MailSender:
    def __init__(self):
        self.username = os.environ.get("EMAIL_USER")
        self.password = os.environ.get("EMAIL_PASS")
        try:
            # Login with OAuth2 (no need for password)
            self.yag = yagmail.SMTP(self.username, oauth2_file="./gmail_secret.json")
            
            print("Logged in successfully with OAuth2!")
        except Exception as e:
            print(f"Failed to login: {e}")
            raise

    def send_email_with_image(self, images: list, recipient="mina.yousry.iti@gmail.com", subject="Email with Image", body="Hello! Please see the attached image."):
        try:
            print(f"Sending images: {images}")
            self.yag.send(
                to=recipient,
                subject=subject,
                contents=body,
                attachments=images
            )
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
