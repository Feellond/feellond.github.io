<!DOCTYPE html>
<html>
    <head>
       <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <script src="https://telegram.org/js/telegram-web-app.js"></script>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
              integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <title>Чекбокс в HTML5</title>
        <script>
            function funcLoad(){
                console.log('Script will load now...');
                const params = new URLSearchParams(window.location.search);
                    for (const param of params) {
                      console.log(param);
                    }
                alert("Page is loaded");
            }
        </script>
    </head>
    <body onload="funcLoad()">
        <h1>Hello, world!</h1>
        <div id="content">not inited</div>
        <button onclick="validateData()" type="button" class="btn btn-primary">Show</button>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
                crossorigin="anonymous"></script>
        <!--<script src="static/app.js"></script>-->

        <h2>Изучаемые технологии</h2>
        <form>
            <p>
                <input type="checkbox" checked name="html5"/>HTML5
            </p>
            <p>
                <input type="checkbox" name="dotnet"/>.NET
            </p>
            <p>
                <input type="checkbox" name="java"/>Java
            </p>
            <p>
                <button type="submit">Отправить</button>
            </p>
        </form>
    </body>
</html>
