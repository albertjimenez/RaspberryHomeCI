# Image of latest python 3.7 currently
FROM resin/raspberry-pi-python:3.6-wheezy
# Define a variable with my GIT repo and the folder
ENV repo_url https://github.com/albertjimenez/RaspberryHomeCI.git
ENV repo_folder RaspberryHomeCI
ENV SLACK_WEBHOOK 1
# Update the package list
RUN apt-get update
# Shrink image size
RUN apt-get clean autoclean
RUN apt-get autoremove --yes
RUN rm -rf /var/lib/{apt,dpkg,cache,log}/
# Clone my REPO containing all the python code
RUN git clone ${repo_url}
# Pull the contents if the container already exists
RUN cd ${repo_folder} && git pull
# Set the work directory to the repo_folder
WORKDIR ${repo_folder}
# install the requirements
RUN pip install -r requirements.txt
# Expose the port 5000 which is used by Flask
EXPOSE 5000
# Final command
CMD ["python", "app/main.py"]