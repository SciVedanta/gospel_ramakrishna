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
    <p id="paragraph1">IN THE HISTORY of the arts, genius is a thing of very rare occurrence. Rarer still, however, are the competent reporters and recorders of that genius. The world has had many hundreds of admirable poets and philosophers; but of these hundreds only a very few have had the fortune to attract a Boswell or an Eckermann.</p>
    <p id="paragraph2">When we leave the field of art for that of spiritual religion, the scarcity of competent reporters becomes even more strongly marked. Of the day-to-day life of the great theocentric saints and contemplatives we know, in the great majority of cases, nothing whatever. Many, it is true, have recorded their doctrines in writing, and a few, such as St. Augustine, Suso and St. Teresa, have left us autobiographies of the greatest value. But, all doctrinal writing is in some measure formal and impersonal, while the autobiographer tends to omit what he regards as trifling matters and suffers from the further disadvantage of being unable to say how he strikes other people and in what way he affects their lives. Moreover, most saints have left neither writings nor self-portraits, and for knowledge of their lives, their characters and their teachings, we are forced to rely upon the records made by their disciples who, in most cases, have proved themselves singularly incompetent as reporters and biographers. Hence the special interest attaching to this enormously detailed account of the daily life and conversations of Sri Ramakrishna.</p>
    <p id="paragraph3">"M", as the author modestly styles himself, was peculiarly qualified for his task. To a reverent love for his master, to a deep and experiential knowledge of that master's teaching, he added a prodigious memory for the small happenings of each day and a happy gift for recording them in an interesting and realistic way. Making good use of his natural gifts and of the circumstances in which he found himself, "M" produced a book unique, so far as my knowledge goes, in the literature of hagiography. No other saint has had so able and indefatigable a Boswell. Never have the small events of a contemplative's daily life been described with such a wealth of intimate detail. Never have the casual and unstudied utterances of a great religious teacher been set down with so minute a fidelity. To Western readers, it is true, this fidelity and this wealth of detail are sometimes a trifle disconcerting; for the social, religious and intellectual frames of reference within which Sri Ramakrishna did his thinking and expressed his feelings were entirely Indian. But after the first few surprises and bewilderments, we begin to find something peculiarly stimulating and instructive about the very strangeness and, to our eyes, the eccentricity of the man revealed to us in "M's" narrative. What a scholastic philosopher would call the "accidents" of Ramakrishna's life were intensely Hindu and therefore, so far as we in the West are concerned, unfamiliar and hard to understand; its "essence", however, was intensely mystical and therefore universal. To read through these conversations in which mystical doctrine alternates with an unfamiliar kind of humour, and where discussions of the oddest aspects of Hindu mythology give place to the most profound and subtle utterances about the nature of Ultimate Reality, is in itself a liberal, education in humility, tolerance and suspense of judgment. We must be grateful to the translator for his excellent version of a book so curious and delightful as a biographical document, so precious, at the same time, for what it teaches us of the life of the spirit.</p>
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

