# TODO Runs the tests and receives the INT signal of the process, if SIGNAL > 0 error, else OK
import os
from subprocess import run, CompletedProcess, PIPE

from ISender import ISender


class HandlerTest:
    def __init__(self, msg_sender: "ISender"):
        if not issubclass(type(msg_sender), ISender):
            raise TypeError("{0} is not subclass of type ISender".format(type(msg_sender)))
        self.msg_sender = msg_sender

    def handle_java_maven(self, full_name: "str", clone_url: "str"):
        self._git_clone_pull(full_name, clone_url)

        result = self._run_process("mvn", "test", "-f", full_name.split("/")[1] + "/pom.xml")
        if result.returncode > 0:
            # If the execution returned non-zero exit process
            print("Error mvn")
            self.msg_sender.send_msg(
                "Error during the execution of mvn test\n{0}".format(result.stdout.decode('utf-8')))
        else:
            # When the test works
            print("Test Ok mvn")
            self.msg_sender.send_msg("Successfully tested")

    def handle_npm(self, full_name: "str", clone_url: "str"):
        self._git_clone_pull(full_name, clone_url)
        project_name = full_name.split("/")[1]
        result = self._run_process("npm", "--prefix", "./{0}".format(project_name), "install",
                                   "./{0}".format(project_name), "--production")
        result = self._run_process("npm", "test", "--prefix", "./{0}".format(project_name))
        if result.returncode > 0:
            # If the execution returned non-zero exit process
            self.msg_sender.send_msg(
                "Error during the execution of npm test\n{0}".format(result.stdout.decode('utf-8')))
        else:
            # When the test works
            self.msg_sender.send_msg("Successfully tested")

    def _run_process(self, *kwargs) -> "CompletedProcess":
        return run(args=list(kwargs), stdout=PIPE)

    def _git_clone_pull(self, full_name: "str", git_url: "str"):
        print("Full_name {0} GIT URL {1}".format(full_name, git_url))
        user, project_name = full_name.split("/")
        print("USER {0} PROJECT NAME {1}".format(user, project_name))

        if os.path.exists("{0}".format(project_name)):
            self._run_process("git", "pull")
        else:
            self._run_process("git", "clone", git_url)
