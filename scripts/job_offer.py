import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import mistune
from lektor.project import Project
import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--offer-slug', prompt='Slug of the job offer')
@click.option('--recipient', prompt='Recipient email address')
def send(offer_slug, recipient):
    send_email_for_job_offer(offer_slug, recipient)


@click.command()
@click.option('--offer-slug', prompt='Slug of the job offer')
def render(offer_slug):
    email_data = get_email_data_for_job_offer(offer_slug)
    click.echo("""
<title>{subject}</title>
{body}
    """.format(subject=email_data['subject'], body=email_data['body']))

cli.add_command(send)
cli.add_command(render)


def send_email_for_job_offer(offer_slug, recipient):
    credentials = get_email_credentials_from_env()
    email_data = get_email_data_for_job_offer(offer_slug)
    send_email(
        user=credentials['username'],
        pwd=credentials['password'],
        recipient=recipient,
        subject=email_data['subject'],
        body=email_data['body'].encode('utf-8'))
    click.echo('Email successfully sent')


def get_email_credentials_from_env():
    credentials = {
        'username': os.environ.get('EMAIL_USERNAME'),
        'password': os.environ.get('EMAIL_PASSWORD')
    }
    if not credentials['username']:
        raise ValueError('EMAIL_USERNAME required env variable not set')

    if not credentials['password']:
        raise ValueError('EMAIL_PASSWORD required env variable not set')

    return credentials


def get_email_data_for_job_offer(offer_slug):
    page = get_page(offer_slug)
    return {
        'subject': 'Job offer: %s' % page['title'],
        'body': render_html(page)
    }


def get_page(offer_slug):
    project = Project.discover()
    env = project.make_env()
    pad = env.new_pad()

    page = pad.get('/job-offers/%s' % offer_slug)

    if page is None:
        raise ValueError('Job offer with slug "%s" not found' % offer_slug)

    return page


EMAIL_TEMPLATE = """
<h1>{title}</h1>
{body_html}
"""


def render_html(page):
    body_html = mistune.markdown(page['description'].source)
    return EMAIL_TEMPLATE.format(title=page['title'], body_html=body_html)


def send_email(user, pwd, recipient, subject, body):
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = user
    message['To'] = recipient
    html = MIMEText(body, 'html', _charset='utf-8')
    message.attach(html)

    message_string = message.as_string()

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)

    server.sendmail(user, recipient, message_string)
    server.close()

if __name__ == '__main__':
    cli()
