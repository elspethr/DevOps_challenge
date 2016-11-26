#Dev Ops Interview Challenge Project
------

This project contains a simple app "app.py" that allows a user to upload a
photo and then displays the photo. The file "tester.py" runs a simple
test to ensure the

A working version of the app is hosted at: <https://dvchallenge.herokuapp.com>

This project is linked to a drone continuous integration server (on DigitalOcean) that runs the test code each time the repository is updated.

To set up the continous integration server, I followed the instructions [here]
(https://www.digitalocean.com/community/tutorials/how-to-perform-continuous-integration-testing-with-drone-io-on-coreos-and-docker)
with some modification to the Docker image (adding python and the
required packages). This setup could potentially be mostly automated using a bash script.
