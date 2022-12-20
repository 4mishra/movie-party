import pika
import json
import sys
import os
import django
import time

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "watch_parties_project.settings")
django.setup()

from watch_parties_app.models import UserVO


def save_user(ch, method, properties, body):
    # print(" [x] %r" % body)
    data = json.loads(body)
    username = data["username"]
    email = data["email"]
    if data["delete"]:
        try:
            count, _ = UserVO.objects.filter(username=username).delete()
            print(f"{username} UserVO deleted: ", count > 0)
        except UserVO.DoesNotExist:
            print("UserVO does not exist: ", username)
    else:
        UserVO.objects.update_or_create(username=username, defaults={"email": email})
        print("successfully created UserVO:", username)


def receive_user():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()

    channel.exchange_declare(exchange="users", exchange_type="fanout")

    result = channel.queue_declare(queue="", exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange="users", queue=queue_name)

    print(" [*] Waiting for users. To exit press CTRL+C")

    channel.basic_consume(
        queue=queue_name, on_message_callback=save_user, auto_ack=True
    )

    channel.start_consuming()


while True:
    time.sleep(5)
    try:
        receive_user()
    except Exception as e:
        print("receive_user ERROR: ", e)
