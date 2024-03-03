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

Born in an orthodox brahmin family, Sri Ramakrishna knew the formalities of worship, its rites and rituals. The innumerable gods and goddesses of the Hindu religion are the human aspects of the indescribable and incomprehensible Spirit, as conceived by the finite human mind. They understand and appreciate human love and emotion, help men to realize their secular and spiritual ideals, and ultimately enable men to attain liberation from the miseries of phenomenal life. The Source of light, intelligence, wisdom, and strength is the One alone from whom comes the fulfilment of desire. Yet, as long as a man is bound by his human limitations, he cannot but worship God through human forms. He must use human symbols. Therefore Hinduism asks the devotees to look on God as the ideal father, the ideal mother, the ideal husband, the ideal son, or the ideal friend. But the name ultimately leads to the Nameless, the form to the Formless, the word to the Silence, the emotion to the serene realization of Peace in Existence-Knowledge-Bliss Absolute. The gods gradually merge in the one God. But until that realization is achieved, the devotee cannot dissociate human factors from his worship. Therefore the Deity is bathed and clothed and decked with ornaments. He is fed and put to sleep. He is propitiated with hymns, songs, and prayers. And there are appropriate rites connected with all these functions. For instance, to secure for himself external purity, the priest bathes himself in holy water and puts on a holy cloth. He purifies the mind and the sense-organs by appropriate meditations. He fortifies the place of worship against evil forces by drawing around it circles of fire and water. He awakens the different spiritual centres of the body and invokes the Supreme Spirit in his heart. Then he transfers the Supreme Spirit to the image before him and worships the image, regarding it no longer as clay or stone, but as the embodiment of Spirit, throbbing with Life and Consciousness. After the worship the Supreme Spirit is recalled from the image to Its true sanctuary, the heart of the priest. The real devotee knows the absurdity of worshipping the Transcendental Reality with material articles — clothing That which pervades the whole universe and the beyond, putting on a pedestal That which cannot be limited by space, feeding That which is disembodied and incorporeal, singing before That whose glory the music of the spheres tries vainly to proclaim. But through these rites the devotee aspires to go ultimately beyond rites and rituals, forms and names, words and praise, and to realize God as the All-pervading Consciousness.

Hindu priests are thoroughly acquainted with the rites of worship, but few of them are aware of their underlying significance. They move their hands and limbs mechanically, in obedience to the letter of the scriptures, and repeat the holy mantras like parrots. But from the very beginning the inner meaning of these rites was revealed to Sri Ramakrishna. As he sat facing the image, a strange transformation came over his mind. While going through the prescribed ceremonies, he would actually find himself encircled by a wall of fire protecting him and the place of worship from unspiritual vibrations, or he would feel the rising of the mystic Kundalini through the different centres of the body. The glow on his face, his deep absorption, and the intense atmosphere of the temple impressed everyone who saw him worship the Deity.

Ramkumar wanted Sri Ramakrishna to learn the intricate rituals of the worship of Kali. To become a priest of Kali one must undergo a special form of initiation from a qualified guru, and for Sri Ramakrishna a suitable brahmin was found. But no sooner did the brahmin speak the holy word in his ear than Sri Ramakrishna, overwhelmed with emotion, uttered a loud cry and plunged into deep concentration.

Mathur begged Sri Ramakrishna to take charge of the worship in the Kali temple. The young priest pleaded his incompetence and his ignorance of the scriptures. Mathur insisted that devotion and sincerity would more than compensate for any lack of formal knowledge and make the Divine Mother manifest Herself through the image. In the end, Sri Ramakrishna had to yield to Mathur's request. He became the priest of Kali.

In 1856 Ramkumar breathed his last. Sri Ramakrishna had already witnessed more than one death in the family. He had come to realize how impermanent is life on earth. The more he was convinced of the transitory nature of worldly things, the more eager he became to realize God, the Fountain of Immortality.


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

