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

The main temple is dedicated to Kali, the Divine Mother, here worshipped as Bhavatarini, the Saviour of the Universe. The floor of this temple also is paved with marble. The basalt image of the Mother, dressed in gorgeous gold brocade, stands on a white marble image of the prostrate body of Her Divine Consort, Siva, the symbol of the Absolute. On the feet of the Goddess are, among other ornaments, anklets of gold. Her arms are decked with jewelled ornaments of gold. She wears necklaces of gold and pearls, a golden garland of human heads, and a girdle of human arms. She wears a golden crown, golden ear-rings, and a golden nose-ring with a pearl-drop. She has four arms. The lower left hand holds a severed human head and the upper grips a blood-stained sabre. One right hand offers boons to Her children; the other allays their fear. The majesty of Her posture can hardly be described. It combines the terror of destruction with the reassurance of motherly tenderness. For She is the Cosmic Power, the totality of the universe, a glorious harmony of the pairs of opposites. She deals out death, as She creates and preserves. She has three eyes, the third being the symbol of Divine Wisdom; they strike dismay into the wicked, yet pour out affection for Her devotees.

The whole symbolic world is represented in the temple garden — the Trinity of the Nature Mother (Kali), the Absolute (Siva), and Love (Radhakanta), the Arch spanning heaven and earth. The terrific Goddess of the Tantra, the soul-enthralling Flute-Player of the Bhagavata, and the Self-absorbed Absolute of the Vedas live together, creating the greatest synthesis of religions. All aspects of Reality are represented there. But of this divine household, Kali is the pivot, the sovereign Mistress. She is Prakriti, the Procreatrix, Nature, the Destroyer, the Creator. Nay, She is something greater and deeper still for those who have eyes to see. She is the Universal Mother, "my Mother" as Ramakrishna would say, the All-powerful, who reveals Herself to Her children under different aspects and Divine Incarnations, the Visible God, who leads the elect to the Invisible Reality; and if it so pleases Her, She takes away the last trace of ego from created beings and merges it in the consciousness of the Absolute, the undifferentiated God. Through Her grace "the finite ego loses itself in the illimitable Ego — Atman — Brahman". (Romain Holland, Prophets of the New India, p. 11.)

Rani Rasmani spent a fortune for the construction of the temple garden and another fortune for its dedication ceremony, which took place on May 31, 1855.

Sri Ramakrishna — henceforth we shall call Gadadhar by this familiar name —1 came to the temple garden with his elder brother Ramkumar, who was appointed priest of the Kali temple. Sri Ramakrishna did not at first approve of Ramkumar's working for the sudra Rasmani. The example of their orthodox father was still fresh in Sri Ramakrishna's mind. He objected also to the eating of the cooked offerings of the temple, since, according to orthodox Hindu custom, such food can be offered to the Deity only in the house of a brahmin. But the holy atmosphere of the temple grounds, the solitude of the surrounding wood, the loving care of his brother, the respect shown him by Rani Rasmani and Mathur Babu, the living presence of the Goddess Kali in the temple, and; above all, the proximity of the sacred Ganges, which Sri Ramakrishna always held in the highest respect, gradually overcame his disapproval, and he began to feel at home.

Within a very short time Sri Ramakrishna attracted the notice of Mathur Babu, who was impressed by the young man's religious fervour and wanted him to participate in the worship in the Kali temple. But Sri Ramakrishna loved his freedom and was indifferent to any worldly career. The profession of the priesthood in a temple founded by a rich woman did not appeal to his mind. Further, he hesitated to take upon himself the responsibility for the ornaments and jewelry of the temple. Mathur had to wait for a suitable occasion.

At this time there came to Dakshineswar a youth of sixteen, destined to play an important role in Sri Ramakrishna's life. Hriday, a distant nephew2 of Sri Ramakrishna, hailed from Sihore, a village not far from Kamarpukur, and had been his boyhood friend. Clever, exceptionally energetic, and endowed with great presence of mind, he moved, as will be seen later, like a shadow about his uncle and was always ready to help him, even at the sacrifice of his personal comfort. He was destined to be a mute witness of many of the spiritual experiences of Sri Ramakrishna and the caretaker of his body during the stormy days of his spiritual practice. Hriday came to Dakshineswar in search of a job, and Sri Ramakrishna was glad to see him.

Unable to resist the persuasion of Mathur Babu, Sri Ramakrishna at last entered the temple service, on condition that Hriday should be asked to assist him. His first duty was to dress and decorate the image of Kali.

One day the priest of the Radhakanta temple accidentally dropped the image of Krishna on the floor, breaking one of its legs. The pundits advised the Rani to install a new image, since the worship of an image with a broken limb was against the scriptural injunctions. But the Rani was fond of the image, and she asked Sri Ramakrishna's opinion. In an abstracted mood, he said: "This solution is ridiculous. If a son-in-law of the Rani broke his leg, would she discard him and put another in his place? Wouldn't she rather arrange for his treatment? Why should she not do the same thing in this case too? Let the image be repaired and worshipped as before." It was a simple, straightforward solution and was accepted by the Rani. Sri Ramakrishna himself mended the break. The priest was dismissed for his carelessness, and at Mathur Babu's earnest request Sri Ramakrishna accepted the office of priest in the Radhakanta temple.


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

