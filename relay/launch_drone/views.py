from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
from django.http import HttpResponse

import libardrone
drone = libardrone.ARDrone()


def launch(request):
    drone.takeoff()
    return HttpResponse(fly)

def landing(request):
    drone.land()
    return HttpResponse("ok")

fly ="""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>
        launch drone
    </title>
    <link rel="stylesheet" href="/static/font-awesome.min.css">
    <script type="text/javascript" src="/static/jquery.min.js"></script>
	<script type="text/javascript" src="/static/bootstrap.min.js"></script>
    <link rel="stylesheet" href="launch.css">


    <link rel="stylesheet" href="/static/bootstrap.min.css">


</head>
<body>


    <div class="deploy">
    <!--<input type="button" onclick="'httpGet('/takeoff')" class="btn btn-lg btn-danger">Deploy Drone</input>-->
    <a href="/down">
        Team Relay Drone is on its way to you.
        <button type="button" " class="btn btn-lg btn-danger">Landing</button>
    </a>
    </div>

<script>
function httpGet(theUrl)
{
    console.log(theUrl);
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, true ); // false for synchronous request
    xmlHttp.send( null );
}
</script>
</body>
</html>
"""