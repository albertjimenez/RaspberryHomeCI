import abc

'''
@ ISender is the interface to handle the messages, e.g. Slack, Telegram ...
Implement the send_msg function and pass if you need to the daughter class 
the necessary info through the constructor
'''


class ISender(metaclass=abc.ABCMeta):
    '''
    Handles the messages when the CI/CD test is finished
    @:return None
    '''

    @abc.abstractmethod
    def send_msg(self):
        pass
