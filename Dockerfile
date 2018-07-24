# Image of latest python 3.7 currently
FROM resin/raspberry-pi-python:latest
# Define a variable with my GIT repo and the folder
ENV repo_url https://github.com/albertjimenez/RaspberryHomeCI.git
ENV repo_folder RaspberryHomeCI
# Update the package list
RUN apt-get update
# Clone my REPO containing all the python code
RUN git clone ${repo_url}
# install the requirements
RUN pip install -r RaspberryHomeCI/requirements.txt
# Expose the port 5000 which is used by Flask
EXPOSE 5000
# Final command
CMD ["python", "RaspberryHomeCI/main/main.py", "YOUR_SLACK_WEBHOOK"]