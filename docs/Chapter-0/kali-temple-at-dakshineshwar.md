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

At that time there lived in Calcutta a rich widow named Rani Rasmani, belonging to the sudra caste, and known far and wide not only for her business ability, courage, and intelligence, but also for her largeness of heart, piety, and devotion to God. She was assisted in the management of her vast property by her son-in-law Mathur Mohan.

In 1847 the Rani purchased twenty acres of land at Dakshineswar, a village about four miles north of Calcutta. Here she created a temple garden and constructed several temples. Her Ishta, or Chosen Ideal, was the Divine Mother, Kali.

The temple garden stands directly on the east bank of the Ganges. The northern section of the land and a portion to the east contain an orchard, flower gardens, and two small reservoirs. The southern section is paved with brick and mortar. The visitor arriving by boat ascends the steps of an imposing bathing-ghat which leads to the chandni, a roofed terrace, on either side of which stand in a row six temples of Siva. East of the terrace and the Siva temples is a large court, paved, rectangular in shape, and running north and south. Two temples stand in the centre of this court, the larger one, to the south and facing south, being dedicated to Kali, and the smaller one, facing the Ganges, to Radhakanta, that is, Krishna, the Consort of Radha. Nine domes with spires surmount the temple of Kali, and before it stands the spacious natmandir, or music hall, the terrace of which is sup- ported by stately pillars. At the northwest and southwest corners of the temple compound are two nahabats, or music towers, from which music flows at different times of day, especially at sunup, noon, and sundown, when the worship is performed in the temples. Three sides of the paved courtyard — all except the west — are lined with rooms set apart for kitchens, store-rooms, dining-rooms, and quarters for the temple staff and guests. The chamber in the northwest angle, just beyond the last of the Siva temples, is of special interest to us; for here Sri Ramakrishna was to spend a considerable part of his life. To the west of this chamber is a semicircular porch overlooking the river. In front of the porch runs a foot-path, north and south, and beyond the path is a large garden and, below the garden, the Ganges. The orchard to the north of the buildings contains the Panchavati, the banyan, and the bel-tree, associated with Sri Ramakrishna's spiritual practices. Outside and to the north of the temple compound proper is the kuthi, or bungalow, used by members of Rani Rasmani's family visiting the garden. And north of the temple garden, separated from it by a high wall, is a powder-magazine belonging to the British Government.


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

