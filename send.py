import pika
import json
import sys


def main():
    if len(sys.argv) != 5:
        print("Usage: {} <server> <exchange> <queue> <message>".format(sys.argv[0]))
        return -1
    send(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


def send(server, exchange, queue, msg):
    credentials = pika.PlainCredentials("privapp",
                                        "ElCieloEsAzul")  # these credentials must be removed, they were createdd for testing purposes
    connection = pika.BlockingConnection(pika.ConnectionParameters(server, 5672, '/', credentials))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange=exchange,
                          routing_key=queue,
                          body=msg)
    print(" [x] Sent {}".format(msg))
    connection.close()


if __name__ == "__main__":
    main()
