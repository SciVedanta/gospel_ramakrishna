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

At the age of sixteen Gadadhar was summoned to Calcutta by his elder brother Ramkumar, who wished assistance in his priestly duties. Ramkumar had opened a Sanskrit academy to supplement his income, and it was his intention gradually to turn his younger brother's mind to education. Gadadhar applied himself heart and soul to his new duty as family priest to a number of Calcutta families. His worship was very different from that of the professional priests. He spent hours decorating the images and singing hymns and devotional songs; he performed with love the other duties of his office. People were impressed with his ardour. But to his studies he paid scant attention.

Ramkumar did not at first oppose the ways of his temperamental brother. He wanted Gadadhar to become used to the conditions of city life. But one day he decided to warn the boy about his indifference to the world. After all, in the near future Gadadhar must, as a householder, earn his livelihood through the performance of his brahminical duties; and these required a thorough knowledge of Hindu law, astrology, and kindred subjects. He gently admonished Gadadhar and asked him to pay more attention to his studies. But the boy replied spiritedly: "Brother, what shall I do with a mere bread-winning education? I would rather acquire that wisdom which will illumine my heart and give me satisfaction for ever."


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

