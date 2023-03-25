import boto3
import time

hint = '''
help         - See this hint
send <msg>   - Send message
receive      - Receive messages
exit         - Delete queue and exit program
        '''

client = None
queue_url = None


def create_queue():
    global client, queue_url
    
    client = boto3.client(
        service_name='sqs',
        endpoint_url='https://message-queue.api.cloud.yandex.net',
        region_name='ru-central1'
    )
    queue_url = client.create_queue(QueueName='turboqueue').get('QueueUrl')
    print(f'Queue created!\nURL: {queue_url}')


def send_message(message):
    id = client.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    ).get('MessageId')
    
    print(f'id: {id}')


def receive_message():
    # Receive sent message
    messages = client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=5
    ).get('Messages')

    if not messages:
        print("No messages received")
        return

    print('Received messages:\n')
    for msg in messages:
        print(msg.get('Body'))
        print('id: ' + msg.get('MessageId'))
        print()

    # Delete processed messages
    for msg in messages:
        client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=msg.get('ReceiptHandle')
        )


def delete_queue():
    client.delete_queue(QueueUrl=queue_url)
    print('Queue deleted')


def main():
    print('Initializing...')
    print(hint)
    create_queue()

    while True:

        action = input('\n>>> ').strip()

        if action.startswith('send '):
            message = action[5:].strip()
            send_message(message)

        elif action == 'receive':
            receive_message()
        
        elif action == 'exit':
            break

        elif action == 'help':
            print(hint)

        else:
            print('Wrong input, try again')

    delete_queue()
    print('Terminating...')


if __name__ == '__main__':
    main()
