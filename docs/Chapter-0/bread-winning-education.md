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

The anguish of the inner soul of India found expression through these passionate words of the young Gadadhar. For what did his unsophisticated eyes see around him in Calcutta, at that time the metropolis of India and the centre of modem culture and learning? Greed and lust held sway in the higher levels of society, and the occasional religious practices were merely outer forms from which the soul had long ago departed. Gadadhar had never seen anything like this at Kamarpukur among the simple and pious villagers. The sadhus and wandering monks whom he had served in his boyhood had revealed to him an altogether different India. He had been impressed by their devotion and purity, their self-control and renunciation. He had learnt from them and from his own intuition that the ideal of life as taught by the ancient sages of India was the realization of God.

When Ramkumar reprimanded Gadadhar for neglecting a "bread-winning education", the inner voice of the boy reminded him that the legacy of his ancestors — the legacy of Rama, Krishna, Buddha, Sankara, Ramanuja, Chaitanya — was not worldly security but the Knowledge of God. And these noble sages were the true representatives of Hindu society. Each of them was seated, as it were, on the crest of the wave that followed each successive trough in the tumultuous course of Indian national life. All demonstrated that the life current of India is spirituality. This truth was revealed to Gadadhar through that inner vision which scans past and future in one sweep, unobstructed by the barriers of time and space. But he was unaware of the history of the profound change that had taken place in the land of his birth during the previous one hundred years.

Hindu society during the eighteenth century had been passing through a period of decadence. It was the twilight of the Mussalman rule. There were anarchy and confusion in all spheres. Superstitious practices dominated the religious life of the people. Rites and rituals passed for the essence of spirituality. Greedy priests became the custodians of heaven. True philosophy was supplanted by dogmatic opinions. The pundits took delight in vain polemics.

In 1757 English traders laid the foundation of British rule in India. Gradually the Government was systematized and lawlessness suppressed. The Hindus were much impressed by the military power and political acumen of the new rulers. In the wake of the merchants came the English educators, and social reformers, and Christian missionaries — all bearing a culture completely alien to the Hindu mind. In different parts of the country educational institutions were set up and Christian churches established. Hindu young men were offered the heady wine of the Western culture of the late eighteenth and early nineteenth centuries, and they drank it to the very dregs.

The first effect of the draught on the educated Hindus was a complete effacement from their minds of the time-honoured beliefs and traditions of Hindu society. They came to believe that there was no transcendental Truth; The world perceived by the senses was all that existed. God and religion were illusions of the untutored mind. True knowledge could be derived only from the analysis of nature. So atheism and agnosticism became the fashion of the day. The youth of India, taught in English schools, took malicious delight in openly breaking the customs and traditions of their society. They would do away with the caste-system and remove the discriminatory laws about food. Social reform, the spread of secular education, widow remarriage, abolition of early marriage — they considered these the panacea for the degenerate condition of Hindu society.

The Christian missionaries gave the finishing touch to the process of transformation. They ridiculed as relics of a barbarous age the images and rituals of the Hindu religion. They tried to persuade India that the teachings of her saints and seers were the cause of her downfall, that her Vedas, Puranas, and other scriptures were filled with superstition. Christianity, they maintained, had given the white races position and power in this world and assurance of happiness in the next; therefore Christianity was the best of all religions. Many intelligent young Hindus became converted. The man in the street was confused. The majority of the educated grew materialistic in their mental outlook. Everyone living near Calcutta or the other strong-holds of Western culture, even those who attempted to cling to the orthodox traditions of Hindu society, became infected by the new uncertainties and the new beliefs.

But the soul of India was to be resuscitated through a spiritual awakening. We hear the first call of this renascence in the spirited retort of the young Gadadhar: "Brother, what shall I do with a mere bread-winning education?"

Ramkumar could hardly understand the import of his young brother's reply. He described in bright colours the happy and easy life of scholars in Calcutta society. But Gadadhar intuitively felt that the scholars, to use one of his own vivid illustrations, were like so many vultures, soaring high on the wings of their uninspired intellect, with their eyes fixed on the charnel-pit of greed and lust. So he stood firm and Ramkumar had to give way.


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

