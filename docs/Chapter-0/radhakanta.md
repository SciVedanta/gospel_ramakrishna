<!DOCTYPE html>
<html>
<head>
    <title>Text Reader with Progress Bar</title>
    <style>
        .progress-bar {
            width: 0%;
            height: 30px;
            background-color: green;
            text-align: center;
            color: white;
            line-height: 30px;
        }
        .button {
            background-color: blue;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-right: 10px;
        }
        .button:hover {
            background-color: darkgreen;
        }
    </style>
</head>
<body>
<button class="button" onclick="readText()">Read Text</button>
<button class="button" onclick="stopText()">Stop</button>
<div class="progress-bar" id="progress-bar">0%</div>
<div id="text-container">
    <p id="paragraph1">

The temple of Radhakanta, also known as the temple of Vishnu, contains the images of Radha and Krishna, the symbol of union with God through ecstatic love. The two images stand on a pedestal facing the west. The floor is paved with marble. From the ceiling of the porch hang chandeliers protected from dust by coverings of red cloth. Canvas screens shield the images from the rays of the setting sun. Close to the threshold of the inner shrine is a small brass cup containing holy water. Devoted visitors reverently drink a few drops from the vessel.


    </p>
</div>


<script>
    var speechSynthesis = window.speechSynthesis;

    function readText() {
        var paragraphs = document.querySelectorAll('#text-container p');
        var progressBar = document.getElementById('progress-bar');
        var totalLength = 0;
        var readLength = 0;

        paragraphs.forEach(function(paragraph) {
            totalLength += paragraph.textContent.length;
        });

        paragraphs.forEach(function(paragraph, index) {
            var msg = new SpeechSynthesisUtterance(paragraph.textContent);
            msg.onend = function(event) {
                readLength += paragraph.textContent.length;
                var progress = (readLength / totalLength) * 100;
                progressBar.style.width = progress + '%';
                progressBar.textContent = Math.floor(progress) + '%';
            };
            speechSynthesis.speak(msg);
        });
    }

    function stopText() {
        speechSynthesis.cancel();
        var progressBar = document.getElementById('progress-bar');
        progressBar.style.width = '0%';
        progressBar.textContent = '0%';
    }
</script>
</body>
</html>

