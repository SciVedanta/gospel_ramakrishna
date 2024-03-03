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

And, indeed, he soon discovered what a strange Goddess he had chosen to serve. He became gradually enmeshed in the web of Her all-pervading presence. To the ignorant She is, to be sure, the image of destruction; but he found in Her the benign, all-loving Mother. Her neck is encircled with a garland of heads, and Her waist with a girdle of human arms, and two of Her hands hold weapons of death, and Her eyes dart a glance of fire; but, strangely enough, Ramakrishna felt in Her breath the soothing touch of tender love and saw in Her the Seed of Immortality. She stands on the bosom of Her Consort, Siva; it is because She is the Sakti, the Power, inseparable from the Absolute. She is surrounded by jackals and other unholy creatures, the denizens of the cremation ground. But is not the Ultimate Reality above holiness and unholiness? She appears to be reeling under the spell of wine. But who would create this mad world unless under the influence of a divine drunkenness? She is the highest symbol of all the forces of nature, the synthesis of their antinomies, the Ultimate Divine in the form of woman. She now became to Sri Ramakrishna the only Reality, and the world became an unsubstantial shadow. Into Her worship he poured his soul. Before him She stood as the transparent portal to the shrine of Ineffable Reality.

The worship in the temple intensified Sri Ramakrishna's yearning for a living vision of the Mother of the Universe. He began to spend in meditation the time not actually employed in the temple service; and for this purpose he selected an extremely solitary place. A deep jungle, thick with underbrush and prickly plants, lay to the north of the temples. Used at one time as a burial ground, it was shunned by people even during the day-time for fear of ghosts. There Sri Ramakrishna began to spend the whole night in meditation, returning to his room only in the morning with eyes swollen as though from much weeping. While meditating, he would lay aside his cloth and his brahminical thread. Explaining this strange conduct, he once said to Hriday: "Don't you know that when one thinks of God one should be freed from all ties? From our very birth we have the eight fetters of hatred, shame, lineage, pride of good conduct, fear, secretiveness, caste, and grief. The sacred thread reminds me that I am a brahmin and therefore superior to all. When calling on the Mother one has to set aside all such ideas." Hriday thought his uncle was becoming insane.

As his love for God deepened, he began either to forget or to drop the formalities of worship. Sitting before the image, he would spend hours singing the devotional songs of great devotees of the Mother, such as Kamalakanta and Ramprasad. Those rhapsodical songs, describing the direct vision of God, only intensified Sri Ramakrishna's longing. He felt the pangs of a child separated from its mother. Sometimes, in agony, he would rub his face against the ground and weep so bitterly that people, thinking he had lost his earthly mother, would sympathize with him in his grief. Sometimes, in moments of scepticism, he would cry: "Art Thou true, Mother, or is it all fiction — mere poetry without any reality? If Thou dost exist, why do I not see Thee? Is religion a mere fantasy and art Thou only a figment of man's imagination?" Sometimes he would sit on the prayer carpet for two hours like an inert object. He began to behave in an abnormal manner, most of the time unconscious of the world. He almost gave up food; and sleep left him altogether.

But he did not have to wait very long. He has thus described his first vision of the Mother: "I felt as if my heart were being squeezed like a wet towel. I was overpowered with a great restlessness and a fear that it might not be my lot to realize Her in this life. I could not bear the separation from Her any longer. Life seemed to be not worth living. Suddenly my glance fell on the sword that was kept in the Mother's temple. I determined to put an end to my life. When I jumped up like a madman and seized it, suddenly the blessed Mother revealed Herself. The buildings with their different parts, the temple, and everything else vanished from my sight, leaving no trace whatsoever, and in their stead I saw a limitless, infinite, effulgent Ocean of Consciousness. As far as the eye could see, the shining billows were madly rushing at me from all sides with a terrific noise, to swallow me up! I was panting for breath. I was caught in the rush and collapsed, unconscious. What was happening in the outside world I did not know; but within me there was a steady flow of undiluted bliss, altogether new, and I felt the presence of the Divine Mother." On his lips when he regained consciousness of the world was the word "Mother".


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

