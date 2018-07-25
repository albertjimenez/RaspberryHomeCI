# TODO Runs the tests and receives the INT signal of the process, if SIGNAL > 0 error, else OK
from subprocess import run, CompletedProcess, PIPE

from ISender import ISender


class HandlerTest:
    def __init__(self, msg_sender: "ISender"):
        if not issubclass(type(msg_sender), ISender):
            raise TypeError("{0} is not subclass of type ISender".format(type(msg_sender)))
        self.msg_sender = msg_sender

    def handle_java_maven(self):
        result = self._run_process("mvn", "test")
        if result.returncode > 0:
            # If the execution returned non-zero exit process
            self.msg_sender.send_msg(
                "Error during the execution of mvn test\n{0}".format(result.stdout.decode('utf-8')))
        else:
            # When the test works
            self.msg_sender.send_msg("Successfully tested")

    def handle_npm(self):
        result = self._run_process("npm", "install", "--production")
        result = self._run_process("npm", "test")
        if result.returncode > 0:
            # If the execution returned non-zero exit process
            self.msg_sender.send_msg(
                "Error during the execution of npm test\n{0}".format(result.stdout.decode('utf-8')))
        else:
            # When the test works
            self.msg_sender.send_msg("Successfully tested")

    def _run_process(self, *kwargs) -> "CompletedProcess":
        return run(kwargs, stdout=PIPE)
